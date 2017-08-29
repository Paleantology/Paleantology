# Chapter One: An Introduction to Project Organization

## Introduction: How can we maintain tractable data structures for use with phylogenetic 
projects?

"I just wasted five hours running an analysis on the wrong input file."

"I can't remember where I saved my output."

"I accidentally overwrote my raw data."

Many of us have probably said one or more of the above sentences. When you're balancing 
multiple projects and lots of data, it can be easy to lose track of files.
One of the biggest challenges to any project is placing project files in a structure that 
is easy for you, the scientist, to access and maintain. 

This chapter will cover the basics of project organization and data organization and management. 
At the end of this chapter, you should be familiar with:

1. *Concept:* How to store project input files, scripts and project outputs
2. *Concept:* How to organize your data in a way that is reusable for you, and for others
3. *Hands-On:* How to use the command line to create directories, move files and view the 
files that you have

## Creating Project Workspaces

This book will discuss not solely the Dendropy computing library, but efficient Python computation
for phylogenetic analyses. In this section, we are going to address a very specific aim:
setting up projects on your computer in a way that will allow you to manage your projects 
efficiently. We will use hands-on examples throughout this section.

When managing a project, you want to *keep files together as much as possible*. Doing this 
makes it easier to document your project, and avoid losing data files. For example, let's create
a directory at the command line for all of our project data. We will do this in UNIX, not 
Python right away. The reason for this is that most servers, Macintosh and Linux machines 
will have the tools to do this available. UNIX is a very commonly-used tool. Open your 
command line and type:

```UNIX
mkdir phylo_data_science
```

This has created a new directory in your computer called phylo_data_science. You can think of this
as a workspace for all the phylo_data_science files. If a file is related to this tutorial, 
it should go here. The directory is currently empty. You can try navigating to this directory 
using your normal file viewer. We're now going to put some content into this directory. 
Open a test editor of your choosing. In the file write a short note about why you have 
created this directory. For example, in my directory, I wrote 

```
This directory contains files for a tutorial on using data science to learn phylogenetics
```

save this as README.txt. Now, at the command line, type:

```
cd phylo
```

then hit tab. What happens when you hit tab? The whole file name pops up! This behavior is 
called *tab completion*, and it's incredibly useful. Tab completion saves you from typing 
out the whole file name (and potentially making typos). If you press tab and nothing comes 
up? Then you know that either you haven't entered enough characters to make a unique match 
- for example, if you have phylo_data_science and phylo_Bayesian, or that the file doesn't 
exist in the directory you're in. 

We are now in the phylo_data_science directory. If you type 

```UNIX
ls
```
you should see the README file you made. If you don't see it, check that you've saved the 
file correctly. If you have, check that you're in the right directory by typing

```UNIX
pwd
```

for print working directory. If something went wrong in your cd command, this will let you 
know.

Now, we will make four subdirectories.

```UNIX

mkdir scripts
mkdir data
mkdir output
mkdir documentation
```

These four subdirectories will all serve important purposes. Our scripts directory will house
the Python code we will write. We will talk in further chapters about why it is important
and useful to keep all of the scripts for a single project together. For now, just know that 
it is. 

Our data directory will house our raw data. We want our raw data to be housed on its own. If 
we make a mistake in how we save output files, we can always go back to our raw data and 
run the analysis again ... so long as we have maintained the integrity of our raw data. 
Once we have populated our data directory with the necessary data, we do not write to it. 
A simple motto for this philosophy is that *data are read-only*. 

We do, however, write to our output directory. We will talk in future chapters about using 
Python to make readable and informative output file names. For now, just know that the results 
of _any_ analysis go in the output directory.

Documentation is where we can put miscellaneous, informative files. For example, papers that
you are reading for your project, cost sheets for sequencing, talk slides.

This is the basic setup all chapters of this book will rely on. This manner of file organization
is very transparent: anyone looking at your file directory can understand what components 
of your research project are stored where. If you follow this structure, when you go to 
publish your paper, you can simply archive your entire project directory to meet most 
funders' and journal's guidelines for providing data and software code. And who couldn't 
use a little less on their plate when it comes time to submit a paper?

### Recap: Our Three Goals

So far, we have introduced two important concepts: *keep files together as much as possible* 
and *data are read-only*. The first principle means to keep data, output and code related to
one project in one place on your computer to increase your organization. The second principle
means to treat raw data as untouchable. Any outputs of analyses should be kept separate to
avoid loss of data, and to ensure you can rerun any steps as needed.

