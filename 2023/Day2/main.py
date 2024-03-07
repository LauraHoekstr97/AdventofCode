from collections import defaultdict

# Imports the input of the puzzle (from the txt file)
# Puts every line in a list for easy accessibility.
file1 = open("input.txt", "r")
list_lines = list()
for line in file1:
    list_lines.append(line)

# Removes game number and splits the different sub-games.
def clean_data(line):
    line = line.strip() # Removes \n
    y = ' '.join(line.split(' ')[2:]) # Removes game number.
    cleaned_line = y.split('; ') # Different list for every sub-game.

    return cleaned_line


def find_possible_subgames(cleaned_line, green_count, blue_count, red_count):
    possible_game = "yes"

    # Collects all color counts for a game -> creates an easy accessible dict.
    color_counts_dict = defaultdict(list)

    for sub_game in cleaned_line:
        sub_game = sub_game.split(', ')

        for color_counts in sub_game:
            count, color = color_counts.split(" ")
            color_counts_dict[color].append(count)

    # Compares the counts with the given color counts.
    # If any count is bigger than the expected color count, give back as a game that is not possible (= "no").
    if any(int(y) > green_count for y in color_counts_dict["green"]):
        possible_game = "no"

    if any(int(y) > blue_count for y in color_counts_dict["blue"]):
        possible_game = "no"

    if any(int(y) > red_count for y in color_counts_dict["red"]):
        possible_game = "no"

    # return whether game is possible
    return possible_game

# Answer part 1
sum = 0 # Keeps track of the answer
game = 1 # Keeps track of game number

for line in list_lines:
    x = clean_data(line)
    y = find_possible_subgames(x, 13, 14, 12)

    if y == "yes":
        sum += game

    game += 1

print(f"Answer part 1: {sum}")


###### Part 2

# Find maximal value per color of blocks.
def maximaal(color_counts):
    count = 0
    for i in color_counts:
        if int(i) > count:
            count = int(i)

    return(count)

def puzzle_4(cleaned_line):
    # Collects all color counts for a game -> creates an easy accessible dict.
    color_counts_dict = defaultdict(list)

    for sub_game in cleaned_line:
        sub_game = sub_game.split(', ')

        for color_counts in sub_game:
            count, color = color_counts.split(" ")
            color_counts_dict[color].append(count)

    # Finds the max of each color
    max_red = maximaal(color_counts_dict["red"])
    max_green = maximaal(color_counts_dict["green"])
    max_blue = maximaal(color_counts_dict["blue"])

    return max_red, max_green, max_blue

# Calculating the power, and thus the answer to part 2.
total_power = 0
for line in list_lines:
    power = 1
    x = clean_data(line)
    y = puzzle_4(x)

    for val in y:
        power *= int(val)
    total_power += power

print(f"Answer part 2: {total_power}")

