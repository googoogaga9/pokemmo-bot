import pyautogui
import time
import secrets

# Define constants for the movement keys
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
UP_KEY = 'w'
DOWN_KEY = 's'

# Define the time it takes to move one space when facing the direction
TIME_PER_SPACE = 0.20
# The time it takes to turn the character to face the correct direction
TIME_TO_TURN = 0.12
# Direction the character is facing
DIRECTION_FACING = 'D'

def random_delay(min_delay=-10, max_delay=10):
    """Generate a cryptographically secure random delay between min_delay and max_delay seconds."""
    return min_delay + (max_delay - min_delay) * secrets.SystemRandom().random()

def wait(min_wait=0, max_wait=10):
    """Wait a random number of seconds between min_wait and max_wait."""
    time.sleep(random_delay(min_wait, max_wait))

def move(direction_key, direction_char, spaces=1):
    """Move in a specified direction a certain number of spaces."""
    global DIRECTION_FACING
    turn_time = TIME_TO_TURN if DIRECTION_FACING != direction_char else 0
    pyautogui.keyDown(direction_key)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.02, 0.02) + turn_time)
    pyautogui.keyUp(direction_key)
    time.sleep(random_delay(0.1, 0.2))  # Small randomized delay after moving
    DIRECTION_FACING = direction_char

def move_left(spaces=1):
    """Move left a certain number of spaces."""
    move(LEFT_KEY, 'L', spaces)

def move_right(spaces=1):
    """Move right a certain number of spaces."""
    move(RIGHT_KEY, 'R', spaces)

def move_up(spaces=1):
    """Move up a certain number of spaces."""
    move(UP_KEY, 'U', spaces)

def move_down(spaces=1):
    """Move down a certain number of spaces."""
    move(DOWN_KEY, 'D', spaces)

def run_back_and_forth():
    """Randomly run back and forth continuously staying within 3 spaces of the original position."""
    step_right = 0
    while True:
        step_left = secrets.choice([0, 1, 2, 3])
        move_left(step_left + step_right)
        step_right = secrets.choice([0, 1, 2, 3])
        move_right(step_right + step_left)

def follow_path():
    """Run between the PC and the PokeMart in Viridian City."""
    while True:
        dx1 = secrets.choice([-1, 0, 0, 0, 1])
        dy1 = secrets.choice([-1, 0, 0, 0, 1])
        move_down(5)
        wait(2, 2.5)
        move_right(5 + dx1)
        move_up(6 + dy1)
        move_right(5 - dx1)
        move_up(2 - dy1)
        wait(2, 2.5)
        move_up(4)

        dx2 = secrets.choice([-1, 0, 0, 0, 1])
        dy2 = secrets.choice([-1, 0, 0, 0, 1])
        move_down(5)
        wait(2, 2.5)
        move_left(5 + dx2)
        move_down(8 + dy2)
        move_left(5 - dx2)
        move_up(2 - dy2)
        wait(2, 2.5)
        move_up(4)

def main_menu():
    """Display the main menu and prompt the user to select an option."""
    options = {
        "1": ("Run back and forth", run_back_and_forth),
        "2": ("Follow path", follow_path),
        "3": ("Exit", None)
    }

    while True:
        print("Select an option:")
        for key, (description, _) in options.items():
            print(f"{key}. {description}")

        choice = input("Enter your choice: ")

        if choice in options:
            if choice == "3":
                print("Exiting the program.")
                break

            print(f"Starting '{options[choice][0]}' in 5 seconds. Press Ctrl+C to stop.")
            time.sleep(5)
            try:
                options[choice][1]()
            except KeyboardInterrupt:
                print(f"{options[choice][0]} stopped by user.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
