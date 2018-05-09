
# coding: utf-8

# In[31]:

import dendropy
from dendropy.calculate import treecompare
import itertools


# In[163]:

estimated_trees = []
mcc = dendropy.Tree.get_from_path("../Data/Morph/output/binary/combined/ants6.mcc.tre", schema="nexus", preserve_underscores=True, rooting='force-unrooted')
map = dendropy.Tree.get_from_path("../Data/Morph/output/binary/combined/ants6.map.tre", schema="nexus", taxon_namespace= mcc.taxon_namespace, preserve_underscores=True, rooting='force-unrooted')
con = dendropy.Tree.get_from_path("../Data/Morph/output/binary/combined/ants6.maj.tre", schema="nexus", taxon_namespace= mcc.taxon_namespace, preserve_underscores=True, rooting='force-unrooted')
allc = dendropy.Tree.get_from_path("../Data/Morph/output/binary/combined/ants6.allcompat.tre", schema="nexus", taxon_namespace= mcc.taxon_namespace, preserve_underscores=True, rooting='force-unrooted')

estimated_trees.append(mcc)
estimated_trees.append(map)
estimated_trees.append(con)
estimated_trees.append(allc)



# In[164]:

barden_tree = dendropy.Tree.get_from_path("../Data/Morph/Data/Barden.nex", schema="nexus", preserve_underscores=True, rooting='force-unrooted')


# In[165]:

include_list = []
blabels = barden_tree.taxon_namespace.labels()
mcclabels = estimated_trees[1].taxon_namespace.labels()
for label in mcclabels:
    if label in blabels:
        include_list.append(label)
print(len(include_list))
        
for et in estimated_trees:
    et.retain_taxa_with_labels(include_list)
    print(len(et.leaf_edges()))


# In[167]:

total_diffs = 2*len(barden_tree.nodes())

for et in estimated_trees:
    for i in range(0,3):
        et.migrate_taxon_namespace(barden_tree.taxon_namespace)
        et.write_to_path("test{}.tre".format(i), schema="nexus")
        print((treecompare.symmetric_difference(et,barden_tree))/total_diffs)
    


# In[ ]:



