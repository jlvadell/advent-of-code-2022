import unittest
from day6.src import main


class Day6TestCase(unittest.TestCase):

    def test_given_a_text__find_non_repeating_sequence__should_return_sequence_and_finish_index(self):
       """
       Given a text find_non_repeating_sequence should return the sequence and the index of the next char after the sequence
       """
       # Given
       text = 'AAABCABCDAAAAA'
       seq_len = 4

       # When
       actual_sequence, actual_index = main.find_non_repeating_sequence(text, seq_len)
       expected_sequence = 'ABCD'
       expected_index = 9

       # Then
       self.assertEqual(expected_sequence, actual_sequence)
       self.assertEqual(expected_index, actual_index)

    def test_given_a_file__load_data_stream__should_return_file_contents_as_string(self):
        # Given
        input_file = 'data/test_input_1.txt'

        # When
        actual = main.load_datastream(input_file)
        expected = 'ABCDEFGH'

        # Then
        self.assertEqual(expected, actual)

    def test__solve_part_1__should_find_correct_solution(self):
        # Given
        params = [
            ['mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7],
            ['bvwbjplbgvbhsrlpgdmjqwftvncz', 5],
            ['nppdvjthqldpwncqszvftbrmjlhg', 6],
            ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10],
            ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 11],
        ]

        for text, expected_solution in params:
            # When
            actual = main.solve_part_1(text)

            # Then
            self.assertEqual(expected_solution, actual)





if __name__ == '__main__':
    unittest.main()
