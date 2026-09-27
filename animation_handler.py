import tkinter as tk

_BOARD_COLOR = "#0000FF"
_QUESTION_TEXT_COLOR = "#FFFFFF"
_VALUE_TEXT_COLOR = "#FFCC00"
_VALUE_TEXT_OUTLINE_COLOR = "#000000"

class FadeInHandler(tk.Label):
    def __init__(self, master, text, start_color=_BOARD_COLOR, end_color=_QUESTION_TEXT_COLOR, duration=1000, steps=30, **kwargs):
        super().__init__(master, text=text, fg=start_color, **kwargs)

        self.start_color = start_color
        self.end_color = end_color
        self.duration = duration
        self.steps = steps
        self.current_step = 0

        # Parse hex colors to RGB tuples
        self.r1, self.g1, self.b1 = self.hex_to_rgb(self.start_color)
        self.r2, self.g2, self.b2 = self.hex_to_rgb(self.end_color)

        # Calculate the delay between each step in milliseconds
        self.step_delay = self.duration // self.steps

    def hex_to_rgb(self, hex_color):
        hex_str = hex_color.lstrip('#')
        return tuple(int(hex_str[i:i + 2], 16) for i in (0, 2, 4))

    def start_fade(self):
        # Interpolate the RGB values based on the current step
        if self.current_step < self.steps:
            alpha = self.current_step / self.steps
            r = int(self.r1 + (self.r2 - self.r1) * alpha)
            g = int(self.g1 + (self.g2 - self.g1) * alpha)
            b = int(self.b1 + (self.b2 - self.b1) * alpha)

            # Convert the RGB values back to a hex color string
            current_hex = f"#{r:02x}{g:02x}{b:02x}"

            # Apply color and queue next step
            self.config(fg=current_hex)
            self.current_step += 1
            self.after(self.step_delay, self.start_fade)
            