In learning these two concepts, we have used hands-on commands: mkdir to create directories, 
ls to look at their contents and cd to navigate. We also learned to check our navigation with
the pwd command and to use tab-complete to increase the efficiency of our typing.

# Chapter Two: Moving From Spreadsheets to Python

## Introduction

"I know I made a plot of this ... I just can't remember how."

"This looks totally different on my computer."

"My coworker doesn't have Excel."

Almost everyone used a spreadsheet program to manage data at some point in our career. These
graphical programs offer a clean interface to view and manage the data we work so hard to 
collect. But these types of programs can also introduce problems in biological workflows.

There are three main issues with using Excel and other similar programs to carry out computations:

1. *They can be black boxes.* Most spreadsheet programs are closed-source, meaning that their 
inner workings might not be examineable by users because the source code is not available. 
Exceptions to this do exist, such as Open Office. Behaviors can also vary between platforms
(i.e., Macintosh vs. Windows) or across versions of the software in ways that are somewhat 
unpredictable.
2. *You need to maintain a separate log file with your commands.* As we'll see in this section,
programmatically working with data provides an inherent log of all the commands you did. As
long as you provide the version number of the Python distribution and any libraries you're 
working with, a colleague should be able to reproduce what you did exactly. By contrast, to
do this in a spreadsheet program requires either writing out exactly what data were
 highlighted  and what options were clicked on.
3. *Reuse and batching is tricky.* When you are using a spreadsheet program, you are 
generally performing operations on one file at a time. Many spreadsheet programs have a system,
often called macros, that allows for a series of operations to be carried out in several 
spreadsheet files. But you often still need to click each file to open it, and start your
macro. Writing code that can be reused because it explicitly lists every operation performed 
allows us to process large batches of files in a way that simply isn't possible with spreadsheet 
programs.

In this chapter, we will discuss moving data management and analysis past the traditional
spreadsheet paradigm. Along the way, we will learn about how to store data in a way that is
both human- and machine-readable. Using a test dataset on ant (Formicidae) taxonomy, we will
import datasets using Python and begin to explore them programmatically. At the end of this chapter, you will be familiar 
with:

1. *Concept:* How to store data and documentation in a way that is useful to you, colleagues
and is machine-readable.
2. *Concept:* How the Pandas Python library can be used to move beyond reliance on spreadsheets.
3. *Hands-On:* Commands to load libraries in the Python language and to begin calling useful functions for data manipaltion.

## Storing Data

When you save a file in Excel, you don't simply save the data. You save, encoded in binary,
information about cell positioning, coloring, and other document attributes. In the previous 
section, we mentioned that the behavior of a file loaded into a spreadsheet viewing program 
can vary between versions of the software. This is not because the data are changing. This
is because there are often subtle changes to how the data are displayed or how statistics 
are calculated. These subtle changes can cause dramatically different renderings of files
across versions and platforms. 

All of this extraneous information also makes the file harder to read at the command line, 
or in Python. For example, in the data directory, you will find two data files: Ants.csv and 
Ants.xlsx. At the command line, type:



```UNIX

head Data/Ants.csv
head Data/Ants.xlsx
```
**Note for Pat and Andre: If you do this in your own workspaces, you'll need to do:** 

```UNIX

head ../Data/Ants.csv
head ../Data/Ants.xlsx
```

Which of these files are you able to visualize? 

The Ants.csv file is stored in what is called a *flat file*. Flat files are plain text - 
they don't contain any characters that can't be typed with a keyboard, or viewed at the 
command line. Any fancy formatting in a plain text file comes from the viewer. For example,
this book is written in plain text. The nice formatting you see is the result of rendering 
software. If you were to view this file at the command line, you would still be able to 
access all of the data within it. Because flat files can be read by both human and machine,
they are often considered preferable to files with extensive encoding of extra information.

For the purposes of this lesson, we will show you how to get data out of spreadsheet files 
(such as Excel files), but we will predominantly be describing how you can avoid using these
file types. 

Inside each flat file, data should be organized with each row being an observation, and each 
column being the variables observed. If you open the Ants.csv file, you will note that each
row corresponds to one fossil ant. Each column is labeled as a variable observed about the 
ant - taxonomy, age of the fossil and notes. Most programmatic ways of handling data assume 
this structure.  

You will also notice that all the column names have underscores, rather than spaces. Most 
programming languages will assume that a space indicates the end of a name, so it's best to
avoid spaces. Lastly, notice that the data directory also contains a README. This README
tells the user what data files they should expect to find when they download your data.

## The Pandas Library

