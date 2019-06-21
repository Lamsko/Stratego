# Class representing single field on board
class Field(object):
    def __init__(self, player):
        self._player = player

    def player(self):
        return self._player

    # Checks whether field is occupied
    def is_used(self):
        return self._player is not None
