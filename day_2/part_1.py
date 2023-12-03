#!/usr/bin/python3

import re

FILEPATH = "day_2/data.txt"


def main():
    sum_id = 0

    with open(FILEPATH, "r") as file:
        for line in file:
            game_id, result = parse_line(line)
            print(f"game_id: {game_id}")
            print(f"result: {result}")

            if (result == True):
                sum_id += int(game_id)

        print(f"sum_id: {sum_id}")


def parse_line(string: str):
    result = True
    game = re.split(':', string)
    game_id = get_game_id(game)
    sets = get_sets(game)
    for subset in sets:
        cubes = get_cubes(subset)
        result = analyze_cubes(cubes)
        if (result == False):
            break

    return game_id, result


def get_game_id(game: str):
    game_id = re.split('Game ', game[0])
    return game_id[1]


def get_sets(game: str):
    sets = re.split(';', game[1])
    return sets


def get_cubes(subset: str):
    cubes = re.split(',', subset)
    return cubes


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
