import unittest
from day4.src import main


class Day4TestCase(unittest.TestCase):


    def test_given_an_input_data__load_input_data__should_load_and_parse_data_correctly(self):
        """
            Given an input data, function 'load_data' should load and parse it into a list
        """
        # Given
        inputs = 'data/test_input_1.txt'

        # When
        actual = main.load_data(inputs)
        expected = [({2,3,4},{6,7,8}),({2,3},{4,5}),({5,6,7},{7,8,9}),({2,3,4,5,6,7,8},{3,4,5,6,7}),({6},{4,5,6}),({2,3,4,5,6},{4,5,6,7,8})]

        # Then
        self.assertEqual(expected, actual)  # add assertion here

    def test_given_an_assignment__parse_assignment__should_return_set(self):
        """
            Given an assignment (start-end) should return set {start, ...., end}
        """
        # Given
        assignment = '2-7'

        # When
        actual = main.parse_assignment(assignment)
        expected = {2,3,4,5,6,7}

        # Then
        self.assertEqual(expected, actual)

    def test_given_a_pair_of_assignments__parse_assignments__should_return_tuple_of_assignments(self):
        """
            Given a pair of assignments (start-end,start-end) function parse_assignments should return tuple with sets
        """
        # Given
        assignments = '1-3,4-6'

        # When
        actual  = main.parse_assignments(assignments)
        expected = ({1,2,3},{4,5,6})

        # Then
        self.assertEqual(expected, actual)

    def test__is_fully_overlapping__should_return_true_if_one_set_overlaps_another(self):
        """
            Given 2 sets check if either set1 or set2 is subset of the other
        """
        # Given
        params = [[{2,3,4}, {1,2,3,4,5}, 'Test case: set 1 is subset of set2'],
                  [{1,2,3,4,5}, {2,3,4}, 'Test case: set 1 is superset of set2']]
        for set1, set2, test_case in params:
            # When
            actual = main.is_fully_overlapping(set1, set2)

            # Then
            self.assertTrue(actual, test_case)

if __name__ == '__main__':
    unittest.main()
