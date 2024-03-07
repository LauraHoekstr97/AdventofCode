# Imports the input of the puzzle
# Puts every line in a list for easy accessibility.
file1 = open("input.txt", "r")
list_line = list()
for line in file1:
    list_line.append(line)

# Function to find 1st and last number of a string.
def find_1st_digit(line):
    digit = None
    for tok in line:
        if tok.isdigit():
            digit = tok
        # Stop searching for digits once the first one is found (possibly reducing runtime, especially for very long strings).
        if digit != None:
            break
    return(digit)

def find_two_digit_number(line):
    first_digit = find_1st_digit(line) # To find the first digit
    last_digit = find_1st_digit(line[::-1])# Reverse line to find last digit.

    return (first_digit + last_digit)

# Answer part 1
sum_1 = 0
for line in list_line:
    x = int(find_two_digit_number(line))
    sum_1 += x

print(f"Answer part 1: {sum_1}")

#Answer part 2
sum_2 = 0
for line in list_line: # Chaning all numbers that are written out to digits.
    new_line = line.replace("one", "o1e")
    new_line = new_line.replace("two", "t2o") # leaving the t and the o, since these letter could also form another spelled out word.
    new_line = new_line.replace("three", "t3e")
    new_line = new_line.replace("four", "4")
    new_line = new_line.replace("five", "5e")
    new_line = new_line.replace("six", "6")
    new_line = new_line.replace("seven", "7n")
    new_line = new_line.replace("eight", "e8t")
    new_line = new_line.replace("nine", "n9n")

    x = int(find_two_digit_number(new_line))
    sum_2 += x

print(f"Answer part 2: {sum_2}")