There are many ways to process data at the command line. These range from simple methods 
available in UNIX to elaborate and complex libraries in R or Python. In this section, we'll 
get to know Pandas a little better. We will use Pandas as a gateway to getting familiar with 
Python. Once we have learned how to carry out some common spreadsheet operations, we will
discuss Python programming more generally in the next chapter. This is by no means an exhaustive 
look at the Pandas library. It is simply a teaser to show some useful ways that you might 
interact with data in Python. 

Pandas was written by Wes McKinney to facilitate efficient data processing, manipulation and 
plotting in Python. The fundamental data type of Pandas is a dataframe, an object containing
rows and columns of data. For our Ants.csv data, the rows will be the fossil ants. The columns
will be the observations (fossil minimum ages, maximum ages, and taxonomy). It's instructive
to look at an example. At the command line, type:

```python
Jupyter notebook
```

This will open an Jupyter Notebook. These notebooks are Python instances, run on your computer,
but rendered in the browser. Browser rendering allows the notebook to have lots of nice features,
like plot rendering and clean visualization of dataframes. Each space for you to type is called
a 'cell'. A cell is a unit of code that can be run independently of all other cells. This 
is very nice for debugging, as we will see later.

In the first cell, type:

```python
import pandas as pd
```

And click 'run'. Pandas is a library for the Python language. Libraries are sets of code, created for a purpose,
and contributed back to Python. Python, being an open source and user-developed language, 
welcomes this. When we tell Python to import a library, we are telling Python to look into
that codebase and make its functions open to us. The 'as pd' is called an alias. Many programmers
prefer to type fewer characters than more, and so will use aliases to shorten the names of 
libraries.

When we load a library, the functions in it can then be called for our use. We do this by
typing the name (or alias) of the library, followed by a dot, and then the name of the function.
For example:

```python

pd.read_csv
```

will return the output:

```python
<function pandas.io.parsers._make_parser_function.<locals>.parser_f>
```

In the command pd.read\_csv, we called the function read\_csv out of the Pandas library. We
haven't provided it with any data to read, therefore, Python simply told us that the function
is available via Pandas to parse text.

Now we will use this function to load some data into Python, via the Pandas library:

```UNIX
ant_data = pd.read_csv('data/Ants.csv')
```
**Note for Pat and Andre: If you do this in your own workspaces, you'll need to do:** 
```UNIX
ant_data = pd.read_csv('../Data/Ants.csv')
```

To view the data, type:

```python
ant_data
```

What we see is the data. We are able to call up the data to view because the data have been 
saved to a variable, ant\_data, which was stored in memory as a dataframe when we called 
pd.read\_csv. 

> ### Challenge:
> Try this command again without saving it to a variable. 
> - What happens? 
> 
> - Is it what you expected? 
> - Why did this happen?

Let's take a closer look at the ant\_data object. On the face of it, it looks very much like 
our Excel file. Now, we'll explore how to access data in this dataframe. Let's start by getting
a look at all the names in the file. There are a couple ways we can do this:

```python
ant_data[[0]]
```

or

```python 
ant_data.specimen
```

In our first block of code, we call the dataframe object and use what is called indexing 
to get the first column. Now, you may be thinking, what is going on with the notation? The 
brackets indicate that we will be accessing a column. Python counts from zero. This may be
somewhat surprising - that the language doesn't start with one. It's actually quite natural-
you weren't born at one year old, were you? But it still takes a little to get used to - 
programmers often verbally say the first item, but they mean the zeroeth item.

In our second block of code, we call the column by its name - specimen. This is a very natural
way to access the data. We gave attributes of the data names, why not use them?

> ### Challenge:

> Try accessing other columns. 
> 
> - When will it be useful to access by name? 
> - When will it not?

We can also select multiple columns at once using our column names. 

```python 
ant_data[['specimen', 'tribe']]
```

> ### Challenge 
> Try to access these same columns using their numerical index of columns. When you have an answer, highlight below to check it against my answer. 
> Remember, Python indexes values from zero, not one!

>! ant_data[[0,3]]

Selecting rows of data is also possible. The below code grab all columns in the fifth row of the dataframe:

```python
ant_data[5:6]
```

This introduces a couple of interesting concepts. The first is using inclusive and exclusive indexing. This is an example of the 5 being inclusive - we will get the fifth row of data. The six is exclusive - we will stop accessing data at the 6th row.

You might notice that we are not using the specimen names as we access data. That is because, by default, Pandas assigns an index to the dataframe. We can alter this default behavior:

```python
ant_data = pd.read_csv('data/Ants.csv', index_col=0)
```

