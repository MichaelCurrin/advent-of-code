#!/usr/bin/env python3
"""
https://adventofcode.com/2022/day/1#part2
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
    
    elves.sort()
    
    top_3 = elves[-3:]
    total_top_3 = sum(top_3)
    print(total_top_3)


if __name__ == '__main__':
    main()
