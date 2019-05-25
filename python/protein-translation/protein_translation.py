codonDict = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC':'Serine',
    'UCA':'Serine',
    'UCG':'Serine',
    'UAU':'Tyrosine',
    'UAC':'Tyrosine',
    'UGU':'Cysteine',
    'UGC':'Cysteine',
    'UGG':'Tryptophan',
    'UAA':'STOP',
    'UAG':'STOP',
    'UGA':'STOP',
}

def proteins(strand):
    proteinChain = []
    for i in range(0, len(strand), 3):
        currProtein = codonDict.get(strand[i:i+3])
        if currProtein == 'STOP':
            break
        proteinChain.append(currProtein)
    return proteinChain