from game.board import Board
from game.points_calculator import PointsCalculator


# Game engine class
class Game(object):
    def __init__(self, size, player1, player2, board_printer):
        self._board = Board(size)
        self._player1 = player1
        self._player2 = player2
        self._current_player = player1
        self._other_player = player2
        self._board_printer = board_printer

    # Runs the game
    def play(self):
        # Next move until the game is finished
        while not self._is_finished():
            # Get user's move using his strategy
            move = self._current_player.move(self._board, self._other_player)

            # Apply move to the board
            self._board.apply_move(move, self._current_player)

            # Add points to the user
            self._current_player.add_points(PointsCalculator.calculate(self._board, move))

            # Print the board
            self._board_printer.print(self._board, self._player1, self._player2)

            # Switch players
            [self._current_player, self._other_player] = [self._other_player, self._current_player]

    # Checks if game is finished (there are no empty fields left)
    def _is_finished(self):
        return self._board.count_empty_fields() == 0
