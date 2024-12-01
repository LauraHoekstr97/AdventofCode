# Advent of Code 2024 - Day 1

# Prepares data for usage.
def data_prep():
    # Gets the input of the puzzle (== the location ID's).
    file1 = open("Input - Day 1.txt", "r")

    # Puts the ID's in the corresponding list (left column == List 1, right column == List 2).
    locations_list_1 = []
    locations_list_2 = []

    for line in file1:
        clean_line = line.strip()  # Removes \n.
        locations = clean_line.split('  ')  # Splits numbers.

        # Puts the collected numbers in the correct list.
        # Also turns str location_ID into int location_Id, so we can do calculations with them later on.
        locations_list_1.append(int(locations[0]))
        locations_list_2.append(int(locations[1]))

    return locations_list_1, locations_list_2


# Calculates solution - Part 1
def solution_part1(locations_1, locations_2):
    # Sorting the location_IDs from small to large, for both lists.
    sorted_1 = sorted(locations_1)
    sorted_2 = sorted(locations_2)

    # Get difference of every ID, when comparing both lists, and add them up.  The difference is an absolute value.
    total_difference = 0
    scope = len(sorted_1)
    for i in range(scope):
        difference = abs(sorted_1[i] - sorted_2[i])
        total_difference += difference

    # Prints solution of Day 1 - Part 1.
    print(f"Solution Day 1 - Part 1: {total_difference}")


# Calculates solution - Part 2
def solution_part2(locations_1, locations_2):
    similarity_score = 0  # Keeps track of the similarity score.

    # Checks similarity for all numbers in list 1, when comparing to list 2.
    for num in locations_1:
        occurrences_in_list2 = locations_2.count(num)  # Gets amount of occurrences of number list 1 in list 2.
        similarity_score_increase = num * occurrences_in_list2  # Calculating the increase of the similarity score.
        similarity_score += similarity_score_increase  # Updating similarity score.

    # Prints solution of Day 1 - Part 2.
    print(f"Solution Day 1 - Part 2: {similarity_score}")


# Get solutions
x, y = data_prep()
solution_part1(x, y)
solution_part2(x, y)