This behavior sets the index to be the zeroeth column in the dataframe, the specimen column. We can now use the names of our specimens to index:

```python
ant_data['Casaleia_eocenica':'Casaleia_eocenica']
```

When we accession this way, the indexing is no longer inclusive. This will return the same taxon is before. In the next chapter, we will look at more efficient ways of performing this selection and slicing. 

> ### Challenge

> Try assigning a subset of columns to an object. Are the objects you assign what you expect, in terms of the number of rows and columns you select? Inclusive vs. exlcusive indexing can be challenging. 

## Recap: Our Three Goals

In this chapter, we have discussed *data storage* using flat files, which can be read by both computers and humans. We introduced Python *libraries* and learned how we can call functions out of a library to do useful tasks for us. And finally, we have started to use a small set of functions in the Pandas library to access data programmatically. In the next chapter, we will build on these concepts to perform a wider range of data tasks.



# Chapter Three: Accessing Complex Combinations of Data

## Introduction

When would we not want to use lists of columns and rows to select data out of a dataframe? When we have a lot of data, which is rapidly becoming the norm in biology. In order to process data at a large scale, we need better tools to allow us to do complex data filtering, selection and manipulation. By using Python, we automatically create a log of all the operations we perform as we access our data. By the end of this chapter, you will understand:

1. *Concept:* How the Pandas library operates to access data in a dataframe.
2. *Concept:* How accessing data programmatically leads to reproducible research by preserving a log of your work.
3. *Hands-On:* Commands for using Pandas to perform common spreadsheet sorting and viewing functions. 

## Data Accession

We will now discuss using what is called 'slicing' to access swaths of data in our dataframe. To do this, we will introduce two new functions, loc and iloc. loc allows for data to be accessed via either the number of the column or row, or the name of the column or row. iloc allows for data to be accessed via the column or row number only.

As an example, let's try to access our same row the previous chapter:

```python
ant_data.iloc[5:6]
ant_data.loc['Casaleia_eocenica']
```

These outputs have the same information, but they look rather different. Try assigning each output to a variable. Now, we will call the type function on each variable. For example, if I called my variables casa_iloc and casa_loc, I would type:

```python
type(casa_iloc)
type(casa_loc)
```

Type is a function that is built in to Python. It allows us to know what sorts of objects our variables are, which in turn tells us about their properties. You will note that the output for the iloc function is a dataframe, with which we are familiar. The output of the loc function is a series, which we have not seen before.

A series is a Pandas object type. It is a one-dimensional array (i.e. not a matrix). In some ways, if a dataframe is like a spreadsheet, a series is like a single row of column in that sheet. More information on the series data type can be found by typing 

```python 
?c_e
```

in your notebook.

If you type 

```python 
c_e.
```

followed by a tab in your iPython notebook, you will see a list of functions available to operate on series. 

> ### Challenge

> Try some of the functions available to the series and dataframe objects. When do you think it might be prefereable to use loc vs. iloc?

Using these complex indexers, we can begin to make multiple selections of data. For example, this syntax will select all values of the subfamily column:

```python
ant_data.loc[:, 'subfamily']
```

What happens if you plug in numbers on either side of the colon to get a selection of columns? Try it!

Pandas doesn't love mixed type indexing. But if you try:

```python
ant_data.loc[['Casaleia_eocenica','Myopopone_sinensis'], 'subfamily']
```

thereby passing in a list of rows that we're interested in getting info from, you can index the data this way.

> ### Challenge

> How could you print the minimum ages for all three Mianeuretus listed in this data file?

The above is more useful and flexible than what we discussed in Chapter Two. But it's still somewhat naive - we need to know where, exactly the data are in the file to retrieve them. We'll now cover a few methods to allow us to sort and access data without knowing this _a priori_.

Something we might want to do is know which of our ants are at least as old as the KPg event, the end of the Cretaceous. Ants are thought to have arisen during the Cretaceous. We can do this easily and assign our sample of old ants to a new dataframe:

```python
old_ants  = ant_data[ant_data.min_ma > 65.5]
```
The way this works is that we select all the values in the dataframe column min_ma that are larger than 65.5. By default, this will take the whole row. Then, we assign that to a new dataframe. We can write this dataframe to a csv file for storeage like so:

```python
pd.to_csv("output/filter_old.csv")
```

> ###Challenge

> - The syntax is a little weird. Can you explain why we have dataframe typed in twice? 
> - Try this again - how could we filter for ants that only existed after the end of the Creatceous? Can we use the same column?
> - When you open the parentheses on a function argument and press tab, you can see all the *arguments*, or special options, available to that function. Try a couple, such as delimiters. Once you've chosen an argument, Shift+Tab will show you possible values for the argument.


