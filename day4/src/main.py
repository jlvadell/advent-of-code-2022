def parse_assignments(raw_assignments: str):
    assignments = raw_assignments.split(',')
    return parse_assignment(assignments[0]), parse_assignment(assignments[1])


def parse_assignment(assignments: str):
    section_range = assignments.split('-')
    return {x for x in range(int(section_range[0]), int(section_range[1])+1, 1)}


def is_fully_overlapping(section: set, another_section: set):
    return section.issubset(another_section) or another_section.issubset(section)


def load_data(input_file):
    with open(input_file, 'r') as input_data:
        data = []
        for line in input_data.readlines():
            data.append(parse_assignments(line))
        return data

def solve_part_1(input_file):
    data = load_data(input_file)
    total = 0
    for sections in data:
        total = total + is_fully_overlapping(sections[0], sections[1])
    print("Total overlapping: {0}".format(total) )
