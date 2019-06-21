# Class representing player
class Player(object):
    def __init__(self, strategy):
        self._strategy = strategy
        self._points = 0

    # Returns user's points
    def points(self):
        return self._points

    # Adds points
    def add_points(self, points):
        self._points += points

    # Get user's move for current board using his strategy
    def move(self, board, other_player):
        return self._strategy.move(board, self, other_player)
