from collections import defaultdict
import numpy as np

# Imports the input of the puzzle (from the txt file)
# Puts every line in a list for easy accessibility.
file1 = open("input.txt", "r")
list_lines = list()
for line in file1:
    list_lines.append(line)


# Returns clean data 
def clean_data(lines):
    lines = lines.strip()  # Removes \n
    clean = ' '.join(lines.split(' ')[2:])  # Removes card number.
    return clean

######################################### Part 1 ######################################################################

# Puts winning numbers and your numbers in separate lists
def get_numbers(cleaned_data):
    winning_numbers, your_numbers = cleaned_data.split(' | ')
    winning_numbers = winning_numbers.split()
    your_numbers = your_numbers.split()

    return winning_numbers, your_numbers


# Calculates the points of a single card.
def winning_points(winning_numbers, your_numbers):

    # Loops through all your numbers and checks whether it is a winning number.
    winning_count = 0

    for number in your_numbers:
        if number in winning_numbers:
            winning_count += 1

    # Calculates the winning points of the card
    if winning_count == 0:
        points = 0

    else:
        points = 2 ** (winning_count-1)

    return points


# Answer part 1: Calculates total points of ALL the scratchcards.
total_points = 0

for card in list_lines:
    data = clean_data(card)
    win, your = get_numbers(data)
    card_points = winning_points(win, your)
    total_points += card_points

print(f"Answer part 1: {total_points}")


######################################### Part 2 ######################################################################

def data_prep(our_data):

    # Creating a data structure that is useful for this puzzle:
    # where key == number of cards - 1, value == numbers on the card  (winning numbers | your numbers)
    cards_dict = defaultdict(str)

    # Put our data in the dict
    count = 0

    for card_2 in our_data:
        cards_dict[count] = card_2
        count += 1

    # List to store the amount of any card (card 1 is stored as 0)
    amount_cards = np.ones(count)

    return cards_dict, amount_cards


# The same function as wining_points, however we now only need the amount of wins and not the points.
def wins(winning_n, your_n):

    # Loops through all your numbers and checks whether it is a winning number.
    winning_count = 0

    for number in your_n:
        if number in winning_n:
            winning_count += 1

    return winning_count


# Function to calculate the amount of cards you eventually have.
def total_cards(data_2):
    cards, amount_per_card = data_prep(data_2)
    amount_of_card_numbers = len(amount_per_card)

    # Checks for every card the wins, and thus how many new cards (= copies) to add.
    for i in range(amount_of_card_numbers):
        num_cards = amount_per_card[i]

        # Check the amount of wins
        card_data = clean_data(cards[i])
        winning_num, your_num = get_numbers(card_data)
        new_cards = wins(winning_num, your_num)

        # Add the extra scratchcards gained by winning to amount_per_card
        position_new_card = i + 1
        for j in range(new_cards):
            if position_new_card < amount_of_card_numbers:
                amount_per_card[position_new_card] += (1 * num_cards)  # The original AND the copies win new cards.
                position_new_card += 1
            else:
                break  # break, since "cards will never make you copy a card past the end of the table"

    tot_card = sum(amount_per_card)

    return tot_card


# Answer part 2
answer_2 = total_cards(list_lines)
print(f"Answer part 2: {answer_2}")
