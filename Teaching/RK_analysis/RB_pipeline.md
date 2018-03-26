1. On LONI, open RevBayes and execute the following:

```UNIX
taxa <- readTaxonData("Data/taxa.tsv")

#Import the molecular sequences #this file contains only the #taxa for which sequence data #are available #
filenames <- v("Data/18s.nex", "Data/28s.nex", "Data/ABD.nex","Data/Arg.nex", "Data/CAD.nex", "Data/EF1.nex", "Data/EF2.nex", "Data/lg.nex", "Data/WG.nex")
                                                             
n_data_subsets <- filenames.size()                            
for (i in 1:n_data_subsets) {                                 
   data[i] = readDiscreteCharacterData(filenames[i])
}

# Import the morphological #character matrix #
# this file contains only the #taxa for which morphological #characters are available 

morpho <- readDiscreteCharacterData("Data/AntMegaMatrixMinusAmbig.nex")

# Add the missing taxa to each data partition #
for (i in 1:n_data_subsets) {                                 
    data[i].addMissingTaxa( taxa )
}
       
morpho.addMissingTaxa( taxa )
writeNexus(file="molecular", data[i])
writeNexus(file="morphological", morpho)

```

2. Exit RevBayes
3. Remove the headers and footers from each data file, but make note of how many taxa and characters are in each.
4. Now, pull off the taxa in the molecular file:

```
tr -s ' ' < molecular | cut -d' ' -f2 > moldat
```

5. And combine the two files:
```
paste -d,  morphological moldat > combined
```
6. Now, enter the file, and at the top, separated by tabs, enter the number of taxa and total number of characters (molecular characters + morphological). If I have 759 taxa, 163 morphological characters and 300 molecular characters, this line will look like so:

759   463

7. Next, you will make a partition file. It will look like this:

MULTI, p1=1-163
DNA, p2=164-543

Except, you'll fill in the number of molecular characters you have. It might vary.

Save it as partition.txt.

8. Now, run RAxML as 

```
raxmlHPC -m MULTIGAMMA -p 12345 -q partition.txt -s combined -n startingTree
```

You can either complete this step on your personal machine, or on LONI. I've put a qsub file for LONI in the git repo under scripts.

This will give you some output in the form of RAxML_*. You'll look for the file RAxML_bestTree.startingtree. Move this file into the data directory. 

7. You'll also need to create two accessory files, taxa.tsv and FossInt.tsv. Taxa is all the taxa on the tree (morphology + mol + just dates), FossInt is the age of all the fossils.

I've created two scripts that write these files. They are in the scripts directory of the main repo - feel free to move them into the scripts directory of the RK_analysis folder, if that's easier for you. 

```python

../../Scripts/TaxonListParser.py -h
usage: TaxonListParser.py [-h] [--mol MOL] [--morph MORPH] [--foss FOSS]
                          [--ages AGES] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --mol MOL        Path to nexus or fasta file containing molecular data.
                   Should end in .nex, .fasta or .fa.
  --morph MORPH    Path to nexus-formatted file containing morphological data.
                   Should end in .nex.
  --foss FOSS      Path to TSV or CSV file containing the fossils you'd like
                   to include in the analysis
  --ages AGES      Path to data ages TSV or CSV file containing ages of non-
                   contemporaneous tips, if any exist in your analysis.
  --output OUTPUT  Path to where you'd like to write output

```

So the arguments you'll provide are: one of the molecular data files (does not matter which), the morphological data matrix, one of the fossil files you made (you'll need to run this step for EACH FBD analysis you execute), and the path to the FossilTRNS file, and where you want to put the output (I'd put it in data, but whatever's fine). The FBD analysis assumes it is in the data folder, and is called taxa.tsv.

For example: 

```
../../Scripts/TaxonListParser.py --mol Data/18s.nex --morph Data/AntMegaMatrixMinusAmbig.nex --foss Data/Tribe_max.tsv --ages ../../Data/Morph/FossilTNRS.csv --output taxa.tsv
```

generates the taxon list file for that Tribe_max file you sent.

FossInterval works like this:

```
usage: FossInterval.py [-h] [--set SET] [--ages AGES] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --set SET        Path to the taxon TSV or CSV file containing all fossils
                   and all tips on the tree.
  --ages AGES      Path to data ages TSV or CSV file containing ages of non-
                   contemporaneous tips, if any exist in your analysis.
  --output OUTPUT  Path to where you'd like to write output
```
  
 So you'll provide the foss set you made, the FossTRNS file and the output you'd like to write. The FBD analysis assumes it is in the data folder, and is called FossInt.tsv.
 
 
8. Now, you're ready to execute the revbayes analysis. Make sure all the files (including the starting tree, if you ran it on your personal machine) are on LONI. Submit the revbayes.sh file.



