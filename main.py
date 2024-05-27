import pyautogui
import time
import secrets

# Define constants for the movement keys
LEFT_KEY = 'left'
RIGHT_KEY = 'right'

def random_delay(min_delay=0.5, max_delay=1.5):
    """Generate a cryptographically secure random delay between min_delay and max_delay seconds."""
    return min_delay + (max_delay - min_delay) * secrets.SystemRandom().random()

def random_duration(min_duration=3.5, max_duration=4.5):
    """Generate a cryptographically secure random duration between min_duration and max_duration seconds."""
    return min_duration + (max_duration - min_duration) * secrets.SystemRandom().random()

def move_left():
    """Move left for a random duration with random delays."""
    duration = random_duration()
    pyautogui.keyDown(LEFT_KEY)
    time.sleep(duration)
    pyautogui.keyUp(LEFT_KEY)
    time.sleep(random_delay(0.5, 1.0))  # Small randomized delay after moving

def move_right():
    """Move right for a random duration with random delays."""
    duration = random_duration()
    pyautogui.keyDown(RIGHT_KEY)
    time.sleep(duration)
    pyautogui.keyUp(RIGHT_KEY)
    time.sleep(random_delay(0.5, 1.0))  # Small randomized delay after moving

def run_back_and_forth():
    while True:
        # Move left for a random duration
        move_left()

        # Move right for a random duration
        move_right()

        # Add more logic if needed for waiting or additional movements
        time.sleep(random_delay(1, 3))  # Example randomized delay between actions

if __name__ == "__main__":
    print("Starting the back-and-forth bot. Press Ctrl+C to stop.")
    try:
        run_back_and_forth()
    except KeyboardInterrupt:
        print("Bot stopped by user.")