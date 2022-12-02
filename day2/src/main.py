from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def calculate_score(opponent, player):
    score_result = calculate_result_score(opponent, player)
    return score_result + player.value


def player_won(opponent, player):
    if opponent == Shape.ROCK:
        return player == Shape.PAPER
    elif opponent == Shape.PAPER:
        return player == Shape.SCISSORS
    return player == Shape.ROCK


def calculate_result_score(opponent, player):
    if opponent == player:
        return 3
    elif player_won(opponent, player):
        return 6
    return 0
