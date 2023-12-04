#!/usr/bin/env python3
import re


class Card:
    def __init__(self, num, winning, drawn):
        self.num = num
        self.winning = winning
        self.drawn = drawn
        self.winCount = self.countWinningNumbers()
        self.copies = 1
        

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
    
    def getPoints(self): # just for problem 1
        if self.winCount > 0:
            return pow(2, self.winCount - 1)
        else:
            return 0


# filename = "test_input.txt"
# table_length = 6
filename = "input.txt"
table_length = 211
with open(filename, 'r') as file:
    # Parsing the file into Games
    cards = {}
    i = 1
    for line in file:        
        line = line.strip()
        card_and_nums = line.split(":")
        digit = int(re.search(r'\d+', card_and_nums[0]).group())
        if not digit == i:
            print("uh oh, something weird about line ", i)
        nums = card_and_nums[1].split("|")

        winning = [x.group() for x in re.finditer(r'\d+', nums[0])]
        drawn = [x.group() for x in re.finditer(r'\d+', nums[1])]
        
        c = Card(digit, winning, drawn)
        cards[str(digit)] = c
        i+=1

    print(cards)

    scratchCard_count = 0
    debug = True
    for i in range (1, table_length + 1):
        debug = i % 10 == 0;
        card = cards[str(i)]
        scratchCard_count += card.copies
        if debug:
            print("for card", i, "with", card.copies, "copies and", card.winCount, "wins")
        for j in range(card.copies):
            for k in range(i + 1, min(i + card.winCount + 1, table_length + 1)):
                # increment the number of copies
                if debug:
                    print("making a copy of card", k)
                cards[str(k)].copies += 1

    print(scratchCard_count)


    

