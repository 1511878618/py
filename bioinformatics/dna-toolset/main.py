from dnatoolkit import * 
import random 
import os 

test = read_fasta('bioinformatics/dna-toolset/test.txt')
matrix = profileMatrix(test)
print(Consensus(matrix))