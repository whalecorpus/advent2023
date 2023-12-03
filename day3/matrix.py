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

    # returns true if the given matrix number is adjacent to a symbol
    # Given a number, you have to search
    
    def hasSymbolNeighbors(self, n):
        debug = False
        if n.d == 664:
            debug = True
        # on the same line, at startx - 1 and endX + 1
        line = self.matrix[n.y]
        if n.x > 0 and self.isSymbol(line[n.x-1]):
            return True
        if n.x < len(line) - 1 and self.isSymbol(line[n.x2]):
            return True

        # in the line above, at startx - 1 through endX + 1
        if n.y > 0:
            line = self.matrix[n.y - 1]
            start = max(0, n.x - 1)
            end = max(n.x2, len(line) - 1)
            if debug:
                print("above: scanning from ", start, "to", end, "on line", line, "; which is", line[start:end])
            for c in line[start:end]:
                if self.isSymbol(c):
                    return True

        # in the line below, at startx - 1 through endX + 1
        if n.y <= len(line) - 2:
            line = self.matrix[n.y + 1]
            start = max(0, n.x - 1)
            end = max(n.x2, len(line) - 1)
            if debug:
                print("below: scanning from ", start, "to", end, "on line", line, "; which is", line[start:end])
            for c in line[start:end]:
                if self.isSymbol(c):
                    return True

        return False
    
    def isSymbol(self, ch):
        symbols = re.findall(r"[!@#$%^&*()\-_=+\[\]{};:'\",<>\/?|\\~]", ch)
        return len(symbols) > 0
    
    def allPartNumbers(self):
        friendly_nums = []
        unfriendly_nums = []
        for n in self.numbers:
            if self.hasSymbolNeighbors(n):
                friendly_nums.append(n.d)
            else:
                unfriendly_nums.append(n.d)

        print ("all friendly numbers:", friendly_nums)
        print ("all unfriendly numbers:", unfriendly_nums)
        return friendly_nums

    def sumPartNumbers(self):
        all = self.allPartNumbers()
        sum = 0
        for n in all:
            sum += n
        return sum




class Matrix_Number:
    def __init__(self, startX, startY, endX, number):
        self.x = startX
        self.x2 = endX
        self.span = span
        self.y = startY
        self.d = int(number)

        # calculate how many digits in number

class Matrix_Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y

filename = "test_input.txt"
# filename = "input.txt"
with open(filename, 'r') as file:
    # Parsing the file into Numbers
    games = []
    sum_of_power = 0
    y = 0
    m = Matrix([],[])
    for line in file:
        line.strip()
        m.addRow(list(line))
        nums = re.finditer(r'\d+', line)
        for match in nums:
            span = match.span()
            m.addNum(Matrix_Number(span[0], y, span[1], match.group()))
        # if you wanted a list of all the symbols:
        # symbols = re.finditer(r"[!@#$%^&*()\-_=+\[\]{};:'\",<>\/?|\\~]", line)
        # for match in symbols:
        #     span = match.span()
        #     m.addSym(Matrix_Symbol(span[0], y))

        y += 1 # going down the matrix
    
    sum_q1 = m.sumPartNumbers()
    print(sum_q1)
