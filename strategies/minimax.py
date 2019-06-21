from game.move import Move
from game.points_calculator import PointsCalculator
from math import inf
from strategies.strategy import Strategy


# Minimax strategy
class Minimax(Strategy):
    def __init__(self, max_depth):
        self._max_depth = max_depth

    def move(self, board, player, other_player):
        (points, move) = self._alpha_beta(board, player, other_player, True, self._max_depth)

        return move

    def _alpha_beta(self, board, player, other_player, maximizing_player, depth):
        best_move = None
        max_points = -inf

        # Return if there are no empty fields left
        if board.count_empty_fields() == 0:
            return 0, None

        # Return if max depth is reached
        if depth == 0:
            return 0, None

        # For each empty field
        for row in range(0, board.size()):
            for column in range(0, board.size()):
                if not board.is_field_used(row, column):
                    # Calculate points for move
                    move = Move(row, column)
                    board.apply_move(move, player)
                    (deeper_points, deeper_move) = self._alpha_beta(board, other_player, player, not maximizing_player, depth - 1)
                    points = PointsCalculator.calculate(board, move) + deeper_points

                    # Check if it's best move
                    if points > max_points:
                        max_points = points
                        best_move = move

                    # Revert move to check others
                    board.revert_move(move)

        if maximizing_player:
            # Return positive points if it's maximizing player
            return max_points, best_move
        else:
            # Return negative points if it's minimizing player
            return -max_points, best_move
