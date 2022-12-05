import unittest
from day3.src import main


class Day3TestCase(unittest.TestCase):

    """
    Given an input of rucksacks load_rucksacks should return list of rucksack and compartments,
    Example for 1 rucksack:    [[compartment1, compartment2]]
    """
    def test_given_an_input__load_rucksacks__should_load_data(self):
        # Given
        input_file = 'data/test_input_1.txt'

        # When
        actual = main.load_rucksacks(input_file)
        expected = [['vJrwpWtwJgWr', 'hcsFMMfFFhFp'],
                    ['jqHRNqRjqzjGDLGL', 'rsFMfFZSrLrFZsSL'],
                    ['PmmdzqPrV', 'vPwwTWBwg'],
                    ['wMqvLMZHhHMvwLH', 'jbvcjnnSBnvTQFn'],
                    ['ttgJtRGJ', 'QctTZtZT'],
                    ['CrZsJsPPZsGz', 'wwsLwLmpwMDw']]

        # Then
        self.assertEqual(expected, actual)

    """
    Given a Rucksack ([c1, c2]) find_misplaced_items should return set of misplaced items ({'a', 'b'})
    """
    def test_given_a_rucksack__find_misplaced_items__should_return_set_of_misplaced_items(self):
        # Given
        rucksack = ['abCDEfgH', 'ABCdeFgh']

        # when
        actual = main.find_misplaced_items(rucksack)
        expected = {'C', 'g'}

        # Then
        self.assertEqual(expected, actual)

    """
    Given an item get_priority should return correct priority
    """
    def test_given_an_item__get_priority__should_return_correct_priority(self):
        # Given
        lower_case_items = [chr(x) for x in range(ord('a'), ord('z')+1)]
        upper_case_items = [chr(x) for x in range(ord('A'), ord('Z') + 1)]

        # When-Then
        for item in lower_case_items:

            actual = main.get_priority(item)
            expected = ord(item) - 96

            self.assertEqual(expected, actual, 'test item {0}'.format(item))

        for item in upper_case_items:
            actual = main.get_priority(item)
            expected = ord(item) - 38

            self.assertEqual(expected, actual, 'test item {0}'.format(item))



    """
    Given a rucksack group find_group_badge should return correct group badge
    """
    def test_given_a_rucksack_group__find_group_badge__should_return_badge(self):
        # Given
        group = [['abCdef', 'uvwxyz'], ['abCdeF', 'uvwxyZ'], ['rnpChgt', 'UVWXYz']]

        # When
        actual = main.find_group_badge(group)
        expected = 'C'

        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
