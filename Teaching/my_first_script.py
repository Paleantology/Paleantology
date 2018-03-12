import pandas as pd


def extract_ants(ant_data, query_list):	
	'''Function to get ants out of dataframe'''
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
	return(ant_names)

def write_out():
	''' '''

<<<<<<< HEAD
if __name__ == "__main__":
	ant_data = pd.read_csv("Data/Ants.csv", index_col=0)
	namefile = "Data/AntNames.txt"
	query_list = get_names(namefile)
	extracted_ants = extract_ants(ant_data, query_list)
	print(extracted_ants)
=======
(^write into file NOT Data, and leave comment^)

if __name__ == "__main__":
	ant_data = pd.read_csv("Data/Ants.csv", index_col=0)
	namefile = "Data/AntNames.txt" 
	query_list = get_names(namefile)
	extracted_ants = extract_ants(ant_data, query_list)		
	print(extracted_ants)






>>>>>>> 9b3c0e14c2d7d2ef4140d75f7f2d5abecc8fbe34
>>>>>>> 90b8100f154d483ebf5c7394f8a7f2e056484c5b
