import board
import player as jp
import input_handler as ih
import tkinter as tk
import random

class Game:
    def __init__(self, question_set):
        self.board = board.JeopardyBoard(question_set)
        self.players = []
        self.current_player_index = -1
        self.num_players = 0

    def add_player(self, player_name):
        player = jp.Player(player_name)
        self.players.append(player)
        self.num_players += 1

    def start_game(self):
        self.current_player_index = random.randint(0, self.num_players - 1)
        self.players[self.current_player_index].is_turn = True
        self.board.current_player = self.players[self.current_player_index]

        self.board.root.after(100, self.board.update_board_display())
        self.board.root.mainloop()

if __name__ == "__main__":
    question_set = "questions.jeo"
    player1 = jp.Player("Player 1")
    player2 = jp.Player("Player 2")
    jeopardy_game = Game(question_set)
    jeopardy_game.add_player(player1.name)
    jeopardy_game.add_player(player2.name)
    jeopardy_game.start_game()