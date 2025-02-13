import numpy as np

PATH = "/home/jonas/coding_practice/advent_of_code/01/"

both_lists = np.loadtxt(f"{PATH}advent_of_code.csv", delimiter=",", dtype=int)
first_list, second_list = np.split(both_lists, indices_or_sections=2, axis=1)

lenght_of_list = np.shape(first_list)[0]
first_list = np.reshape(first_list, shape=lenght_of_list)
second_list = np.reshape(second_list, shape=lenght_of_list)

number, counts = np.unique(second_list, return_counts=True)
number_and_counts = dict(zip(number, counts))

sum = 0
for i in range(lenght_of_list):
    key = first_list[i]
    if key in number_and_counts:
        sum += number_and_counts[key] * first_list[i]

print(sum)
