#Install instructions

## Locating the terminal.

Click on the magnifying glass. Type "Terminal" when the search bar pops up. Double-click 
the application. Congratulations, you now have a terminal.

## Installing Git

In this lab, we use Git for doing back-ups of code and data. Eventually, as we progress, we 
will also use Git to do cool things like revert to previous revisions of code, and share data, 
scripts and results amongst our selves.

In the terminal, type:

```
git
```

This will pop-up a visual interface to install Git.

## Installing Python

Python is a really nice, general purpose computing language. We'll use a specific type of Python,
Anaconda, to do our computing activities. 

[This](https://www.anaconda.com/download/) website will walk you through the download.

## Clone our class materials

To interact with a server containing material, we need to first set up our git client. First,
tell it who you are:

```
git config --global user.name "Jane Doe"
git config --global user.email janedoe@example.com
```

When we eventually start sharing code and data with each other, this will be the name listed.

At the command line, type:

```
git clone https://github.com/wrightaprilm/Paleantology.git
```

To copy down our class materials.