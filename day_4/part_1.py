#!/usr/bin/python3

import os
import re
import traceback

DIRECTORY = "day_4/test_cases"


def main():
    # List all files in the directory
    for filename in os.listdir(DIRECTORY):
        filepath = os.path.join(DIRECTORY, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(filepath):
            print(f"FILE: {filepath}")
            with open(filepath, "r") as file:
                total_points = 0
                for line in file:
                    winning_numbers, player_numbers = get_numbers(line)
                    points = check_numbers(winning_numbers, player_numbers)
                    total_points += points
                print(total_points)


def get_numbers(line: str):
    line = line.strip()
    card_num = re.split(': ', line)  # Remove 'Card #:'

    # separate winning numbers from player numbers
    left_side, right_side = card_num[1].split('|', 1)

    # extract numbers from right and left sides
    left_set = re.findall(r'\d+', left_side)
    right_set = re.findall(r'\d+', right_side)

    # create lists of integers
    winning_numbers = [int(num) for num in left_set]
    player_numbers = [int(num) for num in right_set]

    return winning_numbers, player_numbers


def check_numbers(winning_numbers: list, player_numbers: list):
    points = 0
    winning_set = set(winning_numbers)
    player_set = set(player_numbers)

    common_numbers = winning_set.intersection(player_set)
    for idx, _ in enumerate(common_numbers):
        if idx < 1:
            points += 1
        else:
            points *= 2

    return points


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()  # Print the stack trace
