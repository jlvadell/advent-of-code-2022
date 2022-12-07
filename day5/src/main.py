from collections import deque
import re


class CraneInstruction:
    qty: int
    origin: int
    destination: int

    def __eq__(self, other):
        return self.qty == other.qty and \
            self.origin == other.origin and \
            self.destination == other.destination

    def __init__(self, qty: int , origin: int , destination: int):
        self.qty = qty
        self.origin = origin
        self.destination = destination

    def perform(self, containers):
        pass

class CraneInstructionMove(CraneInstruction):
    def perform(self, containers):
        i = 0
        while i < self.qty:
            containers[self.destination-1].append(containers[self.origin-1].pop())
            i += 1

def load_data(input_file):
    with open(input_file, 'r') as input_data:
        containers, instructions = [], []
        reading_instructions = False
        for line in input_data.readlines():
            if line == '\n':
                reading_instructions = True
                continue
            if not reading_instructions and line.find('[') == -1:
                continue
            if reading_instructions:
                instructions.append(parse_instructions(line))
            else:
                container_data = parse_containers(line)
                for i in range(0, len(container_data)):
                    if i > len(containers)-1:
                        containers.append(deque())
                    if container_data[i] != '':
                        containers[i].appendleft(container_data[i])
        return containers, instructions

def parse_instructions(instruction: str):
    instruction_data = instruction.split(' ')
    crane_instruction = None
    if instruction_data[0] == 'move':
        crane_instruction = CraneInstructionMove(int(instruction_data[1]), int(instruction_data[3]), int(instruction_data[5]))
    return crane_instruction

def parse_containers(container_data: str):
    parsed_data = []
    for i in range(0,len(container_data),4):
        container_content = container_data[i:i+4]
        parsed_data.append(re.sub('[\[\]\s\n]+', '', container_content))
    return parsed_data

def solve_part_1(input_file):
    containers, instructions = load_data(input_file)
    for instruction in instructions:
        instruction.perform(containers)
    solution = ''
    for container in containers:
        solution += container[-1]
    return solution