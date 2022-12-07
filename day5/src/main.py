from collections import deque
import re
from enum import Enum

class CraneModel(Enum):
    CRATE_MOVER_9000 = 'CrateMover 9000'
    CRATE_MOVER_9001 = 'CrateMover 9001'

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
        self.origin = origin-1
        self.destination = destination-1

    def perform(self, containers):
        pass

class CraneInstructionCrateMover9000(CraneInstruction):
    def perform(self, containers):
        i = 0
        while i < self.qty:
            containers[self.destination].append(containers[self.origin].pop())
            i += 1

class CraneInstructionCrateMover9001(CraneInstruction):
    def perform(self, containers):
        containers[self.destination].extend(containers[self.origin][len(containers[self.origin]) - self.qty:])
        containers[self.origin] = containers[self.origin][:len(containers[self.origin]) - self.qty]

def load_data(input_file: str, crane_model: CraneModel):
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
                instructions.append(parse_instructions(line, crane_model))
            else:
                add_container_data(parse_containers(line), containers)

        return containers, instructions

def parse_instructions(instruction: str, crane_model: CraneModel):
    instruction_data = instruction.split(' ')
    crane_instruction = None
    match crane_model:
        case CraneModel.CRATE_MOVER_9000:
            crane_instruction = CraneInstructionCrateMover9000(int(instruction_data[1]), int(instruction_data[3]), int(instruction_data[5]))
        case CraneModel.CRATE_MOVER_9001:
            crane_instruction = CraneInstructionCrateMover9001(int(instruction_data[1]), int(instruction_data[3]),
                                                               int(instruction_data[5]))
    return crane_instruction

def add_container_data(data, containers):
    for i in range(0, len(data)):
        if i > len(containers) - 1:
            containers.append(deque())
        if data[i] != '':
            containers[i].appendleft(data[i])

def parse_containers(container_data: str):
    parsed_data = []
    for i in range(0,len(container_data),4):
        container_content = container_data[i:i+4]
        parsed_data.append(re.sub('[\[\]\s\n]+', '', container_content))
    return parsed_data

def solve_part_1(input_file):
    containers, instructions = load_data(input_file, CraneModel.CRATE_MOVER_9000)
    for instruction in instructions:
        instruction.perform(containers)
    solution = ''
    for container in containers:
        solution += container[-1]
    return solution