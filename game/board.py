from game.field import Field


# Class representing game board
class Board(object):
    def __init__(self, size):
        self._size = size
        self._fields = [x[:] for x in [[Field(None)] * size] * size]

    # Returns board size (side length)
    def size(self):
        return self._size

    # Returns board fields (two dimensional list)
    def fields(self):
        return self._fields

    # Checks whether field is occupied by player
    def is_field_used(self, row, column):
        return self._fields[row][column].is_used()

    # Occupies field with move
    def apply_move(self, move, player):
        if self.is_field_used(move.row(), move.column()):
            raise Exception('Invalid move')

        self._fields[move.row()][move.column()] = Field(player)

    # Reverts given move
    def revert_move(self, move):
        self._fields[move.row()][move.column()] = Field(None)

    # Returns number of fields which are not occupied
    def count_empty_fields(self):
        return sum([sum([not field.is_used() for field in row]) for row in self._fields])
