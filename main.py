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

def move_left(spaces=1):
    """Move left a certain number of spaces."""
    global DIRECTION_FACING
    turn_time = TIME_TO_TURN
    if DIRECTION_FACING == 'L':
        turn_time = 0
    pyautogui.keyDown(LEFT_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.02, 0.02) + turn_time)
    pyautogui.keyUp(LEFT_KEY)
    time.sleep(random_delay(0.1, 0.2))  # Small randomized delay after moving
    DIRECTION_FACING = 'L'

def move_right(spaces=1):
    """Move right a certain number of spaces."""
    global DIRECTION_FACING
    turn_time = TIME_TO_TURN
    if DIRECTION_FACING == 'R':
        turn_time = 0
    pyautogui.keyDown(RIGHT_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.02, 0.02) + turn_time)
    pyautogui.keyUp(RIGHT_KEY)
    time.sleep(random_delay(0.1, 0.2))  # Small randomized delay after moving
    DIRECTION_FACING = 'R'

def move_up(spaces=1):
    """Move up a certain number of spaces."""
    global DIRECTION_FACING
    turn_time = TIME_TO_TURN
    if DIRECTION_FACING == 'U':
        turn_time = 0
    pyautogui.keyDown(UP_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.02, 0.02) + turn_time)
    pyautogui.keyUp(UP_KEY)
    time.sleep(random_delay(0.1, 0.2))  # Small randomized delay after moving
    DIRECTION_FACING = 'U'

def move_down(spaces=1):
    """Move down a certain number of spaces."""
    global DIRECTION_FACING
    turn_time = TIME_TO_TURN
    if DIRECTION_FACING == 'D':
        turn_time = 0
    pyautogui.keyDown(DOWN_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.02, 0.02) + turn_time)
    pyautogui.keyUp(DOWN_KEY)
    time.sleep(random_delay(0.1, 0.2))  # Small randomized delay after moving
    DIRECTION_FACING = 'D'

def run_back_and_forth():
    """Run back and forth about 5 spaces continuously."""
    move_right(2)
    while True:
        extra_step = secrets.choice([-1, 0, 0, 0, 1])
        move_left(5 + extra_step)
        move_right(5 - extra_step)

def follow_path():
    """Run between the PC and the PokeMart in Viridian City"""
    while True:
        dx1 = secrets.choice([-1, 0, 0, 0, 1])
        dy1 = secrets.choice([-1, 0, 0, 0, 1])
        move_down(5)
        wait(2, 2.5)
        move_right(5 + dx1)
        move_up(6 + dy1)
        move_right(5 - dx1)
        move_up(2 - dy1)
        wait(2,2.5)
        move_up(4)

        dx2 = secrets.choice([-1, 0, 0, 0, 1])
        dy2 = secrets.choice([-1, 0, 0, 0, 1])
        move_down(5)
        wait(2, 2.5)
        move_left(5 + dx2)
        move_down(8 + dy2)
        move_left(5 - dx2)
        move_up(2 - dy2)
        wait(2,2.5)
        move_up(4)

def follow_up():
    move_up(1)
    wait(2, 2.5)
    move_up(4)

def main_menu():
    """Display the main menu and prompt the user to select an option."""
    print("Select an option:")
    print("1. Run back and forth")
    print("2. Follow path")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Starting the back-and-forth bot in 5 seconds. Press Ctrl+C to stop.")
        time.sleep(5)
        try:
            run_back_and_forth()
        except KeyboardInterrupt:
            print("Bot stopped by user.")
    elif choice == '2':
        print("Following the specified path in 5 seconds. Press Ctrl+C to stop.")
        time.sleep(5)
        try:
            follow_path()
        except KeyboardInterrupt:
            print("Path following stopped by user.")
    elif choice == '3':
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()