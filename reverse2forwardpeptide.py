import re
import os
import tkinter as tk
from tkinter import filedialog

def seqTranslate(init_seq):
    Fliptable = {
        'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
        } # genuinely just a table for flipping bases around
    init_seq = init_seq.rstrip('\r\n') # strip parts that would mess with formatting
    init_seq = init_seq[::-1] # flip sequence to be read in correct direction
    forSeq = ""
    if len(init_seq) % 3 != 0: # check for bases that aren't mults of 3
        print(line[0] + ", DNA:" + line[3] + ", Bases are not in triplet, culling last bases first...")
        init_seq = init_seq[:-(len(init_seq) % 3)]
        for i in range(0, len(init_seq), 1): # establish range
            base = init_seq[i:i + 1] # go through each base by 1
            forSeq += Fliptable[base] # flip base letter
    elif len(init_seq) % 3 == 0:
        for i in range(0, len(init_seq), 1): # establish range
            base = init_seq[i:i + 1] # go through each base by 1
            forSeq += Fliptable[base] # flip base letter
    return forSeq

def translate(forSeq, outfile): 
    AAtable = {        
        **dict.fromkeys(['ATA', 'ATC', 'ATT'], 'I'), 
        **dict.fromkeys(['ACA', 'ACC', 'ACG', 'ACT'], 'T'), 
        **dict.fromkeys(['AAC', 'AAT'], 'N'), 
        **dict.fromkeys(['AAA', 'AAG'], 'K'), 
        **dict.fromkeys(['AGC', 'AGT', 'TCA', 'TCC', 'TCG', 'TCT'], 'S'), 
        **dict.fromkeys(['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGT'], 'R'), 
        **dict.fromkeys(['CTA', 'CTC', 'CTG', 'CTT', 'TTA', 'TTG'], 'L'),             
        **dict.fromkeys(['CCA', 'CCC', 'CCG', 'CCT'], 'P'), 
        **dict.fromkeys(['CAC', 'CAT'], 'H'), 
        **dict.fromkeys(['CAA', 'CAG', 'TAG'], 'Q'), # In this case, amber codon is set to glutamine
        **dict.fromkeys(['GTA', 'GTC', 'GTG', 'GTT'], 'V'), 
        **dict.fromkeys(['GCA', 'GCC', 'GCG', 'GCT'], 'A'), 
        **dict.fromkeys(['GAC', 'GAT'], 'D'), 
        **dict.fromkeys(['GAA', 'GAG'], 'E'), 
        **dict.fromkeys(['GGA', 'GGC', 'GGG', 'GGT'], 'G'), 
        **dict.fromkeys(['TTC', 'TTT'], 'F'), 
        **dict.fromkeys(['TAC', 'TAT'], 'Y'), 
        **dict.fromkeys(['TAA', 'TGA'], '*'), 
        **dict.fromkeys(['TGC', 'TGT'], 'C'), 
        'TGG':'W', 'ATG':'M', 
    } # this is purely a translation table from DNA to Amino Acid       
    protein = ""
    if len(forSeq) % 3 == 0: # one last check in case
        for i in range(0, len(forSeq), 3):
            codon = forSeq[i:i + 3]
            protein += AAtable[codon] # check table and TL to AA
    #forSeq = forSeq[::-1] # redundant code
    #protein = protein[::-1] # redundant code, placing sequence and peptide in correct orientation
    finalSeq_comp = ''.join([protein, "    ", line[2], "  ", forSeq, "\n"]) # put it all together, that's it
    outfile.write(finalSeq_comp) # write it

# tkinter window opening to request file to process
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
with open(file_path, 'r') as infile: #looks for the file
    input_cwd = os.path.dirname(file_path)
    with open(input_cwd + '\\' + 'r2fout_' + (os.path.basename(file_path)), 'w') as outfile: # write to second file
        ori_string = infile.readlines()
        for line in ori_string: # now for writing the actual file
            line = line.replace('  ', '    ') # evens out the spacing for splitting purposes
            line = re.split('    ', line) # splits line
            init_seq = line[3] # pick line 3, this should be the DNA sequence, because for whatever reason DNA is that line
            translate(seqTranslate(init_seq), outfile)
