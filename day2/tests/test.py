import unittest
from day2.src import main


class Day2TestCase(unittest.TestCase):

    """
    Given a play (opponent shape vs player shape) calculate the score (result only) for all the posible outcomes
    """
    def test_given_a_play__calculate_result_score__should_return_correct_core(self):
        # Given
        param_list = [
            (main.Shape.PAPER, main.Shape.SCISSORS, 6, 'Test case: Player wins'),
            (main.Shape.ROCK, main.Shape.ROCK, 3, 'Test case: Draw'),
            (main.Shape.SCISSORS, main.Shape.PAPER, 0, 'Test case: Player lost')
        ]
        for opponent, player, expected, test_case in param_list:
            # When
            actual = main.calculate_result_score(opponent, player)

            # Then
            self.assertEqual(expected, actual, test_case)

    """
    Given a play (opponent shape vs player shape) test all possible win cases from player pov
    """
    def test_given_a_play__player_won__should_return_true_if_player_won(self):
        # Given
        param_list = [
            (main.Shape.PAPER, main.Shape.SCISSORS, 'Test case: Paper vs Scissors'),
            (main.Shape.ROCK, main.Shape.PAPER, 'Test case: Rock vs Paper'),
            (main.Shape.SCISSORS, main.Shape.ROCK, 'Test case: Scissors vs Rock')
        ]
        for opponent, player, test_case in param_list:
            # When
            actual = main.player_won(opponent, player)

            # Then
            self.assertTrue(actual, test_case)

    """
    Given a play (opponent shape vs player shape) test all possible loss/draw cases from player pov
    """
    def test_given_a_play__player_won__should_return_false_if_player_did_not_won(self):
        # Given
        param_list = [
            (main.Shape.PAPER, main.Shape.ROCK, 'Test case: Paper vs Rock'),
            (main.Shape.PAPER, main.Shape.PAPER, 'Test case: Paper vs Paper'),
            (main.Shape.ROCK, main.Shape.SCISSORS, 'Test case: Rock vs Scissors'),
            (main.Shape.ROCK, main.Shape.ROCK, 'Test case: Rock vs Rock'),
            (main.Shape.SCISSORS, main.Shape.PAPER, 'Test case: Scissors vs Paper'),
            (main.Shape.SCISSORS, main.Shape.SCISSORS, 'Test case: Scissors vs Scissors')
        ]
        for opponent, player, test_case in param_list:
            # When
            actual = main.player_won(opponent, player)

            # Then
            self.assertFalse(actual, test_case)

    """
    Given a play (opponent shape vs player shape) test total score obtained for all possible win/loss cases (player pov)
    """
    def test_given_a_play__calculate_score__should_return_correct_score(self):
        # Given
        param_list = [
            (main.Shape.PAPER, main.Shape.SCISSORS, 9, 'Test case: Paper vs Scissors - WIN'),
            (main.Shape.PAPER, main.Shape.ROCK, 1, 'Test case: Paper vs Rock - LOSS'),
            (main.Shape.PAPER, main.Shape.PAPER, 5, 'Test case: Paper vs Paper - DRAW'),
            (main.Shape.ROCK, main.Shape.PAPER, 8, 'Test case: Rock vs Paper - WIN'),
            (main.Shape.ROCK, main.Shape.SCISSORS, 3, 'Test case: Rock vs Scissors - LOSS'),
            (main.Shape.ROCK, main.Shape.ROCK, 4, 'Test case: Rock vs Rock - DRAW'),
            (main.Shape.SCISSORS, main.Shape.ROCK, 7, 'Test case: Scissors vs Rock - WIN'),
            (main.Shape.SCISSORS, main.Shape.PAPER, 2, 'Test case: Scissors vs Paper - LOSS'),
            (main.Shape.SCISSORS, main.Shape.SCISSORS, 6, 'Test case: Scissors vs Scissors - DRAW')
        ]
        for opponent, player, expected, test_case in param_list:
            # When
            actual = main.calculate_score(opponent, player)

            # Then
            self.assertEqual(expected, actual, test_case)

    """
    Given an encrypted_shape (A,B,C | X,Y,Z) parse shape should return correct shape
    """
    def test_given_encrypted_shape__parse_shape__should_return_correct_shape(self):
        # Given
        param_list = [
            ('A', main.Shape.ROCK, 'Test case: A -> Rock'),
            ('X', main.Shape.ROCK, 'Test case: X -> Rock'),
            ('B', main.Shape.PAPER, 'Test case: B -> Paper'),
            ('Y', main.Shape.PAPER, 'Test case: Y -> Paper'),
            ('C', main.Shape.SCISSORS, 'Test case: C -> Scissors'),
            ('Z', main.Shape.SCISSORS, 'Test case: Z -> Scissors')
        ]
        for encrypted_shape, expected, test_case in param_list:
            # When
            actual = main.parse_shape(encrypted_shape)

            # Then
            self.assertEqual(expected, actual, test_case)

    """
    Given an input parse and return list of plays (opponent shape vs player shape)
    """
    def test_given_input__load_plays__should_return_list_of_parsed_plays(self):
        # Given
        input_test_file = 'data/test_input_1.txt'
        # When
        actual = main.load_plays(input_test_file)
        expected = [(main.Shape.ROCK, main.Shape.PAPER), (main.Shape.PAPER, main.Shape.ROCK), (main.Shape.SCISSORS, main.Shape.SCISSORS)]

        # Then
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
