#!/usr/bin/python3

import re

FILEPATH = "day_2/data.txt"


def main():
    power_sum = 0

    with open(FILEPATH, "r") as file:
        for line in file:
            game_data = extract_game_data(line)
            game_id, power = process_game_data(game_data)
            print(f"game id: {game_id}")
            print(f"power: {power}")

            power_sum += int(power)

        print(f"power sum: {power_sum}")


def extract_game_data(string):
    """Extracts game ID and sets from the given string."""
    game = re.split(': ', string)
    game_id = game[0].split('Game ')[1]
    sets = game[1].split(';')
    return game_id, sets


def process_game_data(game_data):
    """Processes game data to determine the result based on cubes in sets."""
    game_id, sets = game_data

    min_red = 0
    min_green = 0
    min_blue = 0
    for subset in sets:
        cubes = subset.split(',')
        red, green, blue = get_num_colors(cubes)
        if red > min_red:
            min_red = red
        if green > min_green:
            min_green = green
        if blue > min_blue:
            min_blue = blue

    power = min_red * min_green * min_blue
    return game_id, power


def get_num_colors(cubes: list):
    red = 0
    green = 0
    blue = 0
    for cube in cubes:
        cube = cube.strip()
        amount_color = re.split(' ', cube)
        if amount_color[1] == 'red':
            red = int(amount_color[0])
        if amount_color[1] == 'green':
            green = int(amount_color[0])
        if amount_color[1] == 'blue':
            blue = int(amount_color[0])

    return red, green, blue


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
