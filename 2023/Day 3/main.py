# Imports the input of the puzzle
# Puts every line in a list for easy accessibility.
file1 = open("input.txt", "r")
list_lines = list()
for line in file1:
    cleaned_line = line.strip()  # Removes \n
    list_lines.append(cleaned_line)


# Saves the data in a matrix (= list of lists) for easy accessibility
def data_structure(data):
    structure = []
    # Split every line up into char and save as a list, then append to our matrix data structure.
    for data_line in data:
        list_of_char = [character for character in data_line]
        structure.append(list_of_char)
    return structure


# Checks whether char is a number, symbol or a placeholder. (Also prints if you're missing symbols)
def char_checker(char_to_check):
    if char_to_check.isdigit():
        # print(f"digit: {char_to_check}")
        return "digit"

    elif char_to_check == '.':
        # print(f"placeholder: {'.'}")
        return "placeholder"

    elif char_to_check in ['+', '*', '#', '$', '/', '%', '=', '&', '@', '-']:
        # print(f"symbol: {char_to_check}")
        return "symbol"

    else:
        print(f"There is another symbol: {char_to_check}")


# Checks whether a digit is horizontally.
def connected_horizontally(h_line, position_digit):
    connected_hor = "no"
    length_line = len(h_line)

    # Checks if previous char is a symbol (only if there is a previous symbol).
    if position_digit != 0:
        if char_checker(h_line[position_digit - 1]) == "symbol":
            #  print(f"{digit} connected to symbol, hor left")
            connected_hor = "yes"

    # Checks if next char is a symbol (only if there is a next symbol, and when not already found a symbol on the left).
    if position_digit != length_line - 1 and connected_hor == "no":
        if char_checker(h_line[position_digit + 1]) == "symbol":
            #  print(f"{digit} connected to symbol, hor right")
            connected_hor = "yes"

    return connected_hor


# Checks whether a digit is diagonally connected to a symbol. hi
def connected_diagonally(data_matrix, position):
    width = len(data_matrix[0])
    length = len(data_matrix)
    connected_diag = "no"
    vert, hor = position
    char = data_matrix[vert][hor]

    # Left, Up
    vert, hor = position

    if vert != 0 and hor != 0:
        vert = vert - 1
        hor = hor - 1

        if char_checker(data_matrix[vert][hor]) == "symbol":
            #  print(f"{char} connected to symbol, diag left up")
            connected_diag = "yes"

    # Left, Down
    vert, hor = position

    if vert != (length - 1) and hor != 0 and connected_diag == "no":
        vert = vert + 1
        hor = hor - 1

        if char_checker(data_matrix[vert][hor]) == "symbol":
            #  print(f"{char} connected to symbol, diag left down")
            connected_diag = "yes"

    # Right, Up
    vert, hor = position

    if vert != 0 and hor != (width - 1) and connected_diag == "no":
        vert = vert - 1
        hor = hor + 1

        if char_checker(data_matrix[vert][hor]) == "symbol":
            #  print(f"{char} connected to symbol, diag right up")
            connected_diag = "yes"

    # Right, Down
    vert, hor = position

    if vert != (length - 1) and hor != (width - 1) and connected_diag == "no":
        vert = vert + 1
        hor = hor + 1

        if char_checker(data_matrix[vert][hor]) == "symbol":
            #  print(f"{char} connected to symbol, diag right down")
            connected_diag = "yes"

    # Up
    vert, hor = position

    if vert != 0 and connected_diag == "no":
        vert = vert - 1

        if char_checker(data_matrix[vert][hor]) == "symbol":
            #  print(f"{char} connected to symbol, up")
            connected_diag = "yes"

    # Down
    vert, hor = position

    if vert != (length - 1) and connected_diag == "no":
        vert = vert + 1

        if char_checker(data_matrix[vert][hor]) == "symbol":
            #  print(f"{char} connected to symbol, diag right down")
            connected_diag = "yes"

    return connected_diag


# Finds the WHOLE number corresponding to the connected digit
def whole_number_of_connected_digit(line_number, position_char, data_matrix, width):
    char_line = line_number
    char_pos = position_char

    # Goes and find the first digit, of the number that is connected to a symbol.
    while char_checker(data_matrix[char_line][char_pos - 1]) == "digit" and char_pos != 0:
        char_pos = char_pos - 1
    #  print(f"first number of connected digit is: {data_matrix[char_line][char_pos]}")

    # Build up the whole digit from the first digit to the last digit.
    number_string = data_matrix[char_line][char_pos]
    while char_pos != (width - 1):
        if char_checker(data_matrix[char_line][char_pos + 1]) == "digit":
            number_string = number_string + data_matrix[char_line][char_pos + 1]
            char_pos = char_pos + 1

        else:
            break

    # Start searching for connected digits after the last digit of connected whole number
    new_start_position = char_pos

    return number_string, new_start_position


# Returns list of all the connected (whole) numbers.
def list_connected_numbers(data_matrix, width, length):
    list_connected = []
    line_number = 0  # To keep track of the position of the char (vertically)
    position_char = 0  # To keep track of the position of the char (horizontally).
    done = "no"

    while done == "no":
        char = data_matrix[line_number][position_char]
        x = char_checker(char)

        # If you find a digit:
        if x == "digit":
            # 1. Check whether its is horizontal connected to a symbol,
            horizontally = connected_horizontally(data_matrix[line_number], position_char)

            # 2. Check whether its is diagonally connected to a symbol (ONLY check if not connected horizontally).
            if horizontally == "no":
                position_x = line_number, position_char
                diagonal = connected_diagonally(data_matrix, position_x)

            # If the digit is connected, find the WHOLE number:
            if horizontally == "yes" or diagonal == "yes":
                number, new_pos = whole_number_of_connected_digit(line_number, position_char, data_matrix, width)
                #  print(f"whole number: {number}")
                list_connected.append(int(number))

                # Finds the new position to start searching for a new connected number, after having found a number.
                if new_pos != (width-1):
                    position_char = new_pos + 1

                elif line_number != (length - 1):
                    line_number += 1
                    position_char = 0

                else:
                    done = "yes"

            else:
                if position_char != (width - 1):
                    position_char += 1

                elif line_number != (length - 1):
                    line_number += 1
                    position_char = 0

                else:
                    done = "yes"
        else:
            if position_char != (width - 1):
                position_char += 1

            elif line_number != (length - 1):
                line_number += 1
                position_char = 0

            else:
                done = "yes"

    return list_connected


# ANSWER part 1
data = data_structure(list_lines)

# The length of the dimensions of the data-matrix
length_data = len(data)  # From top do bottom
width_data = len(data[0])  # From left to right

connected_numbers = list_connected_numbers(data, width_data, length_data)
# print(connected_numbers)

sum_collected_numbers = sum(connected_numbers)
print(f"Answer part = {sum_collected_numbers}")


# ANSWER part 2


