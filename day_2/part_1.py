#!/usr/bin/python3

import re

FILEPATH = "day_2/data.txt"


def main():
    sum_id = 0

    with open(FILEPATH, "r") as file:
        for line in file:
            game_id, sets = extract_game_data(line)
            game_id, result = process_game_data(game_id, sets)
            print(f"game_id: {game_id}")
            print(f"result: {result}")

            if (result == True):
                sum_id += int(game_id)

        print(f"sum_id: {sum_id}")


def extract_game_data(string):
    """Extracts game ID and sets from the given string."""
    game = re.split(': ', string)
    game_id = game[0].split('Game ')[1]
    sets = game[1].split(';')
    return game_id, sets


def process_game_data(game_id, sets):
    """Processes game data to determine the result based on cubes in sets."""
    for subset in sets:
        cubes = subset.split(',')
        result = analyze_cubes(cubes)
        if not result:
            return game_id, result

    return game_id, True


def analyze_cubes(cubes: list):
    for cube in cubes:
        cube = cube.strip()
        amount_color = re.split(' ', cube)
        if amount_color[1] == 'red':
            if int(amount_color[0]) > 12:
                return False
        if amount_color[1] == 'green':
            if int(amount_color[0]) > 13:
                return False
        if amount_color[1] == 'blue':
            if int(amount_color[0]) > 14:
                return False
    return True


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
