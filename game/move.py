# Class representing single move
class Move(object):
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def row(self):
        return self._row

    def column(self):
        return self._column
