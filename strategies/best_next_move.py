from game.move import Move
from game.points_calculator import PointsCalculator
from strategies.strategy import Strategy


# Strategy which returns field which gives most points in current move
class BestNextMove(Strategy):
    def move(self, board, player, other_player):
        max_points = 0
        best_move = None
        for row in range(0, board.size()):
            for column in range(0, board.size()):
                if not board.is_field_used(row, column):
                    move = Move(row, column)
                    board.apply_move(move, player)
                    points = PointsCalculator.calculate(board, move)
                    if points >= max_points:
                        best_move = move
                        max_points = points
                    board.revert_move(move)

        return best_move
