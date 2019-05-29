def YACHT(dice):
    if len(set(dice)) == 1:
        return 50
    return 0

def ONES(dice):
    return dice.count(1)

def TWOS(dice):
    return dice.count(2) * 2

def THREES(dice):
    return dice.count(3) * 3

def FOURS(dice):
    return dice.count(4) * 4

def FIVES(dice):
    return dice.count(5) * 5

def SIXES(dice):
    return dice.count(6) * 6

def FULL_HOUSE(dice):
    freqs={}
    for val in dice:
        if val not in freqs:
            freqs[val] = 0
        freqs[val]= freqs[val] +1
    if len(freqs) == 2:
        for freq in freqs.values():
            if(freq ==2 or freq ==3):
                return sum(dice)
    return 0

def FOUR_OF_A_KIND(dice):
    freqs = {}
    for val in dice:
        if val not in freqs:
            freqs[val] = 0
        freqs[val]= freqs[val] +1
    for val, freq in freqs.items():
        if freq >= 4:
            return val*4
    return 0

def LITTLE_STRAIGHT(dice):
    if len(set(dice)) == 5 and 6 not in dice:
        return 30
    return 0

def BIG_STRAIGHT(dice):
    if len(set(dice)) == 5 and 1 not in dice:
        return 30
    return 0

def CHOICE(dice):
    return sum(dice)
    
def score(dice, category):
    return category(dice)