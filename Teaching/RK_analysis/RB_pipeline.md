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

Now, you're ready to execute the revbayes analysis. Make sure all the files (including the starting tree, if you ran it on your personal machine) are on LONI. Submit the revbayes.sh file.

