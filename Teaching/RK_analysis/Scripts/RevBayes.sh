#!/bin/bash
#PBS -q workq
#PBS -l nodes=1:ppn=20
#PBS -l walltime=72:00:00
#PBS -N steppingstonetest  
#PBS -o ss_test.out
#PBS -j oe
#PBS -A loni_selu_gt
#PBS -m abe
#PBS -M 


#### module load gcc
##module unload mvapich2/2.0/INTEL-14.0.2
##module load openmpi/1.8.1/INTEL-14.0.2

datapath=/work/amwright/Paleantology/Data/Morph
cd $datapath

mpirun -np 20 -hostfile $PBS_NODEFILE ~/rb-mpi scripts/mcmc_TEFBD.Rev
