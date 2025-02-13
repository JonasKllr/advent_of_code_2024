import numpy as np

PATH = "/home/jonas/coding_practice/advent_of_code/01/"

both_lists = np.loadtxt(f"{PATH}advent_of_code.csv", delimiter=",", dtype=int)
first_list, second_list = np.split(both_lists, indices_or_sections=2, axis=1)

lenght_of_list = np.shape(first_list)[0]
first_list = np.reshape(first_list, shape=lenght_of_list)
second_list = np.reshape(second_list, shape=lenght_of_list)

first_list = np.sort(first_list)
second_list = np.sort(second_list)

differences = np.absolute(first_list - second_list)
total_distance = np.sum(differences)
print(total_distance)
