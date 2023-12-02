#!/usr/bin/env python3
import re

const_colors = ["red", "green", "blue"]

class Games:
    def __init__(self, games):
        self.games = games
        self.red = 12
        self.green = 13
        self.blue = 14
    
    def which_games_dont_work(self):
        dont_work = []
        for game in self.games:
            for c in const_colors:
                if game.getMaxColor(c) > getattr(self, c):
                    dont_work.append(game.num)
        return dont_work
    
    def which_games_work(self):
        work_ids = []
        ids_for_bad_games = self.which_games_dont_work()
        for game in self.games:
            if game.num not in ids_for_bad_games:
                work_ids.append(game.num)

        return work_ids
    
    def sum_ids_of_working_games(self):
        return sum(self.which_games_work())


class Game:
  # Each cube_subset should be a dict with how many red, green, or blue
    def __init__(self, num, cube_subsets):
        self.num = int(num)
        self.cube_subsets = cube_subsets

    def addSubset(self, subset):
        self.cube_subsets.append(subset)
    
    def printGame(self):
        print("Game", self.num, ":", self.cube_subsets)
        # for color in ["red", "green", "blue"]:
        #     print("max", color, "=", self.getMaxColor(color))

    def getMaxColor(self, color_string):
        just_color = [subset[color_string] for subset in self.cube_subsets if color_string in subset]
        return max(just_color)

def parse_marble_subset(subset):
    subset_maps = []
    for line in subset:
        line.strip()
        colors = line.split(',')
        color_map = {re.search(r'[a-z]+', color).group(): int(re.search(r'\d+', color).group())
                    for color in line.strip().split(',')}
        subset_maps.append(color_map)
    return subset_maps

with open('input1.txt', 'r') as file:
    # Parsing the file into Games
    games = []
    for line in file:        
        line = line.strip()
        game_and_marbles = line.split(":")
        digit = int(re.search(r'\d+', game_and_marbles[0]).group())
        subsets = parse_marble_subset(game_and_marbles[1].split(";"))
        g = Game(digit, subsets)
        games.append(g)
    
    g = Games(games)
    print(g.sum_ids_of_working_games())