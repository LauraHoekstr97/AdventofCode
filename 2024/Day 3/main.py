# Advent of Code 2024 - Day 3 - Mull It Over
import re


# Prepares data for usage.
def data_prep():
    # Gets the input of the puzzle (== corrupted memory).
    file1 = open("input.txt", "r").read()

    # Turns the input data into one big string, so the instructions won't be cut off by \n.
    one_string = file1.replace("\n", "")

    return one_string


# Calculates solution - Part 1
def solution_part1(corrupted_memory, part):
    result = 0  # Keeps track of the sum of all the real multiplications (== final result).

    # Searches the corrupted_memory for all real MUL instructions.
    real_mul_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", corrupted_memory)

    # Finds all numbers in the real MUL instructions.
    for mul_calculation in real_mul_instructions:
        numbers = re.findall(r"\d{1,3}", mul_calculation)  # Extracts the numbers for the multiplication.
        multiplication = int(numbers[0]) * int(numbers[1])  # Does the calculation of the multiplication.
        result += multiplication  # Adds the multiplication to the total result (== the final result).

    # Prints solution of Day 3 - Part 1.
    if part == "part_1":
        print(f"Solution Day 3 - Part 1: {result}")

    # Prints solution of Day 3 - Part 2. (since this method is also used for part 2)
    else:
        print(f"Solution Day 3 - Part 2: {result}")


# Calculates solution - Part 2
def solution_part2(corrupted_memory):
    # Removes everything between a don't and the next do.
    new_data = re.sub(r"don't\(\).*?do\(\)", '', corrupted_memory)
    # Handles, and thus removes, data that sees a don't but never encounters a do later on.
    newer_data = re.sub(r"don't\(\).*", '', new_data)

    # After the new rules are applied to the data, solving the problem in the same way as part 1.
    solution_part1(newer_data, "part_2") 


# Runs the program to get the results.
x = data_prep()
solution_part1(x, "part_1")
solution_part2(x)
