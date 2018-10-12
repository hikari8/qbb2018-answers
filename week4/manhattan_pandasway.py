#!/usr/bin/env python3

"""
./manhattan2.py plink.Pi.assoc
"""

import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

chrom_order = [
    'chrI','chrII','chrIII','chrIV','chrV',
    'chrVI','chrVII','chrVIII','chrIX',
    'chrXI','chrXII','chrXIII','chrXIV','chrXV',
    'chrXVI','23','26']

colors = ['mediumvioletred', 'steelblue']
highlights = ['magenta', 'cyan']

for fname in sys.argv[1:]:
    # Setting the empty plot with title corresponding to treatment.
    fig, ax = plt.subplots(figsize= (20,5))
    treatment = fname.split('.')[1]
    ax.set_title('Manhattan Plot\n'+str(treatment))

    df = pd.read_csv(open(sys.argv[1]), delim_whitespace=True)
    df['P'] = -(np.log10(df['P']))
    
    tick_labels = []
    tick_positions = []
    
    for i, (chrom, group) in enumerate(df.groupby('CHR', sort=False)):
        sig_filter = (group['P'] > 5)
        if sum(sig_filter) > 0:
            group['P'][sig_filter].plot(ax=ax, **{'style':'.','c':highlights[i%2]})
        group['P'][~sig_filter].plot(ax=ax, **{'style':'.','c':colors[i%2]})
        tick_labels.append(chrom)
        tick_positions.append(np.median(group.index.values))
        
    ax.axhline(5, c='k', ls=':', label='Significance cutoff')
    ax.set_xticks(tick_positions)
    ax.set_xticklabels(tick_labels)
    ax.set_xlabel('Genomic Position')
    ax.set_ylabel(r'$\log_{10}(P-value)$')
    plt.savefig(str(treatment) + "_Manhattan")
    plt.close()