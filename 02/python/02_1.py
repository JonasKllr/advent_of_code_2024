import numpy as np


def is_all_increasing(row: np.ndarray) -> bool:
    return np.all(np.diff(row) > 0)


def is_all_decreasing(row: np.ndarray) -> bool:
    return np.all(np.diff(row) < 0)


def max_three_appart(row: np.ndarray) -> bool:
    return np.all(np.abs(np.diff(row)) <= 3)


PATH = "/home/jonas/coding_practice/advent_of_code/02/"
reports = np.genfromtxt(
    f"{PATH}advent_of_code-02.csv", delimiter=",", filling_values=np.nan
)

safe_counter = 0
for i in range(np.shape(reports)[0]):
    row = reports[i, :]
    row = row[~np.isnan(row)]

    if (is_all_increasing(row) or is_all_decreasing(row)) and max_three_appart(row):
        safe_counter += 1
    else:
        # second part
        for i in range(np.shape(row)[0]):
            temp_row = np.delete(row, i, 0)
            if (
                is_all_increasing(temp_row) or is_all_decreasing(temp_row)
            ) and max_three_appart(temp_row):
                safe_counter += 1
                break

print(safe_counter)
