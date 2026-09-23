from pathlib import Path

class InputHandler:
    def __init__(self):
        self.key_pressed = None
        self.key_dictionary = {}

    def handle_key_press(self, key):
        self.key_pressed = key
        with open(Path(__file__).with_name("input_handler.jeo"), "r") as key_file:
            for line in key_file.readlines():
                if not line.strip():
                    continue
                self.key_dictionary[line.strip().rsplit(":", 1)[0].strip()] = line.rsplit(":", 1)[1].strip()

        return int(self.key_dictionary[self.key_pressed].rsplit(" ", 1)[0]), int(self.key_dictionary[self.key_pressed].rsplit(" ", 1)[1])
