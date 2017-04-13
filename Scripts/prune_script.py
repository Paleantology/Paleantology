#!/usr/bin/env python3
import dendropy
import argparse

def define_parser():
	parser = argparse.ArgumentParser(description='Load & prune trees.')
	parser.add_argument('File', metavar='FILE', help='File containing trees')
	parser.add_argument('Burnin', type=int help='How many trees to discard as burnin')
	args = parser.parse_args()

def get_names():
	tl = dendropy.Tree.get_from_path(file, schema="nexus", preserve_underscores=True)
	retain_list = []
	for name in tl.taxon_namespace:
    	if str(name).endswith('X\'', 2) == False:
        	retain_list.append(name)
    return(retain_list)    	

def tree_ops(burnin, retain_list)
	newtl = tl[burnin:]
	for t in newtl:
		t = t.extract_tree_with_taxa(retain_list)
	return(newtl)
	
if __name__ == "__main__":
	define_parse()
	retain_list = get_names
	newtl = tree_ops(burnin, retain_list)
	newtl.write_to_path('newt', schema='nexus')