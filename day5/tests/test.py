import unittest
from day5.src import main
from collections import deque


class Day5TestCase(unittest.TestCase):
    def test_given_a_move_instruction__parse_instruction__should_return_CraneInstruction(self):
        """
        Given an instruction ('`instruction_type` `qty` from `origin` to `destination`') function parse_instruction
        should return a correct CraneInstruction
        """
        # Given
        move_instruction = 'move 5 from 2 to 1'

        # When
        actual = main.parse_instructions(move_instruction)
        expected = main.CraneInstructionMove(5,2,1)

        # Then
        self.assertEqual(expected, actual)

    def test_given_a_container_input__parse_containers__should_return_list_of_items(self):
        """
        Given a container input ('[C] [C] [C]') function parse_containers
        should return list of items
        """
        # Given
        container_line = '    [M] [X]'

        # When
        actual = main.parse_containers(container_line)
        expected = ['', 'M', 'X']

        # Then
        self.assertEqual(expected, actual)

    def test_given_an_input_file__load_data__should_return_container_and_instruction_data(self):
        """
        Given an actual input load_data should return containers and instructions
        """
        # Given
        input_file = 'data/test_input_1.txt'

        # When
        actual_containers, actual_instructions = main.load_data(input_file)
        expected_containers = [
            deque(['Z', 'N']),
            deque(['M', 'C', 'D']),
            deque(['P',])
        ]
        expected_instructions = [
            main.CraneInstructionMove(1, 2, 1),
            main.CraneInstructionMove(3, 1, 3),
            main.CraneInstructionMove(2, 2, 1),
            main.CraneInstructionMove(1, 1, 2)
        ]
        # Then
        self.assertEqual(expected_containers, actual_containers)
        self.assertEqual(expected_instructions, actual_instructions)

    def test_given_a_set_of_containers_and_a_move_instruction__perform__should_be_able_to_execute_instruction(self):
        """
        Given an instruction it should be able to execute it on a given set of containers
        """
        # Given
        containers = [deque(['A','B','C']), deque(['A']), deque(['A','B','C','C','B'])]
        instruction = main.CraneInstructionMove(2, 3, 2)

        # When
        instruction.perform(containers)
        expected = [deque(['A','B','C']), deque(['A','B','C']), deque(['A','B','C'])]

        # Then
        self.assertEqual(expected, containers)

    def test__solve_part_1_should_return_correct_solution(self):
        """
        Given the example test data solve_part_1 should return correct solution
        """
        # Given
        test_file = 'data/test_input_1.txt'
        
        # When
        actual = main.solve_part_1(test_file)
        expected = 'CMZ'

        # Then
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
