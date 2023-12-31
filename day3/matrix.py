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
        if n.x > 0 and self.isSymbol(line[n.x-1]):
            self.addSymbolNeighbor(n.x-1, n.y, n)
            return True
        if n.x2 < len(line) - 1 and self.isSymbol(line[n.x2 + 1]):
            self.addSymbolNeighbor(n.x2 + 1, n.y, n)
            return True


        # in the line above, at startx - 1 through endX + 1
        if n.y > 0:
            line = self.matrix[n.y - 1]
            start = max(0, n.x - 1)
            end = min(n.x2+2, len(line))
            if debug:
                print(n.d, "above: scanning from ", start, "to", end, "which is", line[start:end])
            x = start
            for c in line[start:end]:
                if self.isSymbol(c):
                    self.addSymbolNeighbor(x, n.y - 1, n)
                    return True
                x += 1

        # in the line below, at startx - 1 through endX + 1
        if n.y <= len(m.matrix) - 2:
            line = self.matrix[n.y + 1]
            start = max(0, n.x - 1)
            end = min(n.x2+2, len(line))
            if debug:
                print(n.d, "below: scanning from ", start, "to", end, "which is", line[start:end])
            x = start
            for c in line[start:end]:
                if self.isSymbol(c):
                    self.addSymbolNeighbor(x, n.y + 1, n)
                    return True
                x += 1

        return False
    
    def isSymbol(self, ch):
        symbols = re.findall(r"[!@#$%^&*()\-_=+\[\]{};:'\",<>\/?|\\~]", ch)
        return len(symbols) > 0
    
    def addSymbolNeighbor(self, x, y, n):
        for sy in self.symbols:
            if x == sy.x and y == sy.y:
                sy.addNeighbor(n)

    def printSymbolNeighbors(self):
        for s in self.symbols:
            print(s.d, "symbol at ", s.x, ",", s.y, ":")
            for n in s.neighbors:
                print(n.d, ",")

    def findGears(self):
        debug = False
        sum = 0
        gears = {}
        for s in self.symbols:
            if debug:
                print(s.d, s.neighbors, len(s.neighbors))
            if len(s.neighbors) == 2:
                gear_key = s.d+ "(" + str(s.x) + "," + str(s.y) +")"
                gears[gear_key] = s.neighbors[0].d * s.neighbors[1].d
                gear_ratio = s.neighbors[0].d * s.neighbors[1].d
                if debug:
                    print("adding", gear_ratio, "to gear ratio sum")
                sum += gear_ratio

        return gears, sum
                

    
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

class Matrix_Symbol:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.neighbors = []

    def addNeighbor(self, n):
        # add number as neighbor
        self.neighbors.append(n)

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
        symbols = re.finditer(r"[!@#$%^&*()\-_=+\[\]{};:'\",<>\/?|\\~]", line)
        for match in symbols:
            span = match.span()
            m.addSym(Matrix_Symbol(span[0], y, match.group()))

        y += 1 # going down the matrix
    
    sum_q1 = m.allPartNumbers()
    gears, summedGearRatio = m.findGears()
    print("Gears:", gears)
    print("sum gear ratio: ", summedGearRatio)