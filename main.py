import pyautogui
import time
import secrets

# Define constants for the movement keys
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
UP_KEY = 'w'
DOWN_KEY = 's'

# Define the time it takes to move one space
TIME_PER_SPACE = 0.22

def random_delay(min_delay=-10, max_delay=10):
    """Generate a cryptographically secure random delay between min_delay and max_delay seconds."""
    return min_delay + (max_delay - min_delay) * secrets.SystemRandom().random()

def wait(min_wait=0, max_wait=10):
    """Wait a random number of seconds between min_wait and max_wait."""
    time.sleep(random_delay(min_wait, max_wait))

def move_left(spaces=1):
    """Move left a certain number of spaces."""
    pyautogui.keyDown(LEFT_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.05, 0.05))
    pyautogui.keyUp(LEFT_KEY)
    time.sleep(random_delay(0.1, 0.5))  # Small randomized delay after moving

def move_right(spaces=1):
    """Move right a certain number of spaces."""
    pyautogui.keyDown(RIGHT_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.05, 0.05))
    pyautogui.keyUp(RIGHT_KEY)
    time.sleep(random_delay(0.1, 0.5))  # Small randomized delay after moving

def move_up(spaces=1):
    """Move up a certain number of spaces."""
    pyautogui.keyDown(UP_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.05, 0.05))
    pyautogui.keyUp(UP_KEY)
    time.sleep(random_delay(0.1, 0.5))  # Small randomized delay after moving

def move_down(spaces=1):
    """Move down a certain number of spaces."""
    pyautogui.keyDown(DOWN_KEY)
    time.sleep(TIME_PER_SPACE * spaces + random_delay(-0.05, 0.05))
    pyautogui.keyUp(DOWN_KEY)
    time.sleep(random_delay(0.1, 0.5))  # Small randomized delay after moving

def run_back_and_forth():
    """Run back and forth 5 spaces continuously."""
    while True:
        move_left(5)
        move_right(5)

def follow_path():
    """Run between the PC and the PokeMart in Viridian City"""
    while True:
        move_down(5)
        wait(2, 3)
        move_right(5)
        move_up(6)
        move_right(5)
        move_up(2)
        wait(2,3)
        move_up(4)

        move_down(5)
        wait(2, 3)
        move_left(5)
        move_down(7)
        move_left(5)
        move_up(1)
        wait(2,3)
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
