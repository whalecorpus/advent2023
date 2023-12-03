#!/usr/bin/env python3
import re

class Matrix:
    def __init__(self, numbers, symbols):
        self.matrix = []
        self.numbers = numbers
        self.symbols = symbols
    
    def addRow(self, list_of_chars_in_row):
        self.matrix.append(list_of_chars_in_row)

    def addNum(self, number):
        self.numbers.append(number)

    def addSym(self, number):
        self.symbols.append(number)    

    def printNumbers(self):
        for n in self.numbers:
            print(n.d, "at (", n.x, ",", n.y, ") for", n.x2-n.x)

    def printSymbols(self):
        for s in self.symbols:
            print("symbol at (", s.x, ",", s.y, ")")

class Matrix_Number:
    def __init__(self, startX, startY, endX, number):
        self.x = startX
        self.x2 = endX
        self.span = span
        self.y = startY
        self.d = number

        # calculate how many digits in number

class Matrix_Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y


with open('test_input.txt', 'r') as file:
    # Parsing the file into Numbers
    games = []
    sum_of_power = 0
    y = 0
    m = Matrix([],[])
    for line in file:
        m.addRow(list(line))
        nums = re.finditer(r'\d+', line)
        for match in nums:
            span = match.span()
            m.addNum(Matrix_Number(span[0], y, span[1], match.group()))
        symbols = re.finditer(r"[!@#$%^&*()\-_=+\[\]{};:'\",<>\/?|\\~]", line)
        # for match in symbols:
        #     span = match.span()
        #     m.addSym(Matrix_Symbol(span[0], y))

        y += 1 # going down the matrix
    
    m.printNumbers()
    m.printSymbols()
