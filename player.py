import input_handler as ih
import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wager = 0
        self.has_buzzed_in = False
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

    def make_wager(self, key):
        print(f"Daily Double Key Pressed: {key}")
        self.input_handler.make_wager(key)
        self.wager = int(self.input_handler.current_wager) if self.input_handler.current_wager.isdigit() else 0
        if len(self.input_handler.current_wager) > 6 and self.input_handler.current_wager[-7:] == (":Return"):
            self.wager = int(self.input_handler.current_wager[:-7])
            self.input_handler.current_wager = ""
        print(self.wager)


        

