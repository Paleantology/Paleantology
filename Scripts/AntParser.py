import requests
import bs4
import sys
import re
import pandas as pd

def url_string(new_file):
	'''Reads a .txt file containing the names of topics within antwiki,
	converts them to urls, and stores them in a dict structure'''
	f = open(new_file,'r')
	line = f.readline()
	d = {}
	for line in f:
		line = line.strip()
		string = 'http://www.antwiki.org/wiki/' + line
		d[line] = string
	return(d)

def query_wiki(dictionary):
	'''Takes a dictionary structure as an argument, queries the urls within the dictionary,
	and stores the results of the queries within the results struct'''
	results = {}
	for name, string in dictionary.items():
	   result = requests.get(str(string))
	   if str(result) != '<Response [404]>':
		  results[name] = result.text
	return(results)
	
def process_html(urls):
	'''Makes an http request to a URL and then uses Soup and regular expressions to get
   specific information from the webpage, such as tribe, family, and genus'''
	taxo = {}
	for name, url in urls.items():
		listo = []
		soup = bs4.BeautifulSoup(url, 'html.parser')
		hierarchy = ['subfamily', 'tribe', 'genus'] 
		for level in hierarchy:
			span = soup.find_all('span', {'class' : level})
			if span is not None:
				listo.append(re.findall ('title="(.*?)"', str(span), re.MULTILINE))
		taxo[name] = listo
	return(taxo)
		
def add_to_frame(dataframe, taxonomy):
	'''Adds the previously-scraped info to existing database, and saves this as a copy 
	for inspection'''
	df = pd.read_csv(dataframe, index_col=0)
	for name, entries in taxonomy.items():
	   while len(entries) < 3:
		  entries.append('NA')
	taxonomy = pd.DataFrame.from_dict(taxonomy, orient='index')
	taxonomy.columns = ['SubFamily', 'Tribe', 'Genus']
	print(taxonomy)
	taxo_df = pd.DataFrame()
#	taxo_df.columns = ['Author','SubFamily', 'Tribe', 'Genus', 'Age','Fossil?', 'Notes']
	taxo_df['Author'] = 'KGB'
	taxo_df['SubFamily'] = taxonomy['SubFamily'].str.get(0)
	taxo_df['Tribe'] = taxonomy['Tribe'].str.get(0)
	taxo_df['Genus'] = taxonomy['Genus'].str.get(0)
	taxo_df['Age'] = 'NA'
	taxo_df['Fossil?'] = 'NA'
	taxo_df['notes'] = ''
	print(taxo_df)
#	updated_df = pd.concat([df, taxo_df])
	return(taxo_df)
if __name__ == "__main__":
	new_file = sys.argv[1]
	dictionary = url_string(new_file)
	urls = query_wiki(dictionary)
	taxonomy = process_html(urls)
	dataframe = sys.argv[2]
	updated_df = add_to_frame(dataframe, taxonomy)
	updated_df.to_csv(sys.argv[3])
