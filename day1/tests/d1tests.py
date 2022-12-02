import unittest
from day1.src import main


class Day1TestCase(unittest.TestCase):

    """
    Given an input data, function 'load_input_data' should load and parse it into an integer list
    """
    def test1(self):
        # Given
        inputs = 'data/test_input_1.txt'

        # When
        actual = main.load_input_data(inputs)
        expected = [6000, 4000, 11000, 24000]

        # Then
        self.assertEqual(actual, expected)  # add assertion here

