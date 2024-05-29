import pyautogui
import time
import random
from enum import Enum

# Constants
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
UP_KEY = 'w'
DOWN_KEY = 's'
TIME_PER_SPACE = 0.20
TIME_TO_TURN = 0.12

class Direction(Enum):
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'

DIRECTION_FACING = Direction.DOWN

def wait(min_wait=0, max_wait=0.1):
    """Wait for a random number of seconds between min_wait and max_wait."""
    time.sleep(random.uniform(min_wait, max_wait))

def move(direction_key, direction_enum, spaces=1):
    """Move in a specified direction a certain number of spaces."""
    global DIRECTION_FACING
    turn_time = TIME_TO_TURN if DIRECTION_FACING != direction_enum else 0
    pyautogui.keyDown(direction_key)
    time.sleep(TIME_PER_SPACE * spaces + random.uniform(-0.01, 0.01) + turn_time)
    pyautogui.keyUp(direction_key)
    wait(0, 0.1)
    DIRECTION_FACING = direction_enum

def move_left(spaces=1):
    """Move left a certain number of spaces."""
    move(LEFT_KEY, Direction.LEFT, spaces)

def move_right(spaces=1):
    """Move right a certain number of spaces."""
    move(RIGHT_KEY, Direction.RIGHT, spaces)

def move_up(spaces=1):
    """Move up a certain number of spaces."""
    move(UP_KEY, Direction.UP, spaces)

def move_down(spaces=1):
    """Move down a certain number of spaces."""
    move(DOWN_KEY, Direction.DOWN, spaces)

def run_back_and_forth():
    """Randomly run back and forth continuously staying within 3 spaces of the original position."""
    step_right = 0
    while True:
        step_left = random.choice([0, 1, 2, 3])
        move_left(step_left + step_right)
        step_right = random.choice([0, 1, 2, 3])
        move_right(step_right + step_left)

def follow_path():
    """Run between the PC and the PokeMart in Viridian City."""
    while True:
        run_to_poke_mart()
        run_to_pc()

def run_to_poke_mart():
    """Run to PokeMart using various routes."""
    dx1 = random.choice([-1, 0, 0, 0, 1])
    dy1 = random.choice([-1, 0, 0, 0, 1])
    move_down(5)
    wait(2, 2.5)
    move_right(5 + dx1)
    move_up(6 + dy1)
    move_right(5 - dx1)
    move_up(2 - dy1)
    wait(2, 2.5)
    move_up(4)

def run_to_pc():
    """Run to PC using various routes."""
    dx2 = random.choice([-1, 0, 0, 0, 1])
    dy2 = random.choice([-1, 0, 0, 0, 1])
    move_down(5)
    wait(2, 2.5)
    move_left(5 + dx2)
    move_down(8 + dy2)
    move_left(5 - dx2)
    move_up(2 - dy2)
    wait(2, 2.5)
    move_up(4)

def locate_pokemon_on_screen(pokemon_images, confidence=0.99):
    """Locate any of the specified Pokémon images on the screen."""
    for pokemon, image in pokemon_images.items():
        try:
            if pyautogui.locateOnScreen(image, confidence=confidence,region=(0,0,700,400)):
                return pokemon
        except pyautogui.ImageNotFoundException:
            pass
    return None

def check_for_pokemon(pokemon_images, timeout=2):
    """Check for a Pokémon within the specified timeout period."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        pokemon = locate_pokemon_on_screen(pokemon_images)
        if pokemon:
            print(f"You are facing a {pokemon}!")
            return pokemon
        time.sleep(0.01)
        print("Checking...")
    print("No pokemon found.")
    return None

def pokemon_still_alive(pokemon_images, min_alive_time=2):
    """Check if the Pokémon is still alive within the specified time limit."""
    start_time = time.time()
    while time.time() - start_time < min_alive_time:
        if locate_pokemon_on_screen(pokemon_images):
            return True
        time.sleep(0.1)
    return False

def fight_pokemon():
    """Initiate the fight sequence by selecting 'fight' and the first move."""
    pyautogui.press('e')  # Select 'fight'
    wait(0.1, 0.2)
    pyautogui.press('e')  # Select the first move

def run_through_grass():
    """Run back and forth in the grass."""
    step_right = 0
    for _ in range(1):
        step_left = random.choice([2, 3])
        move_left(step_left + step_right)
        step_right = random.choice([2, 3])
        move_right(step_right + step_left)

def xp_grind():
    """XP Grind"""
    pokemon_images = {
        #"Rattata": "screenshots/3.png",
        #"Mankey": "screenshots/4.png",
        #"HP Bar": "screenshots/7.png",
        "Ponyta": "screenshots/8.png",
        "Rattata": "screenshots/9.png",
        "Spearrow": "screenshots/10.png",
        "Mankey": "screenshots/11.png",
        "Nidoran Male": "screenshots/12.png",
        "Nidoran Female": "screenshots/13.png",
        "DuDuo":"screenshots/14.png"
    }
    
    while True:
        run_through_grass()
        found_pokemon = check_for_pokemon(pokemon_images)
        if found_pokemon:
                while pokemon_still_alive(pokemon_images):
                    fight_pokemon()
                    wait(3, 4)  # Wait between attacks to ensure move execution
                print(f"Defeated {found_pokemon}!")

def main_menu():
    """Display the main menu and prompt the user to select an option."""
    options = {
        "1": ("Run back and forth", run_back_and_forth),
        "2": ("Follow path", follow_path),
        "3": ("XP Grind", xp_grind),
        "4": ("Exit", None)
    }

    while True:
        print("Select an option:")
        for key, (description, _) in options.items():
            print(f"{key}. {description}")

        choice = input("Enter your choice: ")

        if choice in options:
            if choice == "4":
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
