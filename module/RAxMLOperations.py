from natsort import natsorted
from sys import platform
import subprocess
import shutil
import os
import re
from PyQt4 import QtCore

"""
Functions for creating sequence windows and running RAxML.
~
Chabrielle Allen
Travis Benedict
Peter Dulworth
"""


class RAxMLOperations(QtCore.QThread):
    def __init__(self, inputFilename, windowSize, windowOffset, numBootstraps, model="GTRGAMMA", bootstrap=False, customRaxmlCommand=False, raxmlCommand="", parent=None):
        super(RAxMLOperations, self).__init__(parent)

        self.inputFilename = inputFilename
        self.windowSize = windowSize
        self.windowOffset = windowOffset
        self.numBootstraps = numBootstraps
        self.customRaxmlCommand = customRaxmlCommand
        self.bootstrap = bootstrap
        self.model = model

    def raxml_species_tree(self, phylip):
        """
        Runs RAxML on input PHYLIP file to create a species
        tree.

        Inputs:
        phylip -- a file inputted by the user.

        Returns:
        A species tree folder.
        """
        # Create output directory
        output_directory = "RAxML_SpeciesTree"

        # Delete the folder and remake it if it already exists
        if os.path.exists(output_directory):
            shutil.rmtree(output_directory)

        os.makedirs(output_directory)

        self.emit(QtCore.SIGNAL('SPECIES_TREE_PER'), 11)

        # Run RAxML
        p = subprocess.Popen(
            "raxmlHPC -f a -x12345 -p 12345 -# 2 -m GTRGAMMA -s {0} -n txt".format(phylip),
            shell=True)
        # Wait until command line is finished running
        p.wait()

        self.emit(QtCore.SIGNAL('SPECIES_TREE_PER'), 50)

        # Regular expression for identifying floats
        float_pattern = "([+-]?\\d*\\.\\d+)(?![-+0-9\\.])"

        # Create a separate file with the topology of the best tree
        with open("RAxML_bestTree.txt") as f:
            # Read newick string from file
            topology = f.readline()

            # Delete float branch lengths, ":" and "\n" from newick string
            topology = ((re.sub(float_pattern, '', topology)).replace(":", "")).replace("\n", "")
            file = open("Topology_bestTree.txt", "w")
            file.write(topology)
            file.close()

        self.emit(QtCore.SIGNAL('SPECIES_TREE_PER'), 20)

        if platform == "win32":
            # Move RAxML output files into their own destination folder - Windows
            os.rename("RAxML_bestTree.txt", output_directory + "\RAxML_ST_bestTree.txt")
            os.rename("RAxML_bipartitions.txt", output_directory + "\RAxML_ST_bipartitions.txt")
            os.rename("RAxML_bipartitionsBranchLabels.txt",
                      output_directory + "\RAxML_ST_bipartitionsBranchLabels.txt")
            os.rename("RAxML_bootstrap.txt", output_directory + "\RAxML_ST_bootstrap.txt")
            os.rename("RAxML_info.txt", output_directory + "\RAxML_ST_info.txt")
            os.rename("topology_bestTree.txt", output_directory + "\Topology_ST_bestTree.txt")

        elif platform == "darwin":
            # Move RAxML output files into their own destination folder - Mac
            os.rename("RAxML_bestTree.txt", output_directory + "/RAxML_ST_bestTree.txt")
            os.rename("RAxML_bipartitions.txt", output_directory + "/RAxML_ST_bipartitions.txt")
            os.rename("RAxML_bipartitionsBranchLabels.txt",
                      output_directory + "/RAxML_ST_bipartitionsBranchLabels.txt")
            os.rename("RAxML_bootstrap.txt", output_directory + "/RAxML_ST_bootstrap.txt")
            os.rename("RAxML_info.txt", output_directory + "/RAxML_ST_info.txt")
            os.rename("topology_bestTree.txt", output_directory + "/Topology_ST_bestTree.txt")

        self.emit(QtCore.SIGNAL('SPECIES_TREE_PER'), 20)

    def window_splitter(self, filename, window_size, step_size):
        """
        Creates smaller PHYLIP files based on a window size inputted into
        the GUI.

        Inputs:
        filename --- name of the PHYLIP file to be used
        window_size --- the number of nucleotides to include in each window
        step_size --- the number of nucleotides between the beginning of each window

        Output:
        Smaller "window" files showing sections of the genome in PHYLIP format.
        """

        output_folder = "windows"

        # Delete the folder and remake it
        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)

        os.makedirs(output_folder)

        # Create a list for the output files
        output_files = []

        with open(filename) as f:
            # First line contains the number and length of the sequences
            line = f.readline()
            line = line.split()

            number_of_sequences = int(line[0])
            length_of_sequences = int(line[1])

            # Initialize a pointer for the beginning of each window
            i = 0
            # Initialize a count for the total number of windows
            num_windows = 0

            # Determine the total number of windows needed
            while (i + window_size - 1 < length_of_sequences):
                i += step_size
                num_windows += 1

            # Create a file for each window and add it to the list
            for i in range(num_windows):
                output_files.append(open(output_folder + "/window" + str(i) + ".phylip", "w"))
                output_files[i].close()

            # Write the number and length of the sequences to each file
            for i in range(num_windows):
                file = open(output_files[i].name, "a")
                file.write(" " + str(number_of_sequences) + " ")
                file.write(str(window_size) + "\n")
                file.close()

            # Subsequent lines contain taxon and sequence separated by a space
            for i in range(number_of_sequences):
                line = f.readline()
                line = line.split()

                taxon = line[0]
                sequence = line[1]

                for j in range(num_windows):
                    l = j * step_size
                    file = open(output_files[j].name, "a")
                    file.write(taxon + " ")
                    window = ""
                    for k in range(window_size):
                        window += sequence[l + k]

                    # Writes file to folder
                    file.write(window + "\n")
                    file.close()

    def raxml_windows(self, numBootstraps, model, window_directory='windows', output_directory='RAxML_Files'):
        """
        Runs RAxML on files in the directory containing files from
        window_splitter().

        Inputs:
        window_directory ---  the window directory location
        """

        topology_output_directory = "Topologies"

        # Delete the folder and remake it if it already exists
        if os.path.exists(output_directory):
            shutil.rmtree(output_directory)

        os.makedirs(output_directory)

        # Delete the folder and remake it if it already exists
        if os.path.exists(topology_output_directory):
            shutil.rmtree(topology_output_directory)

        os.makedirs(topology_output_directory)

        # Iterate over each folder in the given directory in numerical order
        for filename in natsorted(os.listdir(window_directory)):

            # If file is a phylip file run RAxML on it
            if filename.endswith(".phylip"):

                file_number = filename.replace("window", "")
                file_number = file_number.replace(".phylip", "")

                input_file = os.path.join(window_directory, filename)

                # Run RAxML
                if not self.customRaxmlCommand:
                    if self.bootstrap:
                        p = subprocess.Popen( "raxmlHPC -f a -x12345 -p 12345 -# {2} -m {3} -s {0} -n {1}".format(input_file, file_number, numBootstraps, model), shell=True)
                    else:
                        p = subprocess.Popen("raxmlHPC -d -p 12345 -m {2} -s {0} -n {1}".format(input_file, file_number, model), shell=True)
                else: # custom raxml command
                    p = subprocess.Popen(self.raxmlCommand + " -s {0} -n {1}".format(input_file, file_number), shell=True)

                # Wait until command line is finished running
                p.wait()

                # Regular expression for identifying floats
                float_pattern = "([+-]?\\d*\\.\\d+)(?![-+0-9\\.])"

                # Create a separate file with the topology of the best tree
                with open("RAxML_bestTree." + file_number) as f:
                    # Read newick string from file
                    topology = f.readline()

                    # Delete float branch lengths, ":" and "\n" from newick string
                    topology = ((re.sub(float_pattern, '', topology)).replace(":", "")).replace("\n", "")
                    file = open("Topology_bestTree." + file_number, "w")
                    file.write(topology)
                    file.close()

                if self.bootstrap:

                    if platform == "win32":
                        # Move RAxML output files into their own destination folder - Windows
                        os.rename("RAxML_bestTree." + file_number, output_directory + "\RAxML_bestTree." + file_number)
                        os.rename("RAxML_bipartitions." + file_number,
                                  output_directory + "\RAxML_bipartitions." + file_number)
                        os.rename("RAxML_bipartitionsBranchLabels." + file_number,
                                  output_directory + "\RAxML_bipartitionsBranchLabels." + file_number)
                        os.rename("RAxML_bootstrap." + file_number, output_directory + "\RAxML_bootstrap." + file_number)
                        os.rename("RAxML_info." + file_number, output_directory + "\RAxML_info." + file_number)
                        os.rename("topology_bestTree." + file_number,
                                  topology_output_directory + "\Topology_bestTree." + file_number)

                    elif platform == "darwin":
                        # Move RAxML output files into their own destination folder - Mac
                        os.rename("RAxML_bestTree." + file_number, output_directory + "/RAxML_bestTree." + file_number)
                        os.rename("RAxML_bipartitions." + file_number,
                                  output_directory + "/RAxML_bipartitions." + file_number)
                        os.rename("RAxML_bipartitionsBranchLabels." + file_number,
                                  output_directory + "/RAxML_bipartitionsBranchLabels." + file_number)
                        os.rename("RAxML_bootstrap." + file_number, output_directory + "/RAxML_bootstrap." + file_number)
                        os.rename("RAxML_info." + file_number, output_directory + "/RAxML_info." + file_number)
                        os.rename("topology_bestTree." + file_number,
                                  topology_output_directory + "/Topology_bestTree." + file_number)

                else:

                    if platform == "win32":
                        # Move RAxML output files into their own destination folder - Windows
                        os.rename("RAxML_bestTree." + file_number, output_directory + "\RAxML_bestTree." + file_number)
                        os.rename("RAxML_log." + file_number,
                                  output_directory + "\RAxML_log." + file_number)
                        os.rename("RAxML_randomTree." + file_number,
                                  output_directory + "\RAxML_randomTree." + file_number)
                        os.rename("RAxML_result." + file_number,
                                  output_directory + "\RAxML_result." + file_number)
                        os.rename("RAxML_info." + file_number, output_directory + "\RAxML_info." + file_number)
                        os.rename("topology_bestTree." + file_number,
                                  topology_output_directory + "\Topology_bestTree." + file_number)

                    elif platform == "darwin":
                        # Move RAxML output files into their own destination folder - Mac
                        os.rename("RAxML_bestTree." + file_number, output_directory + "/RAxML_bestTree." + file_number)
                        os.rename("RAxML_log." + file_number,
                                  output_directory + "/RAxML_log." + file_number)
                        os.rename("RAxML_randomTree." + file_number,
                                  output_directory + "/RAxML_randomTree." + file_number)
                        os.rename("RAxML_result." + file_number,
                                  output_directory + "/RAxML_result." + file_number)
                        os.rename("RAxML_info." + file_number, output_directory + "/RAxML_info." + file_number)
                        os.rename("topology_bestTree." + file_number,
                                  topology_output_directory + "/Topology_bestTree." + file_number)


                self.emit(QtCore.SIGNAL('RAX_PER'), 80 / len(os.listdir('windows')))

    def run(self):
        self.window_splitter(self.inputFilename, self.windowSize, self.windowOffset)
        self.raxml_windows(self.numBootstraps, self.model)
        self.emit(QtCore.SIGNAL('RAX_COMPLETE'), None)


if __name__ == '__main__':
    # input_file = "testFiles/phylip.txt"
    # window_size = 10
    # window_offset = 10

    inputFile = "../RAxML_SpeciesTree/RAxML_ST_bestTree.txt"
    windowSize = 500000
    windowOffset = 500000
    numBootstraps = 2

    ro = RAxMLOperations(inputFile, windowSize, windowOffset, numBootstraps=2)

    windows_dir = ro.window_splitter(ro.inputFilename, ro.windowSize, ro.windowOffset)
    ro.raxml_windows()
