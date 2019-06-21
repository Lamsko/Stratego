# Class for calculating points for given move on a board
class PointsCalculator(object):
    @staticmethod
    def calculate(board, move):
        # Total points for a move is a sum of points from lines: horizontal, vertical and both diagonals
        return PointsCalculator._calculate_line(board, move, 0, 1) + PointsCalculator._calculate_line(board, move, 1, 0) + PointsCalculator._calculate_line(board, move, 1, 1) + PointsCalculator._calculate_line(board, move, 1, -1)

    # Calculates points for a single line
    # dr - how row changes for the line
    # dc - how column changes for the line
    # i.e. dr = 1, dc = -1 means that the lines is right diagonal '/'
    @staticmethod
    def _calculate_line(board, move, dr, dc):
        row = move.row()
        column = move.column()

        # Go to the beginning of the line
        while PointsCalculator._is_on_board(board, row - dr, column - dc):
            row -= dr
            column -= dc

        # Iterate through the line
        points = 0
        fields_in_line = 0
        while PointsCalculator._is_on_board(board, row, column):
            if board.is_field_used(row, column):
                # Add point if field is occupied
                points += 1
            else:
                # 0 points for line which is not finished
                return 0

            # Move to the next field
            row += dr
            column += dc
            fields_in_line += 1

        # We do not give points for single fields in the corners
        if fields_in_line == 1:
            return 0

        return points

    # Checks if given coordinates are contained on board
    @staticmethod
    def _is_on_board(board, x, y):
        return 0 <= x < board.size() and 0 <= y < board.size()
