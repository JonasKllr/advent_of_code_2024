def read_in_rules(PATH: str):
    rules = []
    with open(PATH, "r") as file:
        for line in file:
            temp_row = line.strip("\n").split(sep="|")
            temp_row = list(map(int, temp_row))
            rules.append(temp_row)
    return rules


def read_pages_to_produce(PATH: str):
    pages_to_produce = []
    with open(PATH, "r") as file:
        for line in file:
            temp_row = line.strip("\n").split(sep=",")
            temp_row = list(map(int, temp_row))
            pages_to_produce.append(temp_row)
    return pages_to_produce


def is_order_correct(sequence: list, rules: list):
    correct_order = True

    for rule in rules:
        try:
            id_first_number = sequence.index(rule[0])
            id_second_number = sequence.index(rule[1])
        except:
            continue
        else:
            if id_first_number > id_second_number:
                correct_order = False
                break
    return correct_order


def find_middle_number(sequence: list):
    id_middle_number = float(len(sequence) / 2)
    return sequence[int(id_middle_number - 0.5)]


def get_correct_order(sequence: list, rules: list):
    if not is_order_correct(sequence, rules):
        for rule in rules:
            try:
                id_first_number = sequence.index(rule[0])
                id_second_number = sequence.index(rule[1])
            except:
                continue
            else:
                if id_first_number > id_second_number:
                    sequence[id_first_number], sequence[id_second_number] = (
                        sequence[id_second_number],
                        sequence[id_first_number],
                    )

        get_correct_order(sequence, rules)
    return sequence


PATH_RULES = "/home/jonas/coding_practice/advent_of_code/05/input_rules.txt"
PATH_PAGES = "/home/jonas/coding_practice/advent_of_code/05/input_pages.txt"

rules = read_in_rules(PATH_RULES)
pages_to_produce = read_pages_to_produce(PATH_PAGES)

sum = 0
for sequence in pages_to_produce:
    if is_order_correct(sequence, rules) == False:
        sequence = get_correct_order(sequence, rules)
        sum += find_middle_number(sequence)

print(sum)
