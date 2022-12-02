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


def solve_p1(file):
    data = load_input_data(file)
    calories = max(data)
    print("Total Calories: " + str(calories))

