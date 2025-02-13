def reverse_word(word: str):
    word_backward = ""
    for char in reversed(word_forward):
        word_backward += char

    return word_backward


def read_in_data_as_list(path: str):
    data_as_list = []
    with open(PATH, "r") as file:
        for line in file:
            temp_row = line.strip()
            data_as_list.append(temp_row)

    for i in range(len(data_as_list)):
        data_as_list[i] = list(data_as_list[i])

    return data_as_list


PATH = "/home/jonas/coding_practice/advent_of_code/04/input.txt"
data = read_in_data_as_list(PATH)

number_of_rows = len(data)
number_of_columns = len(data[0])

word_counter = 0
# ROW
for i in range(number_of_rows):
    for j in range(number_of_columns - 3):
        word_forward = ""
        for m in range(4):
            word_forward += data[i][j + m]

        word_backward = reverse_word(word_forward)

        if word_backward == "XMAS" or word_forward == "XMAS":
            word_counter += 1

# COLUMN
for i in range(number_of_rows - 3):
    for j in range(number_of_columns):
        word_forward = ""
        for m in range(4):
            word_forward += data[i + m][j]

        word_backward = reverse_word(word_forward)

        if word_backward == "XMAS" or word_forward == "XMAS":
            word_counter += 1

# UPPER-LEFT TO LOWER-RIGHT
for i in range(number_of_rows - 3):
    for j in range(number_of_columns - 3):
        word_forward = ""
        for m in range(4):
            word_forward += data[i + m][j + m]

        word_backward = reverse_word(word_forward)

        if word_backward == "XMAS" or word_forward == "XMAS":
            word_counter += 1

# LOWER-LEFT TO UPPER-RIGHT
for i in range(number_of_rows - 3):
    i = i + 3
    for j in range(number_of_columns - 3):
        # j = j + 3
        word_forward = ""
        for m in range(4):
            word_forward += data[i - m][j + m]

        word_backward = reverse_word(word_forward)

        if word_backward == "XMAS" or word_forward == "XMAS":
            word_counter += 1

print(word_counter)
