def reverse(text):
    result = ""
    for idx in range(len(text)-1, -1, -1):
        result+= text[idx]
    return result