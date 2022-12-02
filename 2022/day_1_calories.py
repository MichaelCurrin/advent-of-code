#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/1
"""

def main():
    with open('day_1_input.txt') as f_in:
        rows = f_in.read().splitlines()
    
    elves = []
    calories = 0

    for row in rows:
        if not row:
            elves.append(calories)
            calories = 0
        else:
            calories += int(row)
    
    highest_calories = max(elves)

    print(highest_calories)


if __name__ == '__main__':
    main()
