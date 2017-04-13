import pandas as pd
import sys as sys
import os as os

def extract_rows(data, ant_names):
    '''A function to extract relevant data from dataframe'''
    new_data = data.loc[ant_names]
    return(new_data)

def get_names(namefile):
   '''Read in a file of names'''
   with open(namefile, 'r') as f:
       ant_names = f.read().splitlines() 
   return(ant_names)

def check_dir(path):
	check=path.split('/')[0]
	os.listdir(check)
	if 'output' in os.listdir(check):
		return
	else:
		os.mkdir('%s/output' % check)

if __name__ == '__main__':
	data = pd.read_csv(sys.argv[1], index_col=0)
	''' ../../Data/Ants.csv '''
	namefile = sys.argv[2] 
	''' '../../Data/AntTestData.txt' '''
	outputPath = check_dir(sys.argv[3])
	ant_names = get_names(namefile)
	new_dataframe = extract_rows(data, ant_names)
	new_dataframe.to_csv(sys.argv[3]) 
	''' ../../Data/processed_ants.csv '''
