import subprocess
import os
from natsort import natsorted
import re
import dendropy
from dendropy import Tree
import math
from dendropy.calculate import treecompare
import matplotlib.pyplot as plt
import numpy as np
from PyQt4 import QtCore

"""
Functions for calculating statistics for sequence windows and for
 ~
comparison to species tree.
Chabrielle Allen
Travis Benedict
Peter Dulworth
"""

class StatisticsCalculations(QtCore.QThread):
    def __init__(self, parent=None):
        super(StatisticsCalculations, self).__init__(parent)

    def newick_reformat(self, newick):
        """
        Reformat the inputted newick string to work with the PhyloNet jar file
        "(a:2.5,(b:1.0,c:1.0):1.5)" This format works
        "(a:2.0,(b:1.0,c:1.0):1.0);" This format works
        "(a:2.0,(b:1.0,c:1.0)):1.0;" THIS FORMAT DOES NOT WORK --- trees from RAxML are in this format
        Inputs:
        newick --- an incorrectly formatted newick string
        Output:
        newick --- a correctly formatted newick string
        """

        # Find root length and remove it
        pattern = "(?!.*\))(.*?)(?=\;)"

        newick = re.sub(pattern, '', newick)

        return newick

    def calculate_p_of_gt_given_st(self, species_tree, gene_tree):
        """
        Computes the probability that a gene tree occurs given a species tree. If the taxon names between the two trees are not the
        same then the probability returned is 0.0. If trees are the exact same then probability is 1.0.
        Inputs:
        species_tree --- a newick string containing a species tree with branch lengths as outputted by RAxML or inputted by user
        gene_tree --- a newick string containing a gene tree with branch lengths as outputted by RAxML run on windows
        Output:
        p_of_gt_given_st --- the probability that a gene tree occurs given a species tree.
        """

        # If species_tree input is a file read in the newick string
        if os.path.isfile(species_tree):
            with open(species_tree) as f:
                species_tree = f.readline()

        # Check if the species tree is formatted correctly for PhyloNet if not reformat it
        if species_tree[-2] != ")" or species_tree[-1] != ")":
            # species_tree = newick_reformat(species_tree).replace("\n","")
            species_tree = species_tree.replace("\n","")

        # If gene_tree input is a file read in the newick string
        if os.path.isfile(gene_tree):
            with open(gene_tree) as f:
                gene_tree = f.readline()

        # Check if the gene tree is formatted correctly for PhyloNet if not reformat it
        if gene_tree[-2] != ")" or gene_tree[-1] != ")":
            # gene_tree = newick_reformat(gene_tree).replace("\n","")
            gene_tree = gene_tree.replace("\n","")

        # IF YOU COMMENT THIS OUT AGAIN EVERYTHING WILL BREAK
        # add quotes to the strings
        species_tree = str(species_tree)
        species_tree = "'"+ species_tree +"'"
        gene_tree = "'" + gene_tree + "'"

        # Run PhyloNet jar file
        p = subprocess.Popen("java -jar ./pstgt.jar {0} {1}".format(species_tree, gene_tree), stdout=subprocess.PIPE, shell=True)

        # Read output and convert to float
        p_of_gt_given_st = p.stdout.readline()

        return p_of_gt_given_st

    def calculate_windows_to_p_gtst(self, species_tree):
        """
        Calculate p(gt|st) for each window and create a mapping
        of window numbers to probabilities.
        Inputs:
        species_tree --- a newick string containing a species tree
                        with branch lengths as outputted by RAxML or
                        inputted by user
        Output:
        windows_to_p_gtst --- a mapping of window numbers to their p(gt|st).
        """

        # Initialize a mapping
        windows_to_p_gtst = {}

        # Iterate over each folder in the given directory
        for filename in natsorted(os.listdir("RAxML_Files")):

            # If file is the file with the best tree newick string
            if os.path.splitext(filename)[0] == "RAxML_bestTree":

                window_num = (os.path.splitext(filename)[1]).replace(".","")

                gene_tree_filename = os.path.join("RAxML_Files", filename)

                p_gtst = self.calculate_p_of_gt_given_st(species_tree, gene_tree_filename)

                # Reformat output
                p_gtst = float(p_gtst.replace('\r', '').replace('\n', ''))

                windows_to_p_gtst[window_num] = p_gtst

        return windows_to_p_gtst

    def calculate_robinson_foulds(self, species_tree, gene_tree, weighted):
        """
        Calculates the Robinson Foulds distances for weighted and unweighted
        trees.

        Input:
        species_tree -- newick file or newick string containing the species tree
        gene_tree   -- newick file or newick string containing the tree to
                          be compared to the species tree
        weighted       -- boolean parameter for whether the files have weights

        Returns:
        The weighted and/or unweighted Robinson Foulds distance of the species
        tree and input tree.
        """

        # taxon names
        tns = dendropy.TaxonNamespace()

        # Create dendropy tree from species tree input file
        if os.path.isfile(species_tree):
            species_tree = Tree.get_from_path(species_tree, 'newick', taxon_namespace=tns)

        # Create dendropy tree from species tree input newick string
        else:
            species_tree = Tree.get_from_string(species_tree, 'newick', taxon_namespace=tns)

        # Create dendropy tree from gene tree input file
        if os.path.isfile(gene_tree):
            gene_tree = Tree.get_from_path(gene_tree, 'newick', taxon_namespace=tns)

        # Create dendropy tree from gene tree input newick string
        else:
            gene_tree = Tree.get_from_string(gene_tree, 'newick', taxon_namespace=tns)

        # both weighted and unweighted foulds distance
        if weighted:
            return treecompare.weighted_robinson_foulds_distance(species_tree, gene_tree), \
                   treecompare.unweighted_robinson_foulds_distance(species_tree, gene_tree)

        # only unweighted foulds distance
        else:
            return treecompare.unweighted_robinson_foulds_distance(species_tree, gene_tree)

    def calculate_windows_to_rf(self, species_tree, weighted):
        """
        Calculate Robinson-Foulds distance for each window and create a
        mapping of window numbers to RF distance.
        Inputs:
        species_tree --- a newick string containing a species tree with
                         branch lengths as outputted by RAxML or inputted
                         by user
        weighted --- a boolean corresponding to calculating the weighted
                     or unweighted RF distance
        Output:
        windows_to_rf --- a mapping of window numbers to their RF distance.
        """

        # Initialize a mapping for the weighted and unweighted RF distance
        windows_to_w_rf = {}
        windows_to_uw_rf = {}

        # Iterate over each folder in the given directory
        for filename in natsorted(os.listdir("RAxML_Files")):

            # If file is the file with the best tree newick string
            if os.path.splitext(filename)[0] == "RAxML_bestTree":
                # makes file and calculates rf distance
                window_num = (os.path.splitext(filename)[1]).replace(".", "")

                gene_tree_filename = os.path.join("RAxML_Files", filename)

                rf_distance = self.calculate_robinson_foulds(species_tree, gene_tree_filename, weighted)

                if weighted:

                    # Weighted RF
                    windows_to_w_rf[window_num] = rf_distance[0]
                    # Unweighted RF
                    windows_to_uw_rf[window_num] = rf_distance[1]

                else:

                    # Unweighted RF
                    windows_to_uw_rf[window_num] = rf_distance

        # returns weighted and/or unweighted Robinson Foulds mappings
        if weighted:
            return windows_to_w_rf, windows_to_uw_rf

        else:
            return windows_to_uw_rf

    def stat_scatter(self, stat_map, name, title, xlabel, ylabel):
        """
        Creates a scatter plot with the x-axis being the
        windows and the y-axis being the statistic to
        be graphed.

        Input:
        stat_map -- a mapping outputted by either
                    calculate_windows_to_p_gtst or
                    calculate_windows_to_rf ([0] or [1])
        name -- the name of the save file
        title -- the title of the plot
        xlabel -- the label for the x axis
        ylabel -- the label for the y axis

        Returns:
        A scatter plot with windows as the x-axis and
        a statistic as the y-axis.
        """
        # sizes plot circles
        area = math.pi * (3) ** 2

        x_list = []

        # makes x values integers
        xlist = stat_map.keys()
        for j in range(len(xlist)):
            x_list.append(int(xlist[j]))

        x = np.array(x_list)

        # gets y values from dictionary
        ylist = stat_map.values()
        y = np.array(ylist)

        plt.scatter(x, y, s=area, c='#000000', alpha=1)

        # label the axes
        plt.xlabel(xlabel, fontsize=10)
        plt.ylabel(ylabel, fontsize=10)

        plt.title(title, fontsize=15)
        plt.tight_layout()
        plt.savefig(name)

        plt.clf()


    def calculate_d(self, window_directory, window_offset):
        """
        Calculates the D statistic for the given alignment
        Input:
        window_directory --- the location of the folder containing the phylip window files
        window_offset --- the offset that was used to create the windows
        Output:
        d_stat --- the D statistic value
        windows_to_d --- a mapping of window indices to D values
        """

        # Initialize the site index to 0
        site_idx = 0

        # Initialize values for the d statistic numerator and denominator
        d_numerator = 0
        d_denominator = 0

        windows_to_d = {}

        # Iterate over each folder in the given directory in numerical order
        for filename in natsorted(os.listdir(window_directory)):

            # If file is a phylip file get the number of the window
            if filename.endswith(".phylip"):
                file_number = filename.replace("window", "")
                file_number = int(file_number.replace(".phylip", ""))

                input_file = os.path.join(window_directory, filename)

                sequence_list = []

                with open(input_file) as f:

                    # Create a list of each line in the file
                    lines = f.readlines()

                    # First line contains the number and length of the sequences
                    first_line = lines[0].split()
                    number_of_sequences = int(first_line[0])
                    length_of_sequences = int(first_line[1])

                for line in lines[1:]:
                    # Add each sequence to a list
                    sequence = line.split()[1]
                    sequence_list.append(sequence)

                # Initialize values for the d statistic numerator and denominator for each window
                numerator_window = 0
                denominator_window = 0

                # Iterate over the indices in each window
                for window_idx in range(length_of_sequences):

                    site = []

                    # Iterate over each sequence in the alignment
                    for sequence in sequence_list:
                        # Add each base in a site to a list
                        site.append(sequence[window_idx])

                    # site[0], site[1], site[2], site[3] are P1, P2, P3 and O respectively for D statistic algorithm
                    P1, P2, P3, O = site[0], site[1], site[2], site[3]

                    # Case of ABBA
                    if P1 == O and P2 == P3 and P1 != P2:
                        ABBA = 1
                        BABA = 0

                    # Case of BABA
                    elif P1 == P3 and P2 == O and P1 != P2:
                        ABBA = 0
                        BABA = 1

                    # Neither case
                    else:
                        ABBA = 0
                        BABA = 0

                    numerator_window += (ABBA - BABA)
                    denominator_window += (ABBA + BABA)

                    # Increment the site index
                    site_idx += 1

                # Calculate d statistic for the window
                d_window = numerator_window / float(denominator_window)

                # Map the window index to its D statistic
                windows_to_d[file_number] = d_window

                # Add the numerator and denominator of each window to the overall numerator and denominator
                d_numerator += numerator_window
                d_denominator += denominator_window

                # Account for overlapping windows
                site_idx += (window_offset - length_of_sequences)

        d_stat = d_numerator/float(d_denominator)

        return d_stat, windows_to_d


if __name__ == '__main__':
    # Inputs
    species_tree = "ChillLeo_species_tree.0"
    weighted = True

    sc = StatisticsCalculations()

    # Run commands
    windows_to_p_gtst = sc.calculate_windows_to_p_gtst(species_tree)
    # stat_scatter(windows_to_p_gtst, "PGTST")

    # # Unweighted Robinson-Foulds
    # if not weighted:
    #     windows_to_uw_rf = calculate_windows_to_rf(species_tree, weighted)
    #     stat_scatter(windows_to_uw_rf, "unweightedRF")
    #
    # # Weighted Robinson-Foulds
    # if weighted:
    #     windows_to_w_rf, windows_to_uw_rf = calculate_windows_to_rf(species_tree, weighted)
    #     stat_scatter(windows_to_w_rf, "weightedRF")
    #     stat_scatter(windows_to_uw_rf, "unweightedRF")

    window_directory = "windows"
    window_offset = 50000
    d, windows_to_d = sc.calculate_d(window_directory, window_offset)
    print d
    sc.stat_scatter(windows_to_d, "winstoD.png", "Window Indices to D statistic", "Window Indices", "D statistic values")
