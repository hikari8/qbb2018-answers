#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

list_of_genes = []
list_p_val = []

for line in open(sys.argv[1]):
    if line.startswith("gene"):
        continue
    else:
        expression = line.split()
        early_average = (float(expression[1]) + float(expression[5]))/2
        late_average = (float(expression[2]) + float(expression[3]))/2
        if early_average/late_average >= 2 or early_average/late_average <= 0.5:
            t_stat, p_val = stats.ttest_ind([float(expression[1]), float(expression[5])], [float(expression[2]), float(expression[3])])
            if p_val < 0.05:
                list_p_val.append(p_val)
                list_of_genes.append(expression[0])
            
final_list = list(zip(list_of_genes, list_p_val))

for gene, pval in final_list:
    print(gene + "\t" + str(pval))