def load_rucksacks(input_file):
    rucksacks = []
    with open(input_file, 'r') as input_data:
        for line in input_data.readlines():
            items = line.replace('\n', '')
            rucksacks.append([items[slice(0, len(items)//2)], items[slice(len(items)//2, len(items))]])
    return rucksacks


def find_misplaced_items(rucksack):
    misplaced_items = set()
    compartment_1 = rucksack[0]
    compartment_2_items = set(rucksack[1])
    for item in compartment_2_items:
        if item in compartment_1:
            misplaced_items.add(item)

    return misplaced_items


def get_priority(item: str):
    return ord(item)-38 if item.isupper() else ord(item)-96


def solve_part_1(input_file):
    rucksacks = load_rucksacks(input_file)
    total_priority = 0
    for rucksack in rucksacks:
        total_priority = total_priority + sum([get_priority(x) for x in find_misplaced_items(rucksack)])

    return print("Total priority is: {0}".format(total_priority))

