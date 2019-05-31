import re

def is_valid(isbn):
    if len(isbn) == 0:
        return False
    containsTrailingX = True if isbn[-1] == 'X' else False
    cleanIsbn = re.sub(r'\D', "", isbn)
    if (len(cleanIsbn) == 9 and containsTrailingX == True) or (len(cleanIsbn) == 10 and containsTrailingX ==False):
        sum = 0
        for i in range(10, 1, -1):
            sum+= i * int(cleanIsbn[10-i])
        sum += 10 if containsTrailingX else int(cleanIsbn[9])
        return sum % 11 == 0
    return False