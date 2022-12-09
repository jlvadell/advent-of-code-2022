import main

print("Day 6")
input_file = '../data/input.txt'
print("Part One:")
text = main.load_datastream(input_file)
solution = main.solve_part_1(text)
print("Solution: {0}".format(solution))
print("Part Two:")

print("-----------------------------------------------------------")
