def load_rucksacks(input_file):
    rucksacks = []
    with open(input_file, 'r') as input_data:
        for line in input_data.readlines():
            items = line.replace('\n', '')
            rucksacks.append([items[slice(0, len(items)//2)], items[slice(len(items)//2, len(items))]])
    return rucksacks


def find_misplaced_items(rucksack):
    compartment_1_items = set(rucksack[0])
    compartment_2_items = set(rucksack[1])
    return compartment_1_items & compartment_2_items


def get_priority(item: str):
    return ord(item)-38 if item.isupper() else ord(item)-96


def find_group_badge(rucksacks):
    rucksack_1_items = set(''.join(rucksacks[0]))
    rucksack_2_items = set(''.join(rucksacks[1]))
    rucksack_3_items = set(''.join(rucksacks[2]))

    return (rucksack_1_items & rucksack_2_items & rucksack_3_items).pop()


def solve_part_1(input_file):
    rucksacks = load_rucksacks(input_file)
    total_priority = 0
    for rucksack in rucksacks:
        total_priority = total_priority + sum([get_priority(x) for x in find_misplaced_items(rucksack)])

    return print("Total priority is: {0}".format(total_priority))


def solve_part_2(input_file):
    rucksacks = load_rucksacks(input_file)
    total_priority = 0
    for i in range(0, len(rucksacks), 3):
        rucksacks_group = rucksacks[i:i+3]
        total_priority = total_priority + get_priority(find_group_badge(rucksacks_group))

    return print("Total priority is: {0}".format(total_priority))

