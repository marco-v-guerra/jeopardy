from pathlib import Path

class InputHandler:
    def __init__(self):
        self.current_wager = ""
        self.key_dictionary = {}

    def host_key_press(self, key):
        with open(Path(__file__).with_name("input_handler.jeo"), "r") as key_file:
            for line in key_file.readlines():
                if not line.strip():
                    continue
                self.key_dictionary[line.strip().rsplit(":", 1)[0].strip()] = line.rsplit(":", 1)[1].strip()

        return int(self.key_dictionary[key].rsplit(" ", 1)[0]), int(self.key_dictionary[key].rsplit(" ", 1)[1])

    def make_wager(self, key):
        print(f"Daily Double Key Pressed: {key}")
        if key.isdigit():
            self.current_wager += key
            print(f"Current Wager: {self.current_wager}")
        elif key == "BackSpace":
            self.current_wager = self.current_wager[:-1]

