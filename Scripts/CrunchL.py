#!/usr/bin/env python3
#Usage: CrunchL.py location_of_files name_of_output_file
import pandas as pd
import glob
import sys


def read_table_rb(file):
	df = pd.read_csv(file, delimiter='\t')
	mn = df['Likelihood'].mean()
	print(mn)
	return(mn)

def read_table_mb(file):
	df = pd.read_csv(file, delimiter='\t', skiprows=1)
	return(df["LnL"].mean())
	

def read_table_rbtl(file):
	df = pd.read_csv(file, delimiter='\t')
	return(df["tree_length"].mean())

def read_table_mbtl(file):
	df = pd.read_csv(file, delimiter='\t', skiprows=1)
	return(df["TL"].mean())	
	

if __name__ == "__main__":
	flist = glob.glob(sys.argv[1])	
	tuple_list = []
	for file in flist:
		print(file)
		mean_val = read_table_rbtl(file)
		fname = file.split('_.')[0]
		tuple_list.append([fname,mean_val])
	df = pd.DataFrame(tuple_list)
	print(df)
	df.to_csv(sys.argv[2], index=False)
