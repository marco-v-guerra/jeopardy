import tkinter as tk

_EMPTY = " "
_NUMBER_OF_CATEGORIES = 6
_NUMBER_OF_QUESTIONS = 5

class JeopardyBoard:
    def __init__(self, question_set):
        self.question_set = question_set
        self.board = [[_EMPTY for _ in range(_NUMBER_OF_QUESTIONS + 1)] for _ in range(_NUMBER_OF_CATEGORIES)]
        self.questions = []
        self.answers = []
        self.categories = []
        self.values = []

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

    def display_board(self):
        root = tk.Tk()
        root.title("Jeopardy Board")
        root.geometry("1600x1200")
        root.configure(bg="blue")
        root.mainloop()




if __name__ == "__main__":
    question_set = "questions.jeo"
    jeopardy_board = JeopardyBoard(question_set)
    jeopardy_board.initialize_board()
    jeopardy_board.display_board()
    #print(jeopardy_board.board[1][1]["question"])  # Print the first question
    #print(jeopardy_board.board)