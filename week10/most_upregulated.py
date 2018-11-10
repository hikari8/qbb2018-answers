#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

upregulated_genes = []
upregulated_fold_change = []

for line in open(sys.argv[1]):
    if line.startswith("gene"):
        continue
    else:
        expression = line.split()
        early_average = (float(expression[1]) + float(expression[5]))/2
        late_average = (float(expression[2]) + float(expression[3]))/2
        fold_change = early_average/late_average
        if fold_change <= 0.5:
            t_stat, p_val = stats.ttest_ind([float(expression[1]), float(expression[5])], [float(expression[2]), float(expression[3])])
            if p_val < 0.05:
                upregulated_genes.append(expression[0])
                upregulated_fold_change.append(fold_change)
            
upregulated_list = list(zip(upregulated_genes, upregulated_fold_change))
significant_gene = min(upregulated_list, key = lambda t:t[1])
print(significant_gene)