We can also use this type of indexing to compare columns. Our max_ma column should always be bigger than min_ma. We can check for rows where this isn't the case - these are errors.

```python
ant_data[ant_data.min_ma > ant_data.max_ma]
```

In our data, we don't have any such errors, but if we did, we could drop them like so:

```python
ant_data = ant_data[ant_data.min_ma > ant_data.max_ma]
```

Does anyone see a problem with what I did there?

I made a mistake and selected only the data that have a minimum age larger than the maximum age, and used it to overwrite the dataframe object! If I overwrote my data for real, this would be a big problem. But I didn't - Python is not doing these operations in the actual spreadsheet. It's doing them on a dataframe held in memorey - our real data are perfectly safe in the Ants.csv file. 

## Programming as a Living Record of Your Work

In the previous command, I switched the inequality to accidentally drop all the values I actually wanted to keep! So far, we've covered some important conceptual data lessons - that data are read-only, that data should be stored in flat files. We will now learn an important lesson as it pertains to code - that code can be saved for later, as an exact record of what we did in a session of programming.

This might not sound that important, but I think most of us have probably been working in a spreadsheet and completely forgotten how we got the useful annotations on a plot, of calculated a summary statistic. In this section, we will cover some best practices for keeping track of what we've done. We will expand on these best practices later, and in more complexity.

For now, let's have a look at the tool we've been using, the Jupyter Notebook. We've been typing into a window in our browser. That window is running Python on our computer, and rendering the output in a nice format using Java. We have code cells, which we have been pasting code into cells and running it. In these notebooks, you can create a new cell, and chenge it's type by selecting something other than code from the dropdown. For example, we could pick 'Markdown' to write notes.

What we are doing when we do this is weaving together code and data to make readable documents that follow our whole workflow. When we are done for a session, we can select 'Save and Checkpoint' from the File menu. This will save our notebook for later. A notebook can be emailed to a collaborator, or, as we will cover later, managed under version control. We can also download the file as a plain Python script in the File menu. We will discuss why we might want to do this in Chapter Four.

Together, what this means is that our code to reproduce the analysis we did is always available. If we need to go back and do it again, for example, if we get more data, that's easy to do. We just run the code again. If a colleague wants to try the analysis again, we can simply send them the code. This is much easier than trying to explain to someone where to click to get a certain option, particularly when spreadsheet softwares are not consistent across platforms.

So what to do with the mistake I made? We can simply go back to our notebook and re-run the steps before I made the mistake, then fix the inequality in the equation. 

## Recap

In this chapter, we have discussed how to programmatically access and read data using the Pandas library. We have used a variety of commands to perform simple data accession, as well as more complex choices involving multiple columns and rows. We even made a mistake in the data that we accessed - and, in the process, learned that we can use the programmatic record to reproduce the steps before we made our mistake to get our data back.


# Chapter Four: Common Spreadsheet Operations and How to Automate Them

## Introduction

We've now learned a bit about how to read in data and access data in using Python. This chapter will guide you through some common operations that researchers often want to do to with data using Python. We will then take a step back and discuss how to use common programming conventions, like loops and lists  to make automating boring tasks easier.

After finishing this chapter, you will usderstand:

1. *Concept:* How data can be subsetted and sorted in the computer's memory. 
2. *Concept:* How lists and loops can be used to perform data analysis tasks multiple times.
3. *Hands On:* Exposure to the Python language's syntax for managing collections of objects.

## Subsetting and Sorting Data 

One common task many researchers do with their data is break it into smaller chunks, perhaps by treatment, to look at effects in that group. We're not working with experiemental data here, but we can certainly split our data up. Ants are known in the literature as the Formicids. This is a family. There are many subfamilies of ants. We might be interested in seeing if we have equal samples of each subfamily. 

We can group our data by subfamily like so:

```python
sub_fams = ant_data.groupby('subfamily')
```

Doing this creates a groupby object, or a list of chunks of our data, identified by the subfamily to which they belong. We can  view them like so:

```python
for fam in sub_fams:
    print(fam)
```

Congratulations, you've written your first loop. What this loop does is, for every object in sub_fams, Python prints the object to the screen. print() is a Python function available in all installations of Python (version 3.0+). 'fam' is what is known as a *loop variable*. Python automatically assumes that, if sub_fams is an object containing other objects, that fam will be the smallest unit of the sub_fams container. In other languages, you might have to assign the loop variable before using it, but Python is pretty smart about figuring out what it is. 

