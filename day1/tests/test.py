import unittest
from day1.src import main


class Day1TestCase(unittest.TestCase):

    """
    Given an input data, function 'load_input_data' should load and parse it into an integer list
    """
    def test_given_an_input_data__load_input_data__should_load_and_parse_data_correctly(self):
        # Given
        inputs = 'data/test_input_1.txt'

        # When
        actual = main.load_input_data(inputs)
        expected = [6000, 4000, 11000, 24000]

        # Then
        self.assertEqual(expected, actual)  # add assertion here

    """
    Given a list of integers, function 'find_total_n_calories' should return the biggest one
    """
    def test_given_a_list_of_ints__find_total_n_calories__should_find_the_max_number(self):
        # Given
        data = [20, 40, 50, 60, 10, 9, 8]

        # When
        actual = main.find_total_n_calories(data)
        expected = 60

        # Then
        self.assertEqual(expected, actual)

    """
    Given a list of integers, function 'find_total_n_calories' should return the sum of the biggest five
    """
    def test_given_a_list_of_ints__find_total_n_calories__should_find_the_sum_of_the_5_biggest(self):
        # Given
        data = [20, 10, 80, 65, 3, 560, 13, 66]

        # When
        actual = main.find_total_n_calories(data, 5)
        expected = 791

        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
