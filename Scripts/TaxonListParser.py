import pandas as pd
import dendropy
import argparse


def parse_dataframe(df):
    '''Retrieve a taxon list from a dataframe'''
    if df.endswith('.tsv'):
        df = pd.read_csv(df, delimiter="\t")
    elif df.endswith('.csv'):
        df = pd.read_csv(df)
    tax_list= df[['taxon','max']]
    return(tax_list)

def parse_morphology(morph_mat):
    '''Retrieve a taxon list from a Nexus-Formatted morphological matrix'''
    mm = dendropy.StandardCharacterMatrix.get_from_path(morph_mat, schema="nexus", preserve_underscores=True)
    ns = mm.taxon_namespace
    return(ns)

def parse_molecular(mol_mat):
    '''Retrieve a taxon list from a molecular matrix'''
    if mol_mat.endswith('.nex'):
        molm = dendropy.DnaCharacterMatrix.get_from_path(mol_mat, schema="nexus", preserve_underscores=True )
    elif mol_mat.endswith('.fasta' or '.fa'):
        molm = dendropy.DnaCharacterMatrix.get_from_path(mol_mat, schema="fasta")
    else:
        print("Could not tell what file format molecular data are in. Please use suffixes .fa, .fasta, or .nex")
    mns = molm.taxon_namespace
    new_mns = []
    for item in mns:
        new_mns.append(str(item).replace("'", ""))
    df = pd.DataFrame({'taxon':new_mns})
    df = df.drop_duplicates()
    df['age'] = 0
    return(df)

def map_fossils(tnrs, ns):
    '''Decide which taxa in the morphology are fossils, and which are extant'''
    dict_of_nameages = {}
    if tnrs.endswith('.tsv'):
        tnrs = pd.read_csv(tnrs, delimiter="\t")
    elif tnrs.endswith('.csv'):
        tnrs = pd.read_csv(tnrs)
    for item in ns:
        item = str(item).replace("'", "")
        if len(tnrs.loc[tnrs['taxon'] == item]) != 0:
            location = tnrs.loc[tnrs['taxon'] == item]
            dict_of_nameages[str(item)] = location.max_ma.item()
        else:
            dict_of_nameages[item] = 0
    fossil_df = pd.DataFrame.from_dict(dict_of_nameages, orient='index')
    fossil_df = fossil_df.reset_index()
    fossil_df.columns=['taxon','age']
    return(fossil_df)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()

	parser.add_argument("--mol", help="Path to nexus or fasta file containing \
	molecular data. Should end in .nex, .fasta or .fa.")
	parser.add_argument("--morph", help="Path to nexus-formatted file containing \
	morphological data. Should end in .nex.")
	parser.add_argument("--foss", help="Path to TSV or CSV file containing the \
	fossils you'd like to include in the analysis")
	parser.add_argument("--ages", help=" Path to data ages TSV or CSV file containing \
	ages of non-contemporaneous tips, if any exist in your analysis.")
	parser.add_argument("--output", help="Path to where you'd like to write output")
	args = parser.parse_args()
	if args.morph:
		morph_mat = args.morph
	if args.mol:
		mol_mat = args.mol
	if args.foss:
		df = args.foss
	if args.ages:
		morphology_tnrs = args.ages
	if args.output:
		outfile = args.output		
		
	t_l = parse_dataframe(df)
	ns = parse_morphology(morph_mat)
	molm =  parse_molecular(mol_mat)
	foss =  map_fossils(morphology_tnrs, ns)

	big_matr = pd.concat([foss, molm])
	big_matr = big_matr.drop_duplicates()

	big_matr.to_csv(outfile, index=False, sep='\t')


