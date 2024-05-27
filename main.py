import pyautogui
import time
import secrets
import tkinter as tk
from tkinter import messagebox

class MovementSimulator:
    LEFT_KEY = 'a'
    RIGHT_KEY = 'd'
    UP_KEY = 'w'
    DOWN_KEY = 's'
    TIME_PER_SPACE = 0.20
    TIME_TO_TURN = 0.12

    def __init__(self):
        self.direction_facing = 'D'

    def random_delay(self, min_delay=-10, max_delay=10):
        """Generate a cryptographically secure random delay between min_delay and max_delay seconds."""
        return min_delay + (max_delay - min_delay) * secrets.SystemRandom().random()

    def wait(self, min_wait=0, max_wait=10):
        """Wait a random number of seconds between min_wait and max_wait."""
        time.sleep(self.random_delay(min_wait, max_wait))

    def move(self, direction_key, direction_char, spaces=1):
        """Move in a specified direction a certain number of spaces."""
        turn_time = self.TIME_TO_TURN if self.direction_facing != direction_char else 0
        pyautogui.keyDown(direction_key)
        time.sleep(self.TIME_PER_SPACE * spaces + self.random_delay(-0.02, 0.02) + turn_time)
        pyautogui.keyUp(direction_key)
        time.sleep(self.random_delay(0.1, 0.2))  # Small randomized delay after moving
        self.direction_facing = direction_char

    def move_left(self, spaces=1):
        """Move left a certain number of spaces."""
        self.move(self.LEFT_KEY, 'L', spaces)

    def move_right(self, spaces=1):
        """Move right a certain number of spaces."""
        self.move(self.RIGHT_KEY, 'R', spaces)

    def move_up(self, spaces=1):
        """Move up a certain number of spaces."""
        self.move(self.UP_KEY, 'U', spaces)

    def move_down(self, spaces=1):
        """Move down a certain number of spaces."""
        self.move(self.DOWN_KEY, 'D', spaces)

    def run_back_and_forth(self):
        """Randomly run back and forth continuously staying within 3 spaces of the original position."""
        step_right = 0
        while True:
            step_left = secrets.choice([0, 1, 2, 3])
            self.move_left(step_left + step_right)
            step_right = secrets.choice([0, 1, 2, 3])
            self.move_right(step_right + step_left)

    def follow_path(self):
        """Run between the PC and the PokeMart in Viridian City."""
        while True:
            dx1 = secrets.choice([-1, 0, 0, 0, 1])
            dy1 = secrets.choice([-1, 0, 0, 0, 1])
            self.move_down(5)
            self.wait(2, 2.5)
            self.move_right(5 + dx1)
            self.move_up(6 + dy1)
            self.move_right(5 - dx1)
            self.move_up(2 - dy1)
            self.wait(2, 2.5)
            self.move_up(4)

            dx2 = secrets.choice([-1, 0, 0, 0, 1])
            dy2 = secrets.choice([-1, 0, 0, 0, 1])
            self.move_down(5)
            self.wait(2, 2.5)
            self.move_left(5 + dx2)
            self.move_down(8 + dy2)
            self.move_left(5 - dx2)
            self.move_up(2 - dy2)
            self.wait(2, 2.5)
            self.move_up(4)

class Menu:
    def __init__(self, root):
        self.simulator = MovementSimulator()
        self.root = root
        self.root.title("Movement Simulator Menu")

        self.label = tk.Label(root, text="Select an option:")
        self.label.pack()

        self.run_back_and_forth_button = tk.Button(root, text="Run back and forth", command=self.run_back_and_forth)
        self.run_back_and_forth_button.pack()

        self.follow_path_button = tk.Button(root, text="Follow path", command=self.follow_path)
        self.follow_path_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def run_back_and_forth(self):
        """Start running back and forth simulation."""
        self.show_message("Starting 'Run back and forth' in 5 seconds. Press OK to stop.")
        time.sleep(5)
        try:
            self.simulator.run_back_and_forth()
        except KeyboardInterrupt:
            self.show_message("Run back and forth stopped by user.")

    def follow_path(self):
        """Start following path simulation."""
        self.show_message("Starting 'Follow path' in 5 seconds. Press OK to stop.")
        time.sleep(5)
        try:
            self.simulator.follow_path()
        except KeyboardInterrupt:
            self.show_message("Follow path stopped by user.")

    def show_message(self, message):
        """Show a message box."""
        messagebox.showinfo("Information", message)

if __name__ == "__main__":
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()
