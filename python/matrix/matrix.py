import re 

class Matrix(object):
    def __init__(self, matrix_string):
        self.rows = self.parseRows(matrix_string)
        self.cols = self.parseCols()

    def parseRows(self, matrixString):
        # Map implementation:
        # return [list(map(int, re.split(r"\s", row))) for row in re.split(r"\n", matrixString)]
        
        # Nested list comprehension:
        return [[int(val) for val in re.split(r"\s", row)] for row in re.split(r"\n", matrixString)]
        
    def parseCols(self):
        return [[self.rows[rowIdx][colIdx] for rowIdx in range(len(self.rows))] for colIdx in range(len(self.rows[0]))]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.cols[index - 1]