import input_handler as ih
import tkinter as tk

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.wager = 0
        self.has_buzzed_in = False
        self.is_turn = False

    def reset_for_new_round(self):
        self.wager = 0
        self.has_buzzed_in = False

    def correct_answer(self, value):
        self.score += value
        self.is_turn = True

    def incorrect_answer(self, value):
        self.score -= value

    def get_wager(self, event):
        input_handler = ih.InputHandler()
        while event.keysym != "Return":
            wager = input_handler.get_wager(event.keysym)
            if wager is not None:
                self.wager = wager
                break

        return self.wager

