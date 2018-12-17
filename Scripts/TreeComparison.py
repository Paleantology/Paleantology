#!/anaconda3/bin/python3

import dendropy
from dendropy.calculate import treecompare
import itertools
import glob
import sys
import pandas as pd

def read_trees(est_trees, comp_tree):
	estimated_trees = []
	list = glob.glob(est_trees)
	for file in list:
		estimated_trees.append(dendropy.Tree.get_from_path(file, schema="nexus", preserve_underscores=True, rooting='force-unrooted'))
	print(estimated_trees[0])
	comparison_tree = dendropy.Tree.get_from_path(comp_tree, schema="newick", preserve_underscores=True, rooting='force-unrooted', taxon_namespace= estimated_trees[0].taxon_namespace)
	return(estimated_trees, comparison_tree)


def perform_comparsions(treelist, comp_tree):
	df = pd.DataFrame(columns=['RF'])
	total_diffs = 2*len(comp_tree.nodes())

	for et in treelist:
        	et.migrate_taxon_namespace(comp_tree.taxon_namespace)
        	df.loc[len(df)] = treecompare.symmetric_difference(et,comp_tree)/total_diffs
        	print(treecompare.symmetric_difference(et,comp_tree)/total_diffs)
	return(df)
    
if __name__ == "__main__":
	est_trees = sys.argv[1]
	comp_tree = sys.argv[3]
	treelist, comparison_tree = read_trees(est_trees, comp_tree)
	output = perform_comparsions(treelist, comparison_tree)
	output.to_csv(sys.argv[2])


