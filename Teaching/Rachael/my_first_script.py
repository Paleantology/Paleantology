import pandas as pd 


def extract_ants(ant_data, query_list):
	'''Function to get ants out of data frame'''
	new_data = ant_data.loc[query_list] 
	return(new_data)

def get_names(namefile):
	'''Read in a file of names'''
	with open(namefile, 'r') as f:
   		ant_names = f.read().splitlines() 
	return(ant_names) 

if __name__ == "__main__":
	ant_data = pd.read_csv("Data/Ants.csv" , index_col=0)
	namefile = "Data/AntNames.txt"
	query_list = get_names(namefile)
	extracted_ants = extract_ants(ant_data, query_list)
	print(extracted_ants)