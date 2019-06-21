from console_interface.board_printer import BoardPrinter
from game.game import Game
from game.player import Player
from strategies.best_next_move import BestNextMove
from strategies.alpha_beta import AlphaBeta
from strategies.minimax import Minimax
from strategies.random_move import RandomMove
from strategies.user_input import UserInput

if __name__ == "__main__":
    # Board size
    size = 7

    # Players and their strategies
    player1 = Player(Minimax(3))
    player2 = Player(AlphaBeta(6))

    # Run the game
    game = Game(size, player1, player2, BoardPrinter())
    game.play()
