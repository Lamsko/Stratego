from game.move import Move
from strategies.strategy import Strategy
from random import randrange


# Random empty field strategy
class RandomMove(Strategy):
    def move(self, board, player, other_player):
        while True:
            row = randrange(board.size())
            column = randrange(board.size())
            if not board.is_field_used(row, column):
                return Move(row, column)
