## Table of Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Analysis Modes](#analysis-modes)
    - [RAxML](#raxml)
    - [File Converter](#file-converter)
    - [MS Comparison](#ms-comparison)
    - [D Statistic](#d-statistic)
- [Figures](#figures)
- [Output Files](#output-files)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Contributors](#contributors)
- [References](#references)

## Introduction

PhyloVis is a python-based application that provides an intuitive user interface for phylogenetic analyses and data visualization. It has four distinct modes that are useful for different types of phylogenetic analysis: RAxML, File Converter, MS Comparison, and D-Statistic.

![Welcome](https://user-images.githubusercontent.com/6343193/28720952-4041d668-7374-11e7-829e-0fd22521cfc8.png)

RAxML mode gives users a front-end to interact with RAxML (STAMATAKIS 2014a) for Maximum Likelihood based inference of large phylogenetic trees. PhyloVis’s RAxML mode allows one to use RAxML to automatically perform sliding window analysis over an inputted alignment. Users are able to select from a plethora of options in performing their analysis, including: window size, window offset, and number of bootstraps. In this mode, users are able to produce a variety of graphs to help understand their genomic alignment and interpret the trees outputted by RAxML. These graph options include: a tree visualization of the top topologies, scatter plot of windows to their topologies, frequency of top topologies, genome atlas, and a heat map of the informative sites. RAxML mode also provides support for calculating two statistics based on the trees produced within each window as compared to an overall species tree; Robinson-Foulds distance and probability of a gene tree given a species tree.

The file converter in PhyloVis provides a user interface for a Biopython AlignIO file converter function. It allows users to convert between twelve popular genome alignment file types. RAxML mode only accepts phylip-sequential format.
MS Comparison mode allows users to perform an accuracy comparison between a “truth file” and one or more files in MS format or the results of RAxML mode.
With D-Statistic mode, users can compute Patterson’s D-Statistic for determining introgression in a four taxa alignment. D-Statistic mode can produce graphs for the value of the D-Statistic across sliding windows as well as the value of the D-Statistic across the entire alignment.

## Requirements

PhyloVis currently runs on Mac and Windows operating systems and selects the proper operating system automatically. Python 2.7 is required for this GUI, along with the additional libraries: BioPython, DendroPy, ETE, SciPy, PIL, SVGUtils, Reportlab, natsort and PyQt4. RAxML is also required for performing analysis in RAxML mode.

Avoid special characters, such as diacritics, spaces, and punctuation other than dots (“.”) and underscores (“_”)  in the names of the PhyloVis folder and all input files. 

## Analysis Modes

### RAxML
In RAxML mode, there are three analysis sections containing preferences for adjusting the statistics. After selecting a file in phylip-sequential format, standard or advanced RAxML options, types of graphs to be generated, and statistical plots can be modified to fit the user’s preferences.

In standard mode, the window size, window offset, and the number of top topologies to be analyzed can be inputted manually as integers greater than one. The model type can be selected from six popular types. Bootstrapping can also be selected; if it is, the user can input the confidence level and the number of bootstraps to be performed. The user can also choose to root the tree at a specific outgroup in the input file.

![RAxML-Standard](https://user-images.githubusercontent.com/6343193/28720944-3af69d42-7374-11e7-8c19-7fc336c5e428.png)

In advanced mode, the user can input a custom RAxML command in which the -s and -n flags are handled internally. A species tree can also be generated using a custom RAxML command,. Rooting is available for this as well.

![RAxML-Advanced](https://user-images.githubusercontent.com/6343193/28720942-396f2304-7374-11e7-8548-85dd6c7b2e1d.png)

For more information regarding RAxML and its commands see the [RAxML manual](https://sco.h-its.org/exelixis/resource/download/NewManual.pdf)

The user can select up to five graphs to be generated, including: Top Topologies, Windows to Top Topologies, Top Topology Frequency, Genome Atlas, and Informative Sites Heat Map.
The Top Topologies option generates an image containing tree visualizations of the most frequently occurring topologies generated by running RAxML on windows of the previously specified size.
Windows to Top Topologies is a scatter plot in which the x-axis is the window number, and the y-axis is the topology.
Top Topology Frequency is a circle graph showing the number of times each topology occurs; topologies differing from the top topologies are lumped together and categorized as “Other.”
The Genome Atlas is a circular representation of the inputted alignment, showing the RAxML tree topologies for different windows along the alignment. Note that this figure works best for alignments with many windows and is still in development.
Top Topologies, Windows to Top Topologies, Top Topology Frequency, and the Genome Atlas are all generated in such a way that the colors of the topologies correspond with the colors used within the plots.
The Informative Sites Heat Map depicts the informativeness of each site in the data. The more informative the site, the darker the line in the heat map.

![Graph-Options](https://user-images.githubusercontent.com/6343193/28720932-3598db9e-7374-11e7-92c8-31397aedc637.png)

Statistics Options allows the user to select an existing species tree file and generate plots depicting the weighted and/or unweighted Robinson Foulds statistic and the probability of a gene tree given a species tree.

![Statistics-Options](https://user-images.githubusercontent.com/6343193/28720946-3cfdb0f8-7374-11e7-9498-327c70af24d5.png)

### File Converter
File Converter mode allows the user to select a file containing DNA alignments in one of eleven popular formats and convert them to a different file format. After selecting the input file and its format, the user must specify the output file’s name and location along with the desired format.

![File-Converter](https://user-images.githubusercontent.com/6343193/28720928-349f1898-7374-11e7-86ee-86a1abcc9341.png)

For more information regarding file types see [BioPython AlignIO](http://biopython.org/wiki/AlignIO).
### MS Comparison
In MS Comparison mode, the user can specify an MS truth file and the RAxML directory and/or other MS files to compare it to . This mode has options to generate figures for Robinson-Foulds Distance From MS Truth Bar Plot, Percent Matching Sites Bar Plot, and TMRCA Line Graph.

When comparing against the RAxML directory, the user has the option to input the directory containing the RAxML files and choose the window size and offset. This function is meant to be used after performing sliding window analysis in PhyloVis’s RAxML mode. 

When comparing the truth file to other MS files, the user can input multiple MS files for comparison.

The Robinson Foulds Distance from MS Truth Bar Plot depicts the total difference between the trees in the truth file and other files chosen for comparison. 

The Percent Matching Sites Bar Plot shows the percentage of sites in the comparison file(s) that contain trees that match the truth file for both weighted and unweighted analyses. Robinson Foulds distance is used to determine if a tree is considered a match or not.

The TMRCA Line Graph shows the tree height over each site when comparing the truth files and other files. This figure is meant to depict to the differences in the time to most recent common ancestor (TMRCA) between each file.

![MS-Comparison](https://user-images.githubusercontent.com/6343193/28720938-38044bf2-7374-11e7-890a-f711b3a31983.png)

### D-statistic
D-statistic mode allows the user to input an alignment file in phylip-sequential format, choose the window size and offset, and select the location of each outgroup in the tree visual. This mode then generates a scatter plot in which the x-axis is the window number, and the y-axis is the D-statistic value computed for that window.

![D-Statistic](https://user-images.githubusercontent.com/6343193/28720924-30c81a4e-7374-11e7-88b6-cdf02d169af1.png)

For further reading on the D-statistic and its usage see: \
[Green et al. (2010)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5100745/#SD1), 
[Durand et al. (2011)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3144383/),
[Martin et al. (2014)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4271521/) 

## Figures

All figures generated in PhyloVis use a Matplotlib output interface, allowing users to customize figures to their liking. Hovering one’s cursor over the icons at the bottom of each figure’s output window provides a short description of each icon’s usage. The following describes each button from left to right.
 
The home button reformats the plot to the default view. \
The left arrow button changes the plot to its previous view.\
The right arrow button changes the plot back to its former view if the previous view is selected. The arrow cross button allows users to change the view of the figure by panning across the plot.\
The magnifying glass button allows users to zoom to a rectangle on the plot. \
The sliders button allows users adjust the spacing and borders of their plots. The tight layout button gets rid of the border around the plot. \
The plot button allows users to customize the axes and curves of the figure. The axes tab allows users to change the min, max and scale of the axes, along with the title and axes labels. This tab also allows users to automatically generate a legend. The curves tab allows users to select each curve on the plot and alter its label, line style and color. Both the sliders button and plots button can be accessed by the “Configure Plot” menu at the top of the window; they can be found under “Configure Subplots” and “Configure Axis and Curves” respectively. \
The save button allows users to save and export the figure window to a specified location. This functionality can also be accessed under “Save As…” in the “File” menu at the top of the output window.

## Output Files

All output files are automatically saved in various folders in PhyloVis. Windows that are created by RAxML are outputted into the “windows” folder, and are saved as “window0.phylip”, “window1.phylip”, etc. Files outputted by running RAxML are found in the “RAxML_Files” directory. When bootstrap analysis is chosen these files are saved under “RAxML_bestTree”, “RAxML_bipartitions”, “RAxML_bipartitionsBranchLabels”, “RAxML_bootstrap”, and “RAxML_info”. When bootstrapping is not chosen these files are named “RAxML_bestTree”, “RAxML_randomTree”, “RAxML_result”, “RAxML_log”, and “RAxML_info”. Each of these files has “.0”, “.1”, “.2”, etc. extensension corresponding to the index of the window that RAxML was run on. All graphs and images are automatically saved into the plots folder under the name of the image.

For more information regarding the RAxML output files see the [RAxML manual](https://sco.h-its.org/exelixis/resource/download/NewManual.pdf)
## Exporting Files
All images can be exported to a desired save location, renamed and saved as one of the following file types: pdf, png, jpeg, tiff, svg, eps, rgba, pgf, and ps.

### Contributors
- [Chabrielle Allen](https://github.com/chaballen)
- [Travis Benedict](https://github.com/travisbenedict)
- [Peter Dulworth](https://github.com/PeterDulworth)
- [Leo Elworth](https://www.linkedin.com/in/chilleo/)
- [Luay Nakhleh](https://www.cs.rice.edu/~nakhleh/)

### Dependencies
- [BioPython](http://biopython.org/wiki/Documentation)
- [DendroPy](https://www.dendropy.org/)
- [ETE](http://etetoolkit.org/)
- [natsort](https://pypi.python.org/pypi/natsort)
- [PIL](http://www.pythonware.com/products/pil/)
- [PyQt4](http://pyqt.sourceforge.net/Docs/PyQt4/)
- [ReportLab](https://pypi.python.org/pypi/reportlab)
- [SciPy](https://www.scipy.org/)
- [SVGU](https://pypi.python.org/pypi/svgutils)

## Installation
1) Download and install [RAxML](https://sco.h-its.org/exelixis/web/software/raxml/)
    - Tutorial for installing RAxML on Mac: http://www.sfu.ca/biology2/staff/dc/raxml/
    
2) Download and Install [Python2.7.13](https://www.python.org/downloads/)

3) Download and install [SIP and PyQt4](https://www.riverbankcomputing.com/software/pyqt/download)

4) Download and install [PIP](https://pip.pypa.io/en/stable/installing/)

5) Use the following command line commands to install the remaining packages:

    ```
    pip install pillow
    pip install scipy
    pip install natsort
    pip install reportlab
    pip install svgutils
    pip install ete3
    pip install dendropy
    pip install biopython
    ```

6) Download PhyloVis from Github and run main.py

## References

Cock PJA, Antao T, Chang JT, et al. Biopython: freely available Python tools for computational molecular biology and bioinformatics. Bioinformatics. 2009;25(11):1422-1423. doi:10.1093/bioinformatics/btp163.

Durand EY, Patterson N, Reich D, Slatkin M. Testing for Ancient Admixture between Closely Related Populations. Molecular Biology and Evolution. 2011;28(8):2239-2252. doi:10.1093/molbev/msr048.

ETE 3: Reconstruction, analysis and visualization of phylogenomic data. Jaime Huerta-Cepas, Francois Serra and Peer Bork. Mol Biol Evol 2016; doi: 10.1093/molbev/msw046

Green RE, Krause J, Briggs AW, et al. A Draft Sequence of the Neandertal Genome. Science (New York, NY). 2010;328(5979):710-722. doi:10.1126/science.1188021.

Richard R. Hudson; Generating samples under a Wright–Fisher neutral model of genetic variation . Bioinformatics 2002; 18 (2): 337-338. doi: 10.1093/bioinformatics/18.2.337

Hunter, John D. "Matplotlib: A 2D Graphics Environment." Computing in Science & Engineering 9.3 (2007): 90-95. 10.1109/MCSE.2007.55

Martin SH, Davey JW, Jiggins CD. Evaluating the Use of ABBA–BABA Statistics to Locate Introgressed Loci. Molecular Biology and Evolution. 2015;32(1):244-257. doi:10.1093/molbev/msu269.

Stamatakis A. 2014a. RAxML version 8: a tool for phylogenetic analysis and post-analysis of large phylogenies. Bioinformatics 30, 1312–1313. DOI: 10.1093/bioinformatics/btu033.

Stamatakis A. 2014b. The RAxML v8.0.X Manual

Sukumaran, J. and Mark T. Holder. 2010. DendroPy: A Python library for phylogenetic computing. Bioinformatics 26: 1569-1571.

Than C, Ruths D, Nakhleh L (2008) PhyloNet: a software package for analyzing and reconstructing reticulate evolutionary relationships. BMC Bioinformatics 9: 322

Yu Y, Degnan JH, Nakhleh L. The Probability of a Gene Tree Topology within a Phylogenetic Network with Applications to Hybridization Detection. Felsenstein J, ed. PLoS Genetics. 2012;8(4):e1002660. doi:10.1371/journal.pgen.1002660.
