#!/usr/bin/env python3
import dendropy
import argparse
import sys

def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Load & prune trees.')
    parser.add_argument('File', metavar='FILE', help='File containing trees')
    parser.add_argument('Burnin', type=int, help='How many trees to discard as burnin')
    parser.add_argument('Outf', help='Output file name')
    return parser.parse_args(args)
    
def main():
    retain_list, tl = get_names(file)
    newtl = tree_ops(tl, burnin, retain_list)
    print("Writing out pruned trees")
    newtl.write_to_path(outf, schema='nexus')

def get_names(file):
    '''Opens trees using Dendropy, and determines which taxa are extinct'''
    print("Reading in trees")
    tl = dendropy.TreeList.get_from_path(file, schema="nexus", preserve_underscores=True)
    print(tl)
    retain_list = []
    print("Getting list of taxa to keep")
    for name in tl.taxon_namespace:
        if str(name).endswith('X\'', 2) is False:
            retain_list.append(name)
    print("To retain:", retain_list)
    return(retain_list, tl)  
          
def tree_ops(tl, burnin, retain_list):
    '''Extract subtrees of extant taxa'''
    print("Disgaurding burnin")
    newtl = tl[burnin:]
    newTrees = dendropy.TreeList()
    print("Extracting good taxa")
    for t in newtl:
        t = t.extract_tree_with_taxa(retain_list)
        newTrees.append(t)
    return(newTrees)

if __name__ == "__main__":
    args = parse_args()
    file = args.File
    burnin = args.Burnin
    outf = args.Outf
    
    main()
