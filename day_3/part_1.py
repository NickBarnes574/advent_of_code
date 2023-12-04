#!/usr/bin/python3

import os

DIRECTORY = "day_3/test_cases"


def main():
    # List all files in the directory
    for filename in os.listdir(DIRECTORY):
        filepath = os.path.join(DIRECTORY, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(filepath):
            print(f"FILE: {filepath}")
            with open(filepath, "r") as file:
                matrix = create_matrix(file)
                size = len(matrix)
                create_number_data(matrix)


def create_matrix(file):
    """
    Reads a file and creates a 2D matrix from its contents.
    Each character in the file is stored in the matrix with its coordinates printed.

    Parameters:
    file: An iterable object (like a file object) containing strings.

    Returns:
    A 2D list (matrix) representing the characters in the file.
    """
    matrix = []

    for row_num, line in enumerate(file):
        # Strip newline character
        line = line.strip()
        row = []

        for col_num, char in enumerate(line):
            row.append(char)
            # print(f"'{char}' at ({row_num}, {col_num})")

        matrix.append(row)

    return matrix


def create_number_data(matrix):
    total_sum = 0
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    for row_num, row in enumerate(matrix):
        col_num = 0
        while col_num < num_cols:
            char = row[col_num]
            if char.isdigit():
                number = char
                number_start_col = col_num

                # Accumulate the following digits to form the whole number
                col_num += 1
                while col_num < num_cols and row[col_num].isdigit():
                    number += row[col_num]
                    col_num += 1

                # Check if any digit of the whole number is adjacent to a symbol
                is_part_number = False
                for i in range(number_start_col, col_num):
                    if check_for_symbols(row_num, i, matrix):
                        is_part_number = True
                        break

                if is_part_number:
                    total_sum += int(number)

            else:
                col_num += 1

    print(f"sum: {total_sum}")


def check_for_symbols(row_num, col_num, matrix):
    # Getting the dimensions of the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if num_rows > 0 else 0

    boundary = []

    # Function to safely access matrix elements
    def get_element(r, c):
        if 0 <= r < num_rows and 0 <= c < num_cols:
            return matrix[r][c]
        return None  # or some default value

    # north
    boundary.append(get_element(row_num - 1, col_num))
    # north west
    boundary.append(get_element(row_num - 1, col_num - 1))
    # west
    boundary.append(get_element(row_num, col_num - 1))
    # south west
    boundary.append(get_element(row_num + 1, col_num - 1))
    # south
    boundary.append(get_element(row_num + 1, col_num))
    # south east
    boundary.append(get_element(row_num + 1, col_num + 1))
    # east
    boundary.append(get_element(row_num, col_num + 1))
    # north east
    boundary.append(get_element(row_num - 1, col_num + 1))

    for element in boundary:
        if element is not None:
            if not element.isdigit() and element != '.':
                # print(f"symbol: {element}")
                return True  # found a symbol


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
