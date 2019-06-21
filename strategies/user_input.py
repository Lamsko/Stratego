from game.move import Move
from strategies.strategy import Strategy


# User controlled strategy
class UserInput(Strategy):
    def move(self, board, player, other_player):
        while True:
            row = int(input("Row (0-%d): " % (board.size() - 1)))
            column = int(input("Column (0-%d): " % (board.size() - 1)))
            if not board.is_field_used(row, column):
                return Move(row, column)
