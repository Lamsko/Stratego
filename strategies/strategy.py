# Abstract strategy class
class Strategy(object):
    def move(self, board, player, other_player):
        raise NotImplementedError()
