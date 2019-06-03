import re

class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not re.search(r'^\(;(.*)\)$', input_string):
        raise ValueError("String must contain tree with 1+ nodes")
    tree = SgfTree()
    remainderString = input_string[2:len(input_string)-1]
    currKey = ''
    currVal = []
    generatingValue = False
    for i in range(len(remainderString)):
        currChar = remainderString[i]
        if generatingValue == False and currChar != '[' and currChar != ';':
            currKey+= currChar
        elif generatingValue == False and currChar == '[':
            if not re.search((r'^[A-Z]+$'), currKey):
                raise ValueError("Key properties must be string with all capital letters")
            generatingValue = True
        elif generatingValue == True and currChar != ']':
            currVal += currChar
        elif generatingValue == True and currChar == ']':
            tree.properties[currKey] = currVal
            generatingValue = False
            currKey = ''
            currVal = []
        elif currChar == ';':
            tree.children = parse(f'({remainderString[i:]})')
    if len(currKey) > 0 and len(currVal) == 0:
        raise ValueError("Keys must have corresponding value")
    return tree