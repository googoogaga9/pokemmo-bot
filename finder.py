import dlib
import cv2
import numpy as np
import pyautogui
import time
import os

def load_images(image_paths):
    images = {}
    for name, path in image_paths.items():
        if os.path.exists(path):
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            detector = dlib.get_frontal_face_detector() # Or other appropriate detector
            images[name] = (image, detector)
        else:
            print(f"Image not found: {path}")
    return images

def check_for_pokemon():
    # Assuming gen5sprites is in the same directory as the script
    pokemon_images = {
        "Spearow": "gen5sprites/0021.png",
        "Mankey": "gen5sprites/0056.png",
        "Rattata": "gen5sprites/0019.png"
    }
    
    # Load images
    templates = load_images(pokemon_images)
    
    while True:
        screenshot = np.array(cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY))
        for pokemon, (template, detector) in templates.items():
            try:
                detected_faces = detector(screenshot, 1)
                for d in detected_faces:
                    x, y, w, h = (d.left(), d.top(), d.width(), d.height())
                    roi = screenshot[y:y+h, x:x+w]
                    result = cv2.matchTemplate(roi, template, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    if max_val >= 0.8:
                        print(f"You are facing a {pokemon}!")
                        return pokemon
            except Exception as e:
                print(f"Error processing {pokemon}: {e}")
        
        time.sleep(1)

if __name__ == "__main__":
    found_pokemon = check_for_pokemon()
    print(f"Detected Pokemon: {found_pokemon}")