Our original question was if all of the groups are about the same size. So let's answer it:

```python
sub_fams.size()
```

They are not. The samples of Formicinae and Dolichoderinae, for example, are much bigger than the rest. These are also the most specious groups of ants. Could the disparity in the sample be due to group speciousity? I've made a secodn spreadsheet with a rough guess at the species richness of each of the ant groups in this data set. Let's load it:

```python
sub_r = pd.read_csv('data/subfamilyRichness.csv', index_col=0)
```

You'll notice we've added a new option to reading in a csv file - index_col. This allows us to specifiy which column we would like to be the index. In this case, we want the subfamily names to be the index.

To get these two data sources together, we need to do some massaging of our data. Groupby objects can be turned into dataframes in which the index is the groupname (in our case, the subfamily) and the data are the sizes of the group like so:

```python
sizes = pd.DataFrame(sub_fams.size())
```

But this actually gives us a multi-level index that is unsuitable for our purposes. I'm going to have us reset the index to the names of the subfamilies. We're going to do this first by looping over our groupby objects and getting the names of the groups (the subfamily) and putting those in a list. We do this by first creating the list. Then, we initialize our loop. And we take the first value in each groupby group, which is the name of the group.

```python
names = []
for fam in sub_fams:
    names.append(fam[0])
sizes.reset_index
sizes.index = names
```

Once we have executed the loop, we erase the index that exists and reset it to our group names.

>###Challenge  

> - Try calling functions of the groupby objects, for example, mean() on the sub\_fams object. What would these types of functions be helpful for? Remember, once you've typed in sub\_fams. and hit tab, you can see available methods.

## Merging and Using Data

Now we have two dataframes, one with our observed data and one with the number of species that exist in nature. To do mathematical operations using both pieces of data, we will combine them. We will do this using a merge, which combines two datasets on a given column:

```python
new_sizes= sizes.merge(sub_r, left_index=True, right_index=True)

```

In our case, we will merge sizes to sub\_r. We will use the nice indices we just created as our join columns. This is specified by 'left\_index', the index of the object before we call the merge function being set to true, and right_index, the index of the object after we call the merge being set to true. If we had called join with sub_r being first, it would be the left and sizes would be the right. 

The output of this is a new dataframe, with two columns: one from sizes, one from sub_r. We can now divide out our two columns to see if we have sampled some clades more because they are more speciose. If this were true, we would expect to see roughly the same proportion of sampling, but not the same number of samples. We will assign the sampling proportion to a new column called 'proportion'.

```python
new_sizes['proportion'] = new_sizes.reps/new_sizes.size
```

Do these sizes look right? Your answer should be no. It turns out that 'size' is a reserve word, and calls a function called size. This function returns the size of each object in bytes. So instead of dividing each entry in reps by each entry in size we're dividing by bytes. But that's OK, we can rename our columns on the fly:

```python 
new_sizes.columns = ['reps','num_spec','prop']
```

Now try it:

```python
new_sizes['proportion'] = new_sizes.reps/new_sizes.num_spec
```

Much better!


> ###Challenge
> - Try some other mathematical operations. Subtract the columns! 
> - How could you delete a column if you decided you didn't want your mathematical output? (Hint: look at the drop function. Be aware some behaviors are a little odd.) 
> - Think a little about data as read-only: where will you want to save these outputs?

## Recap

In this chapter, we have looked at subsetting our data. We used the groupby command to make 
data subsets along a biologically interesting axis. We then used loops and lists to process 
data and make the process of managing datasets easier. Finally, we joined together multiple 
data objects and used them to perform mathematical operations. In the next chapter, we will 
build on the concepts seen here to further automate data management. 


# Chapter Five: Functions, Scripts and Revision Management 

So far, we've covered the nuts and bolts of programming. We've learned a little bit about how to control Python, and it's time to think about controlling its environment. As you program more and more, you'll need to have maintainable pieces of code, and some framework to maintain them.

In this chapter, we'll cover three core concepts. *Functions*, which are blocks of code that work together to achieve some purpose. We will discuss *scripts*, which may contain one or more functions and the comments needed to interpret and use them. And lastly, we will discuss *revision management*, the practice of using a defined system to track how and when changes are made to your code.

By the end of this chapter, you will be able to:

1. *Concept:* Explain why and how functions can be used to make code more maintainable. 
2. *Concept:* How grouping functions into scripts can make it easier to understand and maintain code.
3. *Concept & Hands-On:* Commands to use a revision management system to keep track of changes to your codebase.

