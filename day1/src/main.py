def load_input_data(file):
    elves_calories = []
    with open(file, 'r') as input_data:
        calories = []
        for line in input_data.readlines():
            if line == "\n":
                elves_calories.append(sum(calories))
                calories = []
            else:
                calories.append(int(line))
    return elves_calories


def find_total_n_calories(data, n=1):
    if n == 1:
        return max(data)
    return sum(sorted(data, reverse=True)[:n])


def solve_p1(data):
    print("Total Calories: {0}".format(find_total_n_calories(data)))


def solve_p2(data):
    print("Total Calories: {0}".format(find_total_n_calories(data, 3)))
