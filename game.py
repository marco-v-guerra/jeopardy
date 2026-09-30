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
        self.buzzers = []

    def add_player(self, player_name, buzzer):
        player = jp.Player(player_name, buzzer)
        self.players.append(player)
        self.buzzers.append(buzzer)
        self.num_players += 1

    def start_game(self):
        self.current_player_index = random.randint(0, self.num_players - 1)
        self.players[self.current_player_index].is_turn = True
        self.board.current_player = self.players[self.current_player_index]
        self.board.root.bind("<Key>", self.handle_key_press)

        self.board.root.after(100, self.board.update_board_display())
        self.board.root.mainloop()

    def handle_key_press(self, event):
        input_handler = ih.InputHandler()
    
        if self.board.question_is_selected:
            if self.board.daily_double_is_selected:
                if not self.board.daily_double_wager_submitted:
                    self.handle_daily_double_key_press(event.keysym)
                    self.board.update_wager_display()
                else:
                    if event.keysym == "Return":  # If Enter is pressed, show the answer
                        self.board.display_answer()
                    elif event.keysym == "Escape":  # If Escape is pressed, close the question window
                        if self.board.question_window:
                            self.board.question_window.destroy()
                            self.board.question_is_selected = False
                            self.board.daily_double_is_selected = False
                            self.board.daily_double_wager_submitted = False
                    #elif event.keysym in self.buzzers:
                    #    index = self.buzzers.index(event.keysym)
                    #    self.buzz_in(self.players[index])
            else:
                if event.keysym == "Return":  # If Enter is pressed, show the answer
                    self.board.display_answer()
                elif event.keysym == "Escape":  # If Escape is pressed, close the question window
                    if self.board.question_window:
                        self.board.question_window.destroy()
                        self.board.question_is_selected = False
        else:
            current_selection = input_handler.host_key_press(event.keysym)
            self.board.selected_category_index = current_selection[0]
            self.board.selected_question_index = current_selection[1]
            if self.board.board[self.board.selected_category_index][self.board.selected_question_index] is not board._EMPTY:
                self.board.select_question(self.board.selected_category_index, self.board.selected_question_index)
                self.board.question_is_selected = True
                self.board.input_handler.is_question_active = True  # Set the flag to indicate that a question is active
                if self.board.selected_question["daily_double"]:
                    self.board.handle_daily_double()
                else:
                    self.board.display_question()

    def handle_daily_double_key_press(self, key):
        if key == "Escape":
            self.board.daily_double_window.destroy()
        elif key == "Return":
            wager = self.board.current_player.wager
            if wager is not None:
                self.board.current_player.wager = wager
                self.board.daily_double_wager_submitted = True
                self.board.daily_double_window.destroy()
                self.board.display_question()
        elif key.isdigit() or key == "BackSpace":
            self.board.current_player.make_wager(key)

    def create_board_display(self):
        self.board.create_board_display()
        self.board.root.bind("<Key>", self.handle_key_press)

    def display_question(self):
        self.board.display_question()
        self.board.question_window.bind("<Key>", self.handle_key_press)

    def handle_daily_double(self):
        self.board.handle_daily_double()
        self.board.daily_double_window.bind("<Key>", self.handle_key_press)

    def buzz_in(self, player):
        if player.can_buzz_in:
            player.can_buzz_in = False
            self.current_player = player


if __name__ == "__main__":
    question_set = "questions.jeo"
    jeopardy_game = Game(question_set)
    jeopardy_game.add_player("Player 1", "F1")
    jeopardy_game.add_player("Player 2", "F2")
    jeopardy_game.start_game()