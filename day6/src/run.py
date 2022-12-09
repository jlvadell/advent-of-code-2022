import main

print("Day 6")
input_file = '../data/input.txt'
text = main.load_datastream(input_file)
print("Part One:")
solution = main.solve_part_1(text)
print("Solution: {0}".format(solution))
print("Part Two:")
solution = main.solve_part_2(text)
print("Solution: {0}".format(solution))
print("-----------------------------------------------------------")
