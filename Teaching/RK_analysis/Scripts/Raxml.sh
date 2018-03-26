#!/bin/bash
#PBS -q workq
#PBS -l nodes=1:ppn=1
#PBS -l walltime=6:00:00
#PBS -N pasta   
#PBS -o paup.out
#PBS -j oe
#PBS -A loni_selu_gt
#PBS -m a
#PBS -M    

module load raxml

datapath=/work/amwright/Paleantology/Data/Morph
cd $datapath

raxmlHPC-PTHREADS-SSE3 -m MULTIGAMMA -p 12345 -q partition.txt -s combined -n startingTree