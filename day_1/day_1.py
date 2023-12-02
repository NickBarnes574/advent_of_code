#!/usr/bin/python3
import os
import sys

URL = "https://adventofcode.com/2023/day/1/input"
FILEPATH = "day_1/data.txt"


def main():
    total = 0

    with open(FILEPATH, "r") as file:
        for line in file:
            first = ""
            last = ""
            for char in line:
                if char.isdigit():
                    if first == "":
                        first = char
                    last = char
            total += int(first + last)

            print(f"total: {total}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
