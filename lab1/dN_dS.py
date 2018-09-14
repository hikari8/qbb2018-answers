#!/usr/bin/env python3

"""
Usage: ./back_to_nucleotides.py blastn.output mafft.output
"""

import sys
import fasta
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

dna_reader = fasta.FASTAReader(open(sys.argv[1]))
aa_reader = fasta.FASTAReader(open(sys.argv[2]))

amino_dictionary = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    '---':'-', 'GA':'','GG':'','GC':'', 'G':'',
    'A':'','C':'','T':'','GT':'','AG':'','AC':'',
    'AT':'', 'AA':'', 'CT':'', 'CG':'', 'CA':'',
    'CC':'', 'TT':'', 'TC':'', 'TG':'', 'TA':''}

# PART 1: Make new lists of lists of amino acids and codons as strings
# to represent dna and aa alignments from blast and mafft.
# All this is copied over from back_to_nucleotides.

new_dna_entries = []
new_aa_entries =[]

for(dna_id, dna), (aa_id, aa) in zip(dna_reader, aa_reader):
    nuc_seq = []
    aa_seq = []
    j = 0
    for i in range(0, len(aa)):
        a = aa[i]
        aa_seq.append(a)
        nuc = dna[j:(j+3)]
        if a != "-":
            nuc_seq.append(nuc)
            j += 3
        else:
            nuc_seq.append("---")
    new_dna_entries.append(nuc_seq)
    new_aa_entries.append(aa_seq)

# PART 2: Counting dS and dN of each alignment as compared to query.
           
query_aa = new_aa_entries[0]
query_codon = new_dna_entries[0]
# For blast, first entry is actually the query (!)
# print(len(query_aa), len(query_codon))
# to make sure they're identical, length was 6615 for both.

number_of_indel = [0] * len(query_aa)
number_of_mutation = [0] * len(query_aa)
dS_per_entry = [0] * len(query_aa)
dN_per_entry = [0] * len(query_aa)
# Here, I'm making a list of empty values in the number of amino acids and corresponding codons.
# Their output looks like number_of_indel = [0,0,0,0,0...] right now.

for codon_list, aa_list in zip(new_dna_entries[1:], new_aa_entries[1:]):
    for i in range(0, len(codon_list)):
        if query_codon[i] == "---":
            number_of_indel[i] += 1
        elif codon_list[i] != query_codon[i]:
            number_of_mutation[i] += 1
            if aa_list[i] == query_aa[i]:
                dS_per_entry[i] += 1
            else:
                dN_per_entry[i] += 1
# Admittedly, some of the codon in these entries can be shorter than three.
# Currently, all non-accountable strings are streamlined into dN_per_entry.
# Can be polish with additional elif statements.

      
# PART 3: The Z-test, where null hypothesis is D = dN - dS = 0
# Positive selection entails aa change i.e. nonsynonymous mutation:
# a negative number for D = dN - dS.

difference_per_entry = []
for i in range(0, len(dS_per_entry)):
    difference = dN_per_entry[i] - dS_per_entry[i]
    difference_per_entry.append(difference)

ratio_per_entry = []
for i in range(0, len(dS_per_entry)):
    ratio = (dN_per_entry[i])/(dS_per_entry[i] + 1)
    ratio_per_entry.append(ratio)


pos_selection = {}
not_pos_selection = {}
std = np.std(difference_per_entry)

for i, difference in enumerate(difference_per_entry):
    if number_of_mutation[i] == 0:
        continue    
    else:
        std_error = std / sqrt(number_of_mutation[i])
        z = difference/std_error
        # z = (Dc - Dn)/ SE (Dc is difference at each codon, Dn is null hypothesis, so 0)
        if z < -1.645:
            pos_selection[i] = np.log(ratio_per_entry[i])
        else:
            not_pos_selection[i] = np.log(ratio_per_entry[i])
        # p < 0.05, so significant z values are z < -1.645

# PART 4: Plotting dN/dS against codon position.

fig, ax = plt.subplots(figsize=(15, 8))
ax.scatter( pos_selection.keys(), pos_selection.values(), 
            alpha=0.5, s=5, color="red", label="positive selection"
            )
ax.scatter( not_pos_selection.keys(), not_pos_selection.values(), 
            alpha=0.5, s=5, color="green", label="negative or no selection"
            )
ax.set_xlabel("codon position")
ax.set_ylabel("log(dN/dS)")
ax.set_title("dN/dS at each codon")
ax.legend(bbox_to_anchor=(1.01,0.5), loc=2)
plt.tight_layout()
plt.axhline(0, color='black', linewidth=0.5)
fig.savefig("dN_dS.png")
plt.close(fig)