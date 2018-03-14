import pandas as pd
import dendropy
import argparse

def parse_dataframe(df):
    '''Retrieve a taxon list from a dataframe'''
    if df.endswith('.tsv'):
        df = pd.read_csv(df, delimiter="\t")
    elif df.endswith('.csv'):
        df = pd.read_csv(df)
    tax_list= df[['taxon','age']]
    foss_tax = tax_list[tax_list.age != 0.0 ]
    return(foss_tax)

def map_fossils(tnrs, foss_tax):
    '''Decide which taxa in the morphology are fossils, and which are extant'''
    dict_of_nameages = {}
    if tnrs.endswith('.tsv'):
        tnrs = pd.read_csv(tnrs, delimiter="\t")
    elif tnrs.endswith('.csv'):
        tnrs = pd.read_csv(tnrs)
    for item in foss_tax.taxon:
        if len(tnrs.loc[tnrs['taxon'] == item]) != 0:
            location = tnrs.loc[tnrs['taxon'] == item]
            dict_of_nameages[str(item)] = [location.max_ma.item(), location.min_ma.item()]
        else:
            dict_of_nameages[item] = 0
    fossil_df = pd.DataFrame.from_dict(dict_of_nameages, orient='index')
    fossil_df = fossil_df.reset_index()
    fossil_df.columns=['taxon','max', 'min']
    return(fossil_df)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("--set", help="Path to the taxon TSV or CSV file containing all\
	fossils and all tips on the tree.")
	parser.add_argument("--ages", help=" Path to data ages TSV or CSV file containing \
	ages of non-contemporaneous tips, if any exist in your analysis.")
	parser.add_argument("--output", help="Path to where you'd like to write output")
	args = parser.parse_args()
	if args.set:
		df = args.set
	if args.ages:
		tnrs = args.ages
	if args.output:
		outfile = args.output		
		
	foss_tax = parse_dataframe(df)
	
	matrix = map_fossils(tnrs, foss_tax)
	matrix.to_csv(outfile, index=False, sep='\t')



#df = "../Data/combined/Data/taxa.tsv"
#morphology_tnrs = "../Data/Morph/FossilTNRS.csv"



