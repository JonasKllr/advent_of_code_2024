def reverse_word(word: str):
    word_backward = ""
    for char in reversed(word):
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

# UPPER-LEFT TO LOWER-RIGHT
for i in range(number_of_rows - 2):
    i_ll_ur = i + 2
    for j in range(number_of_columns - 2):
        word_forward_ul_lr = ""
        word_forward_ll_ur = ""
        for m in range(3):
            word_forward_ul_lr += data[i + m][j + m]
            word_forward_ll_ur += data[i_ll_ur - m][j + m]

        word_backward_ul_lr = reverse_word(word_forward_ul_lr)
        word_backward_ll_ur = reverse_word(word_forward_ll_ur)

        if (word_backward_ul_lr == "MAS" or word_forward_ul_lr == "MAS") and (
            word_backward_ll_ur == "MAS" or word_forward_ll_ur == "MAS"
        ):
            word_counter += 1

print(word_counter)
