# Advent of Code 2024 - Day 2 - Red-Nosed Reports

# Prepares data for usage.
def data_prep():
    # Gets the input of the puzzle (== the reports).
    file1 = open("input.txt", "r")

    # Puts data is an easy accessible data structure (a matrix: a list in a list)
    reports = []

    # Goes over every report, to collect all levels (and its number) in a useful format.
    for report in file1:
        clean_report = report.strip()  # Removes \n.
        level_list = clean_report.split(' ')  # Splits the numbers on a space.

        # Turns all the number strings into integers, to be able to do calculations with them later on.
        level_list_int = [int(number) for number in level_list]

        # Put input in the easy accessible data structure. (== list of lists)
        reports.append(level_list_int)

    return reports


# Checks first requirement: the levels are either all increasing or all decreasing.
def check_first_requirement(report_to_be_checked):
    requirement_one_met = "no"  # To keep track whether the second requirement is met.

    decrease_report = sorted(report_to_be_checked, reverse=True)
    increase_report = sorted(report_to_be_checked)

    # If levels of report are in decreased order, then it should be the same as the sorted one.
    # If levels of report are in increased order, then it should be the same as the reversed sorted one.
    if report_to_be_checked == decrease_report or report_to_be_checked == increase_report:
        requirement_one_met = "yes"

    return requirement_one_met


# Checks second requirement: any two adjacent levels differ by at least one and at most three.
def check_second_requirement(report_to_be_checked):
    amount_of_levels_in_report = len(report_to_be_checked)

    # Checks all levels whether they meet the second requirement.
    for i in range(amount_of_levels_in_report - 1):  # -1 since last number can not be compared to a next one.
        difference = abs(report_to_be_checked[i] - report_to_be_checked[i+1])  # Compares number with next number.

        # When the requirement is not met for a level pair, immediately return no.
        if (difference < 1) or (difference > 3):
            return "no"

    # Returns yes when the second requirement is met for all levels in the report
    return "yes"


# Calculates solution - Part 1
def solution_part1(reports):
    # Calculates how many reports are safe (== when both requirement are met).
    amount_safe_reports = 0
    for report in reports:

        # Only need to check second requirement, when first requirement is met.
        if (check_first_requirement(report)) == "yes":
            if (check_second_requirement(report)) == "yes":
                amount_safe_reports += 1

    # Prints solution of Day 2 - Part 1.
    print(f"Solution Day 2 - Part 1: {amount_safe_reports}")


# Calculates solution - Part 2
def solution_part2(reports):
    # Calculates how many reports are safe (== when both requirement are met and allowing at most 1 error).
    amount_safe_reports = 0

    # Collects all possible reports when removing 1 level.
    for report in reports:
        report_subsets = [report]  # To safe all subsets, and also including the original report.

        # Creates all subsets, by removing one level, of the report.
        for i in range(len(report)):
            report_with_one_level_removed = report.copy()
            del report_with_one_level_removed[i]
            report_subsets.append(report_with_one_level_removed)

        # Checks original report and all allowed subsets for meeting both requirements.
        for subset in report_subsets:
            # Only need to check second requirement, when first requirement is met.
            if (check_first_requirement(subset)) == "yes":
                if (check_second_requirement(subset)) == "yes":
                    amount_safe_reports += 1
                    break  # Loop gets terminated when 1 safe option of a report is found.

    # Prints solution of Day 2 - Part 2.
    print(f"Solution Day 2 - Part 2: {amount_safe_reports}")


# Runs the program to get the results.
x = data_prep()
solution_part1(x)
solution_part2(x)

# Prints side note on solution code.
print(f"Note on solutions: example 8 6 4 4 1 is unsafe because 4 4 is neither an increase or a decrease. "
      f"However this is viewed as decreasing in my code, however this case is captured later on in "
      f"requirement 2 since the difference from 4 to 4 is not at least 1. And thus will still result in the "
      f"correct answer.")
