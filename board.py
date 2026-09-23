import tkinter as tk
from pathlib import Path
import input_handler as ih

_EMPTY = " "
_NUMBER_OF_CATEGORIES = 6
_NUMBER_OF_QUESTIONS = 5
_BOARD_WIDTH = 1500
_BOARD_HEIGHT = 800
_BOARD_COLOR = "blue"
_BOARD_DIMENSIONS = str(_BOARD_WIDTH) + "x" + str(_BOARD_HEIGHT)
_RECTANGLE_WIDTH = _BOARD_WIDTH / _NUMBER_OF_CATEGORIES
_RECTANGLE_HEIGHT = _BOARD_HEIGHT / (_NUMBER_OF_QUESTIONS + 1)  # +1 for category row

class JeopardyBoard:
    def __init__(self, question_set):
        self.question_set = Path(__file__).with_name(question_set)
        self.board = [[_EMPTY for _ in range(_NUMBER_OF_QUESTIONS + 1)] for _ in range(_NUMBER_OF_CATEGORIES)]
        self.questions = []
        self.answers = []
        self.categories = []
        self.values = []
        self.selected_category_index = -1
        self.selected_question_index = -1
        self.selected_question = {"question": "", "answer": "", "value": 0}
        self.question_window = None
        self.question_is_selected = False

    def initialize_board(self):
        # Read data from the file
        with open(self.question_set, "r") as questions_file:
            for line in questions_file.readlines():
                if not line.strip(): # Skip empty lines
                    continue
                if line.strip().startswith("Q:"): # Pulls out question lines
                    self.questions.append(line.rsplit(":", 1)[1].strip())
                elif line.strip().startswith("A:"): # Pulls out answer lines
                    self.answers.append(line.rsplit(":", 1)[1].strip())
                elif line.strip().startswith("C:"): # Pulls out category lines
                    self.categories.append(line.rsplit(":", 1)[1].strip())
                elif line.strip().startswith("V:"): # Pulls out value lines
                    self.values.append(int(line.rsplit(":", 1)[1].strip()))
                else:
                    continue

        for i in range(_NUMBER_OF_CATEGORIES):
            self.board[i][0] = self.categories[i]  # Set category names in the first column
            for j in range(1, _NUMBER_OF_QUESTIONS + 1):
                self.board[i][j] = {"question": self.questions[i * _NUMBER_OF_QUESTIONS + j - 1],
                                    "answer": self.answers[i * _NUMBER_OF_QUESTIONS + j - 1],
                                    "value": self.values[i * _NUMBER_OF_QUESTIONS + j - 1]}

    def handle_key_press(self, event):
        input_handler = ih.InputHandler()

        if self.question_is_selected:
            if event.keysym == "Return":  # If Enter is pressed, show the answer
                self.display_answer()
            elif event.keysym == "Escape":  # If Escape is pressed, close the question window
                if self.question_window:
                    self.question_window.destroy()
                    self.question_is_selected = False
        else:
            current_selection = input_handler.handle_key_press(event.keysym)
            self.selected_category_index = current_selection[0]
            self.selected_question_index = current_selection[1]
            self.select_question(self.selected_category_index, self.selected_question_index)
            self.question_is_selected = True
            print(f"Selected Category: {self.selected_category_index}, Selected Question: {self.selected_question_index}")
            self.display_question()

    def display_board(self):
        # Create the main window
        root = tk.Tk()
        root.title("Jeopardy Board")
        root.geometry(_BOARD_DIMENSIONS)
        root.configure(bg=_BOARD_COLOR)
        root.bind("<Key>", self.handle_key_press)
        canvas = tk.Canvas(root, width=_BOARD_WIDTH, height=_BOARD_HEIGHT, bg=_BOARD_COLOR)
        canvas.pack()
        for i in range(_NUMBER_OF_CATEGORIES):
            for j in range(_NUMBER_OF_QUESTIONS + 1):  # +1 for category row
                x0 = i * _RECTANGLE_WIDTH
                y0 = j * _RECTANGLE_HEIGHT
                x1 = x0 + _RECTANGLE_WIDTH
                y1 = y0 + _RECTANGLE_HEIGHT
                canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="blue", width=3)
                if j == 0:  # Category row
                    canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=self.board[i][j], fill="white", font=("Arial", 20))
                else:  # Question rows
                    canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=f"${self.board[i][j]['value']}", fill="white", font=("Arial", 20))
        root.mainloop()

    def select_question(self, category_index, question_index):
        self.selected_category_index = category_index
        self.selected_question_index = question_index
        self.selected_question = self.board[category_index][question_index + 1]  # +1 to skip the category name

    def display_question(self):
        self.question_window = tk.Toplevel()
        self.question_window.title("Question")
        self.question_window.geometry(_BOARD_DIMENSIONS)
        self.question_window.configure(bg=_BOARD_COLOR)
        question_label = tk.Label(self.question_window, text=self.selected_question["question"], bg=_BOARD_COLOR, fg="white", font=("Arial", 40), wraplength=1000, justify="center")
        question_label.pack(pady=150)
        self.question_window.bind("<Key>", self.handle_key_press)

    def display_answer(self):
        answer_label = tk.Label(self.question_window, text=self.selected_question["answer"], bg=_BOARD_COLOR, fg="white", font=("Arial", 40), wraplength=1000, justify="center")
        answer_label.pack(pady=20)

if __name__ == "__main__":
    question_set = "questions.jeo"
    jeopardy_board = JeopardyBoard(question_set)
    jeopardy_board.initialize_board()
    jeopardy_board.select_question(0, 1)  # Select the first question in the second category
    jeopardy_board.display_board()
    #jeopardy_board.display_question()
    #print(jeopardy_board.board[1][1]["question"])  # Print the first question
    #print(jeopardy_board.board)