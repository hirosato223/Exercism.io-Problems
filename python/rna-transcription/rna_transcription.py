dnaToRnaDict = {
    'G': 'C', 
    'C': 'G', 
    'T': 'A',
    'A':'U'
}

def to_rna(dna_strand):
    rna = ''
    for val in dna_strand:
        rna+= dnaToRnaDict[val]
    return rna