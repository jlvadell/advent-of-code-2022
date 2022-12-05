from enum import Enum


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    """
    Return the shape that shape win against
    """
    def win_against(self):
        match self.value:
            case self.ROCK.value:
                return self.SCISSORS
            case self.PAPER.value:
                return self.ROCK
            case _:
                return self.PAPER

    """
    Return the shape that shape lose against
    """
    def lose_against(self):
        match self.value:
            case self.ROCK.value:
                return self.PAPER
            case self.PAPER.value:
                return self.SCISSORS
            case _:
                return self.ROCK


class PlayParser:
    def parse(self, opponent_shape, player_shape):
        pass


class PlayParserPartOne(PlayParser):
    def parse(self, opponent_shape, player_shape):
        return self.parse_opponent(opponent_shape), self.parse_player(player_shape)

    def parse_opponent(self, opponent_shape):
        return self.__parse_shape(opponent_shape)

    def parse_player(self, player_shape):
        return self.__parse_shape(player_shape)

    def __parse_shape(self, shape):
        match shape:
            case 'A' | 'X':
                return Shape.ROCK
            case 'B' | 'Y':
                return Shape.PAPER
            case _:
                return Shape.SCISSORS


class PlayParserPartTwo(PlayParser):
    def parse(self, opponent_shape, player_shape):
        opponent = self.parse_opponent(opponent_shape)
        return opponent, self.parse_player(opponent, player_shape)

    def parse_opponent(self, opponent_shape):
        match opponent_shape:
            case 'A' | 'O':
                return Shape.ROCK
            case 'B' | 'X':
                return Shape.PAPER
            case _:
                return Shape.SCISSORS

    def parse_player(self, opponent_shape, player_shape):
        match player_shape:
            case 'X':
                return opponent_shape.win_against()
            case 'Y':
                return opponent_shape
            case _:
                return opponent_shape.lose_against()


def calculate_score(opponent, player):
    score_result = calculate_result_score(opponent, player)
    return score_result + player.value


def player_won(opponent: Shape, player: Shape):
    return player.win_against() == opponent


def calculate_result_score(opponent, player):
    if opponent == player:
        return 3
    elif player_won(opponent, player):
        return 6
    return 0


def load_plays(file, parser: PlayParser):
    plays = []
    with open(file, 'r') as input_data:
        for line in input_data.readlines():
            shapes = line.split()
            plays.append(parser.parse(opponent_shape=shapes[0], player_shape=shapes[1]))
    return plays


def calculate_total_score(plays):
    total = 0
    for play in plays:
        total = total + calculate_score(play[0], play[1])
    return total


def solve_part_1(file):
    data = load_plays(file, PlayParserPartOne())
    print("Total score: {0}".format(calculate_total_score(data)))


def solve_part_2(file):
    data = load_plays(file, PlayParserPartTwo())
    print("Total score: {0}".format(calculate_total_score(data)))
