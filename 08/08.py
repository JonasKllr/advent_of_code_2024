import numpy as np


def read_data(PATH: str) -> list:
    data = []
    with open(PATH, "r") as file:
        for line in file:
            line = line.strip("\n")
            data.append(list(line))
    return data


def find_all_matching_occurencies(data: list, character_to_match: str) -> list:
    indeces = []
    for row_id, row in enumerate(data):
        for col_id, character in enumerate(row):
            if character == character_to_match:
                indeces.append([row_id, col_id])
    return indeces


def find_all_hashtag_ids(indeces: list) -> list:
    remaining_indeces = indeces.copy()
    hashtag_indeces = []

    for current_index in indeces:
        remaining_indeces.pop(0)
        for remaining_index in remaining_indeces:
            index_difference = np.subtract(remaining_index, current_index)
            hashtag_indeces.append(np.subtract(current_index, index_difference))
            hashtag_indeces.append(np.add(remaining_index, index_difference))

    return hashtag_indeces


def delete_checked_chars_from_map(data: list, indeces_char: list) -> list:
    for index in indeces_char:
        data[index[0]][index[1]] = "."
    return data


def delete_out_of_bound_ids(indeces: list, data: list) -> list:
    indeces_to_delete = []
    for i, index in enumerate(indeces):
        if (
            index[0] < 0
            or index[0] > len(data) - 1
            or index[1] < 0
            or index[1] > len(data[0]) - 1
        ):
            indeces_to_delete.append(i)

    indeces = np.delete(indeces, indeces_to_delete, axis=0)
    return indeces


def remove_duplication(indeces: np.ndarray) -> np.ndarray:
    return np.unique(indeces, axis=0)


PATH = "/home/jonas/coding_practice/advent_of_code/08/input.txt"
data = read_data(PATH)

indeces_hashtags = []
for row in data:
    for character in row:

        if character != ".":
            indeces_of_same_char = find_all_matching_occurencies(data, character)
            indeces_hashtags_temp = find_all_hashtag_ids(indeces_of_same_char)

            for index in indeces_hashtags_temp:
                indeces_hashtags.append(index)

            data = delete_checked_chars_from_map(data, indeces_of_same_char)

indeces_hashtags = delete_out_of_bound_ids(indeces_hashtags, data)
indeces_hashtags = remove_duplication(indeces_hashtags)
print(np.shape(indeces_hashtags)[0])