## Functions

We've previously introduced functions in the context of calling functions from a package, like calling read_csv from Pandas. We're now going to discuss making our own functions to do everyday operations that we need.

We can think of a function like an organ of the body - a function is a grouping of code that performs a task. For example, we might write a function that extracts relevant rows from a dataframe and writes them to a file. That's a great idea - let's do that here in a second.

Why would we want to write functions, instead of just stuffing all our code into a file? There are several reasons. Functions provide a natural grouping for blocks of code. This makes it easier, just visually, to see what types of operations our code can do. And programming can be tricky - anything to make it easier will help us. Functions also have defined in and outputs. For example, a function that grabs columns from a dataframe might first check that the dataframe exists, and check that the file you're trying to write your data to doesn't exist so you don't overwrite good data. In this way, functions make it possible for us to better check that our code is working as expected. 

Let's start by defining our function. The definition statement names the function and tells us what toexpect as input to that function. Without the right input, the code will stop executing. A definition statement looks like this:

```python
def extract_rows(file, ant_names):

```

This definition statement is for a function named extract\_rows. This function takes as input a variable called data. I think you can guess where this is going  - data will be the name of a dataframe from which we will extract the rows. It also takes as input a list of names of ants that we would like to extract. Recall that our rows in the dataframe are ant species.

The next thing that comes after the function definition is the docstring, or a comment that explains the purpose of the function.


```python
def extract_rows(data, ant_names):
	'''A function to extract relevant data from dataframe'''
```

Next comes the body of the function, or the actual code. In the data directory, I have added a file called AntTestData.txt, containing a number of ant specimen names. These are the ants we would like to call out of our dataframe. We'll talk in a moment about how to read in a non-CSV text file. For now, write a little bit of code that will pull a single row based on an ant name - let's try Amblyopone_pallipes. Then check your answer below.


```python
def extract_rows(data, ant_names):
	'''A function to extract relevant data from dataframe'''
	new_data = data.loc['Amblyopone_pallipes']
```

But we don't just want one name, we want a bunch of names. And what we have done above is called *hard-coding*. Hard coding is undesireable because it means that every time we want to use different data, we have to change the code. That is dangerous. So what we want to do is rewrite this function to take a bunch of names and fetch them from our data frame. 

So let's get ourselves a list of ant names. 

```python
def get_names(namefile):
	'''Read in a file of names'''
	with open(namefile, 'r') as f:
   		ant_names = f.read().splitlines() 
	return(ant_names)
```
Above, we have added one more function piece - the return statement. The return statement allows us to preserve objects after the function is done running. In this case, we can pass the list of ant names out of the function. The above code does a lot of stuff. First, it takes as input a file of ant names. It uses a with statement to open the file, then uses a function called read to get the data out. Our data have newlines at the end - that's what causes each ant name to be on its own line when we open the file in a text editor. But that will cause the ant names to not be found in our dataframes, since the dataframe doesn't have newlines. Splitlines takes these off. Finally, we return the list of names.

So now we have two functions, one to get our ant names and one to use the ant names to look up ants in the database. Let's rewrite our dataframe function to take a list of names. 

```python
def extract_rows(data, ant_names):
	'''A function to extract relevant data from dataframe'''
	new_data = data.loc[ant_names]
	return(new_data)
```

Our function is complete! We have two functions, both of which are doing use_ful_ and interesting things. Now, let's look at how to make them use_able_ by scripting them into a Python program.

## Python Scripts

We can write functions all day, but they don't run unless called - that is, unless we use their names to invoke them. Now, we will cover how to do this. As of right now, we have two functions:

```python
def extract_rows(data, ant_names):
    '''A function to extract relevant data from dataframe'''
    new_data = data.loc[ant_names]
    return(new_data)

def get_names(namefile):
   '''Read in a file of names'''
   with open(namefile, 'r') as f:
       ant_names = f.read().splitlines() 
   return(ant_names)
```

Open your text editor and past in these two functions.

Before your functions, include the line:

```python
import pandas as pd
```

to import Pandas for your script.

Now, we will build our function calls.

```python

if __name__ == '__main__':
	data = pd.read_csv('Data/Ants.csv' index_col=0)
	namefile = 'Data/AntTestData.txt'
	ant_names = get_names(namefile)
   new_dataframe = extract_rows(data, ant_names)
   new_dataframe.to_csv('Data/processed_ants.csv')
```

This is an odd-looking statement. But in a script the name statement allows us to tell Python which functions to actually call. If we had extra functions that we didn't want to execute, we could just leave them out. 
    
