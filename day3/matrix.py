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
        sides_debug = False
        # on the same line, at startx - 1 and endX + 1
        line = self.matrix[n.y]
        if debug:
            print("checking", n.d, "at x (",n.x,") through x2 + 1 (", n.x2 + 1,") inclusive")
        if sides_debug:
            print(n.d, "sides: checking ", n.x-1, "and", n.x2 + 1, "; which are")
        if n.x > 0 and self.isSymbol(line[n.x-1]):
            if sides_debug:
                print(line[n.x-1])
            return True
        elif n.x == 0 and sides_debug:
            print("blank")
        else:
            if sides_debug:
                print(line[n.x-1])
        if sides_debug:
            print("and")
        if n.x2 < len(line) - 1 and self.isSymbol(line[n.x2 + 1]):
            if sides_debug: 
                print(line[n.x2 + 1])
            return True
        elif n.x2 >= len(line) - 1 and sides_debug:
            print("blank")
        else:
            if sides_debug:
                print(line[n.x2 + 1])


        # in the line above, at startx - 1 through endX + 1
        if n.y > 0:
            line = self.matrix[n.y - 1]
            start = max(0, n.x - 1)
            end = min(n.x2+2, len(line))
            if debug:
                print(n.d, "above: scanning from ", start, "to", end, "which is", line[start:end])
            for c in line[start:end]:
                if self.isSymbol(c):
                    return True

        # in the line below, at startx - 1 through endX + 1
        if n.y <= len(m.matrix) - 2:
            line = self.matrix[n.y + 1]
            start = max(0, n.x - 1)
            end = min(n.x2+2, len(line))
            if debug:
                print(n.d, "below: scanning from ", start, "to", end, "which is", line[start:end])
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

        # print ("all friendly numbers:", friendly_nums)
        # print ("all unfriendly numbers:", unfriendly_nums)
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

# filename = "test_input.txt"
filename = "input.txt"
with open(filename, 'r') as file:
    # Parsing the file into Numbers
    games = []
    sum_of_power = 0
    y = 0
    m = Matrix([],[])
    for line in file:
        real_line = line.rstrip('\n')
        m.addRow(list(real_line))
        nums = re.finditer(r'\d+', real_line)
        for match in nums:
            span = match.span()
            m.addNum(Matrix_Number(span[0], y, span[1]-1, match.group()))
        # if you wanted a list of all the symbols:
        # symbols = re.finditer(r"[!@#$%^&*()\-_=+\[\]{};:'\",<>\/?|\\~]", line)
        # for match in symbols:
        #     span = match.span()
        #     m.addSym(Matrix_Symbol(span[0], y))

        y += 1 # going down the matrix
    
    sum_q1 = m.sumPartNumbers()
    print(sum_q1)