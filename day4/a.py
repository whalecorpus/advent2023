#!/usr/bin/env python3
import re


class Card:
    def __init__(self, num, winning, drawn):
        self.num = num
        self.winning = winning
        self.drawn = drawn
        self.winCount = self.countWinningNumbers()
        self.points = self.getPoints()

    def printNice(self):
        # print("for card", self.num, ":")
        # print("winning:", self.winning)
        # print("drawn:", self.drawn)
        print("for card", self.num, ":", "winCount", self.winCount, "points", self.points)
    
    def countWinningNumbers(self):
        winCount = 0
        for d in self.drawn:
            if d in self.winning:
                winCount += 1
        self.winCount = winCount
        return winCount
    
    def getPoints(self):
        if self.winCount > 0:
            return pow(2, self.winCount - 1)
        else:
            return 0


# filename = "test_input.txt"
filename = "input.txt"
with open(filename, 'r') as file:
    # Parsing the file into Games
    cards = []
    sum_of_power = 0
    for line in file:        
        line = line.strip()
        card_and_nums = line.split(":")
        digit = int(re.search(r'\d+', card_and_nums[0]).group())
        nums = card_and_nums[1].split("|")

        winning = [x.group() for x in re.finditer(r'\d+', nums[0])]
        drawn = [x.group() for x in re.finditer(r'\d+', nums[1])]
        
        c = Card(digit, winning, drawn)
        cards.append(c)

    sum = 0
    for c in cards:
        c.printNice()
        sum += c.points
    print(sum)
    

