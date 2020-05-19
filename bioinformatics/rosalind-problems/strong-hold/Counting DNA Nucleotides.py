def countNTFrequency(seq):
    tmpFreqDict = {'A':0,'C':0,'G':0,'T':0}
    for nt in seq:
        tmpFreqDict[nt] +=1 
        
    return tmpFreqDict


DNAString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result  = countNTFrequency(DNAString)

print(' '.join([str(var) for key,var in result.items()]))