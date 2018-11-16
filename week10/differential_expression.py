#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

list_of_genes = []
list_p_val = []
upregulated_genes = []
upregulated_fold_change = []

for line in open(sys.argv[1]):
    if line.startswith("gene"):
        continue
    else:
        expression = line.split()
        # Not defining the columns made fixing this script a pain in the ass so here it is.
        gene = expression[0]
        cfu = float(expression[1])
        poly = float(expression[2])
        unk = float(expression[3])
        mys = float(expression[5])
        early_average = (cfu + mys)/2
        late_average = (poly + unk)/2
        fold_change = early_average/late_average
        if fold_change >= 2 or fold_change <= 0.5:
            t_stat, p_val = stats.ttest_ind([cfu, mys], [poly, unk])
            if p_val < 0.05:
                list_p_val.append(p_val)
                list_of_genes.append(gene)
                if fold_change <= 0.5:
                    upregulated_genes.append(gene)
                    upregulated_fold_change.append(fold_change)
            
# The code below makes a list of tuples.
# I need fold change to be part of the upregulated_list to determine the most upregulated gene.
differentially_expressed_genes = list(zip(list_of_genes, list_p_val))
upregulated_list = list(zip(upregulated_genes, upregulated_fold_change))
significant_gene = min(upregulated_list, key = lambda t:t[1])

for gene, p_val in differentially_expressed_genes:
    print(gene + "\t" + str(p_val))

# or

# print(significant_gene)