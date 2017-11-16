import pandas as pd
def extract_rows(data, ant_names):
    '''A function to extract relevant data from dataframe'''
    new_data = data.loc[ant_names]
    return(new_data)
    
def get_names(namefile):
   '''Read in a file of names'''
   with open(namefile, 'r') as f:
       ant_names = f.read().splitlines() 
   return(ant_names)
   
if __name__ == '__main__':
	data = pd.read_csv('Data/Ants.csv', index_col=0)
	namefile = 'Data/AntNames.txt'
	ant_names = get_names(namefile)
	new_dataframe = extract_rows(data, ant_names)
	new_dataframe.to_csv('Data/processed_ants.csv')

