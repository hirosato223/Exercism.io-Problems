colorCodeDict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def value(colors):
    colorStr = ''
    for color in colors:
        colorStr += str(colorCodeDict[color])
    return int(colorStr)