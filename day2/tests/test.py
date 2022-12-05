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
    Given an encrypted_shape (A,B,C | X,Y,Z) parse should return correct play
    """
    def test_given_encrypted_play__PlayParsePartOne__should_return_correct_play(self):
        # Given
        param_list = [
            ('A', 'X', (main.Shape.ROCK, main.Shape.ROCK), 'Test case: A|X -> Rock'),
            ('B', 'Y', (main.Shape.PAPER, main.Shape.PAPER), 'Test case: B|Y -> Paper'),
            ('C', 'Z', (main.Shape.SCISSORS, main.Shape.SCISSORS), 'Test case: C|Z -> Scissors'),
        ]
        parser = main.PlayParserPartOne()
        for opponent, player, expected, test_case in param_list:
            # When
            actual = parser.parse(opponent, player)

            # Then
            self.assertEqual(expected, actual, test_case)

    """
    Given an input parse and return list of plays (opponent shape vs player shape)
    """
    def test_given_input__load_plays__should_return_list_of_parsed_plays(self):
        # Given
        class PlayTestParser(main.PlayParser):
            def parse(self, opponent_shape, player_shape):
                return opponent_shape, player_shape
        input_test_file = 'data/test_input_1.txt'
        # When
        actual = main.load_plays(input_test_file, PlayTestParser())
        expected = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

        # Then
        self.assertEqual(expected, actual)

    """
    Calculate total score should return the correct score
    """
    def test__calculate_total_score__should_return_correct_score(self):
        # Given
        plays = [(main.Shape.ROCK, main.Shape.SCISSORS), (main.Shape.PAPER, main.Shape.SCISSORS)]

        # When
        actual = main.calculate_total_score(plays)
        expected = 12

        # Then
        self.assertEqual(expected, actual)

    """
    Shape function win_against should return the correct shape
    """
    def test_wining_shape(self):
        # Given
        param_list = [
            (main.Shape.ROCK, main.Shape.SCISSORS, 'Test case: Rock --> Scissors'),
            (main.Shape.PAPER, main.Shape.ROCK, 'Test case: Paper -> Rock'),
            (main.Shape.SCISSORS, main.Shape.PAPER, 'Test case: Scissors -> Paper'),
        ]
        for shape, expected, test_case in param_list:
            # When
            actual = shape.win_against()

            # Then
            self.assertEqual(expected, actual, test_case)

    """
    Shape function lose_against should return the correct shape
    """
    def test_losing_shape(self):
        # Given
        param_list = [
            (main.Shape.ROCK, main.Shape.PAPER, 'Test case: Rock --> Paper'),
            (main.Shape.PAPER, main.Shape.SCISSORS, 'Test case: Paper -> Scissors'),
            (main.Shape.SCISSORS, main.Shape.ROCK, 'Test case: Scissors -> Rock'),
        ]
        for shape, expected, test_case in param_list:
            # When
            actual = shape.lose_against()

            # Then
            self.assertEqual(expected, actual, test_case)

    def test_given_encrypted_play__PlayParsePartTwo__should_return_correct_play(self):
        # Given
        param_list = [
            ('A', 'X', (main.Shape.ROCK, main.Shape.SCISSORS), 'Test case: A|X -> Lose vs Rock'),
            ('A', 'Y', (main.Shape.ROCK, main.Shape.ROCK), 'Test case: A|Y -> Draw vs Rock'),
            ('A', 'Z', (main.Shape.ROCK, main.Shape.PAPER), 'Test case: A|Z -> Win vs Rock'),
            ('B', 'X', (main.Shape.PAPER, main.Shape.ROCK), 'Test case: B|X -> Lose vs Paper'),
            ('B', 'Y', (main.Shape.PAPER, main.Shape.PAPER), 'Test case: B|Y -> Draw vs Paper'),
            ('B', 'Z', (main.Shape.PAPER, main.Shape.SCISSORS), 'Test case: B|Z -> Win vs Paper'),
            ('C', 'X', (main.Shape.SCISSORS, main.Shape.PAPER), 'Test case: C|X -> Lose vs Scissors'),
            ('C', 'Y', (main.Shape.SCISSORS, main.Shape.SCISSORS), 'Test case: C|Y -> Draw vs Scissors'),
            ('C', 'Z', (main.Shape.SCISSORS, main.Shape.ROCK), 'Test case: C|Z -> Win vs Scissors'),
        ]
        parser = main.PlayParserPartTwo()
        for opponent, player, expected, test_case in param_list:
            # When
            actual = parser.parse(opponent, player)

            # Then
            self.assertEqual(expected, actual, test_case)


if __name__ == '__main__':
    unittest.main()
