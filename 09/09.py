def read_data(PATH: str) -> list:
    # data = []
    with open(PATH, "r") as file:
        content = file.read()
        # data.append(list(map(int, content)))
        data = list(map(int, content))
    return data

def separate_into_files_and_free_space(data: list) -> list:
    files = []
    free_spaces = []
    for index, item in enumerate(data):
        if index % 2 == 0:
            files.append(item)
        if index % 2 != 0:
            free_spaces.append(item)
    return files, free_spaces



PATH = "/home/jonas/Documents/advent_of_code/09/test_input.txt"
# PATH = ("/home/jonas/Documents/advent_of_code/09/input.txt")
data = read_data(PATH)

files, free_spaces = separate_into_files_and_free_space(data)


