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


def load_plays(file):
    plays = []
    with open(file, 'r') as input_data:
        for line in input_data.readlines():
            shapes = line.split()
            plays.append((parse_shape(shapes[0]), parse_shape(shapes[1])))
    return plays


def parse_shape(encrypted_shape):
    match encrypted_shape:
        case 'A' | 'X':
            return Shape.ROCK
        case 'B' | 'Y':
            return Shape.PAPER
        case _:
            return Shape.SCISSORS
