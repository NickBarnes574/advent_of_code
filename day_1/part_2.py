#!/usr/bin/python3

URL = "https://adventofcode.com/2023/day/1/input"
FILEPATH = "day_1/data.txt"

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def main():
    total = 0

    with open(FILEPATH, "r") as file:
        for line in file:
            first, last = find_first_and_last_number(line, number_map)

            # Check for first number in word form
            total += int(first + last)

        print(f"total: {total}")


def find_first_and_last_number(string, number_map):
    first, last = None, None

    # Check each character from the start for the first digit or number word
    for idx in range(len(string)):
        if string[idx].isdigit():
            first = string[idx]
            break
        for word, num in number_map.items():
            if string.startswith(word, idx):
                first = num
                break
        if first is not None:
            break

    # Check each character from the end for the last digit or number word
    for idx in range(len(string)-1, -1, -1):
        if string[idx].isdigit():
            last = string[idx]
            break
        for word, num in number_map.items():
            if string.endswith(word, 0, idx+1):
                last = num
                break
        if last is not None:
            break

    return first or "", last or ""


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
