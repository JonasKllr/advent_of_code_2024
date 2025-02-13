import re


def extract_numbers(string: str):
    extracted_numbers = re.findall(r"\d+", string)
    return int(extracted_numbers[0]), int(extracted_numbers[1])


PATH = "/home/jonas/coding_practice/advent_of_code/03/input.txt"
with open(PATH, "r") as file:
    data = file.read().replace("\n", "")
extracted_strings = re.findall(r"mul\(.{1,3},.{1,3}\)|do\(\)|don't\(\)", data)

result = 0
do_multiplication = True
for i in range(len(extracted_strings)):
    if extracted_strings[i] == "do()":
        do_multiplication = True
    elif extracted_strings[i] == "don't()":
        do_multiplication = False

    if (do_multiplication == True) and ("mul" in extracted_strings[i]):
        left_number, right_number = extract_numbers(extracted_strings[i])
        result += left_number * right_number

print(result)
