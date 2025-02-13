import itertools


def read_data(PATH: str):
    data = []
    with open(PATH, "r") as file:
        for line in file:
            line = line.replace(":", "")
            temp_row = line.split()
            temp_row = list(map(int, temp_row))
            data.append(temp_row)
    return data


PATH = "/home/jonas/coding_practice/advent_of_code/07/input.txt"
data = read_data(PATH)

total_calibration = 0

for row in data:
    result = row[0]
    row_without_result = row[1:]
    combinations_of_operators = itertools.product(
        ["+", "*"], repeat=len(row_without_result) - 1
    )

    for combination in combinations_of_operators:
        result_of_combinations = row_without_result[0]

        for i in range(len(combination)):
            if combination[i] == "+":
                result_of_combinations += row_without_result[i + 1]
            if combination[i] == "*":
                result_of_combinations *= row_without_result[i + 1]

        if result_of_combinations == result:
            total_calibration += result
            break

print(total_calibration)
