import input_handler as ih
import tkinter as tk

class Player:
    def __init__(self, name, buzzer):
        self.name = name
        self.score = 0
        self.wager = 0
        self.buzzer = buzzer
        self.can_buzz_in = True
        self.is_turn = False
        self.input_handler = ih.InputHandler()

    def reset_for_new_round(self):
        self.wager = 0
        self.has_buzzed_in = False

    def correct_answer(self, value):
        self.score += value
        self.is_turn = True

    def incorrect_answer(self, value):
        self.score -= value

    def buzz_in(self, key):
        self.can_buzz_in = False


    def make_wager(self, key):
        self.input_handler.make_wager(key)
        self.wager = int(self.input_handler.current_wager) if self.input_handler.current_wager.isdigit() else 0
        if len(self.input_handler.current_wager) > 6 and self.input_handler.current_wager[-7:] == (":Return"):
            self.wager = int(self.input_handler.current_wager[:-7])
            self.input_handler.current_wager = ""


        