Save this as first_script.py. In the git bash terminal, navigate to where you have saved the script (hopefully in the Spring2017 directory) and type:

```python

python first_script.py

```

You should see a 5-row dataframe pop out.

But we've done something bad. Remember how we said that hard coding was not optimal? They still aren't. So let's think about how to get rid of the hard coding. See how I had you import a mystery modeule - sys? Sys allows us to pass in additional information from the command line. We can use the arg function to take in command-line arguments:
if __name__ == '__main__':
	data = pd.read_csv(sys.argv[1] index_col=0)
	namefile = sys.argv[2]
	ant_names = get_names(namefile)
   new_dataframe = extract_rows(data, ant_names)
   new_dataframe.write_to_csv(sys.argv[3])
```

Now, when we call this script, we type:

```python

python first_script.py Data/Ants.csv Data/AntTestData.txt Data/ant_processed.csv

```

Now, if we want to change the name of the output file, we just change the last argument at the command line. Need a different set of ants? Change the taxon list. Easy. No changing the code for every analysis.

One final thing. Remember that data are read-only? We really oughtn't be writing to our data directory. Let's add just one more function. Add an import statement for the os library, which allows us to manipulate file paths:

```python
import os
```

Now we will write a function to us os to check if an output directory exists, and if not, to create it:

```python
def check_dir(path):
	check = path.split('/')[0] 
	os.listdir(check)
	if 'output' in os.listdir(check):
	    return
	else:
	    os.mkdir('%s/output' % check)  
```

>### Challenge:
>
1. Add a function call for check_dir to the main statement.
2. Explain why check_dir does not have a return statement at the very end.
3. How will you need to modify your invocation of the Python script to make sure your output is written to the right place.
4. What is split doing? 
5. Write a docstring for this function.


## Revision Management

Now we have an actual, working script. This is fantastic - we can send this to a coworker and have them reproduce our analyses. We can use it again later to recall exactly what we did!

Until our coworker emails it back and says it doesn't work, and we open it to find a bunch of changes. Until we accidentally delete a piece of code, close our laptop, and go on vacation. Until our laptop dies.

Enter revision management, for tracking changes to our code (or any other text file - this tutorial was written with revision management). As you're aware, we will be using git for revision management this semester. What we're going to do now is a really swift primer on some of the basic functionality of git and its web interface, GitHub. 

First, we'll do some brief setup:


```
git config --global user.name "Your Name"
$ git config --global user.email "you@youremail"
```

When you do the setup, use the email address you set up GitHub with. That way, GitHub will know the commits are from you and won't reject them (I have added you as collaborators on my project).

I really want you to protect the script we just wrote together. First, add your initials to the name of your script so I know whose is whose. Mine would be first\_script\_amw.py. Now, in the Spring2017 directory, type:

```
git add first_script_yourinitials.py
```

This command lets git know that we're interested in tracking any changes made to this script. Next, we want to commit the script. Committing takes a snapshot of the script, preserving it as it existed in that moment in time. People differ on how often to commit. Some people commit frequently, some people only commit when they are done for the day.

```
git commit
```

This will now ask you for a short message describing what is being committed. You could say something like 'adding ant data parsing script' or 'initial draft of script'. Try for something informative.

Now, we push to the internet:

```
git push
```

This may ask you for your username and password, if you cloned the repository over HTTPS. Once this has completed, you should be able to go to the website for the repository and look at your script!

You might be wondering now where git is storing your log of revisions. If you go up one level like so:

```

cd ..
```

and list hidden files:

```
ls -a
```

you will see a folder called .git. This stores all your checkpoints and snapshots. 

We'll cover more complex Git functionality in the future as we do more work.

> ### Challenge
> 
> Try to find a tpyo to fix in the lessons. Fix it, add the file in git, commit it and push it.
> 






# Chapter Six: HPC?

Following this chapter, there is a short practicum where we will use what we've learned to 
subsample taxonomic data for use in a later phylogenetic analysis.

    Pandas for parsing data
    Grouping data by taxonomic level
    Choosing a subset of data to include - at random, and with clade-structured subsampling
    Writing out the relevant info about what taxa were subsampled

2) Reading character data

    Subsampling character data according to part (1)
    Managing the namespaces
    Using pack to ensure that all data are represented in both datasets (important in BEAST, will shortly be unimportant in RevBayes)
    Writing out the data

3) Processing the output

    Pruning non-data tips from a tree (ie occurrance time taxa)
    Summarizing
    Some sort of short capstone, such as showing how to extract the width of the HPD to demonstrate something about sampling or something.