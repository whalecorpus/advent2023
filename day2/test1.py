#!/usr/bin/env python3
import re
# from .day2 import problem1 as p1

test_cases = [
    (["1 red, 2 green, 6 blue"], {'red': 1, 'green': 2, 'blue': 6}),
    (["2 green"], {'green': 2}),
    (["1 blue, 2 green"], {'blue': 1, 'green': 2}),
    (["3 green, 4 blue, 1 red"], {'green': 3, 'blue': 4, 'red': 1}),
    (["1 green, 1 blue"], {'green': 1, 'blue': 1}),
    (["8 green, 6 blue, 20 red"], {'green': 8, 'blue': 6, 'red': 20}),
    (["5 blue, 4 red, 13 green"], {'blue': 5, 'red': 4, 'green': 13}),
    (["5 green, 1 red"], {'green': 5, 'red': 1}),
    (["1 green, 3 red, 6 blue"], {'green': 1, 'red': 3, 'blue': 6}),
    (["3 green, 6 red"], {'green': 3, 'red': 6}),
    (["3 green, 15 blue, 14 red"], {'green': 3, 'blue': 15, 'red': 14}),
    (["6 red, 1 blue, 3 green"], {'red': 6, 'blue': 1, 'green': 3}),
    (["2 blue, 1 red, 2 green"], {'blue': 2, 'red': 1, 'green': 2}),
    (["3 blue, 4 red"], {'blue': 3, 'red': 4})
]

def parse_marble_subset(subset):
    subset_maps = []
    for line in subset:
        line.strip()
        colors = line.split(',')
        color_map = {re.search(r'[a-z]+', color).group(): int(re.search(r'\d+', color).group())
                    for color in line.strip().split(',')}
        subset_maps.append(color_map)

# Function to run the tests
def run_tests():
    for i, (input_value, expected_output) in enumerate(test_cases):
        result = parse_marble_subset(input_value)[0]
        assert result == expected_output, f"Test case {i+1} failed: expected {expected_output}, got {result}"
    print("All tests passed!")

run_tests()