# Class for printing board
class BoardPrinter(object):
    def print(self, board, player1, player2):
        # String length of the biggest index (e.g. 3 for '100')
        size_length = len(str(board.size()))

        # Column indexes
        for i in range(0, size_length):
            print(' ' * size_length + ' ' + ''.join(str(n).rjust(size_length, ' ')[i] for n in range(0, board.size())))

        # Top border
        print(' ' * size_length + '-' * (board.size() + 2))

        # Rows
        for i, row in enumerate(board.fields()):
            # Row index and left border
            print(str(i).rjust(size_length, ' ') + '|', end='')

            # Row fields
            for field in row:
                print(self._print_field(field, player1, player2), end='')

            # Right border
            print('|')

        # Bottom border
        print(' ' * size_length + '-' * (board.size() + 2))
        print('Player1: %d' % player1.points())
        print('Player2: %d' % player2.points())

    def _print_field(self, field, player1, player2):
        if field.player() is player1:
            return 'O'

        if field.player() is player2:
            return 'X'

        return ' '
