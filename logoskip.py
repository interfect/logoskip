#!/usr/bin/env python3

import time
import random

import cv2
import pyautogui

def has_rings():
    """
    Determine if we can see the ring logo.
    """
    pos = pyautogui.locateOnScreen('rings.png', confidence=0.5)
    if not pos:
    	pos = pyautogui.locateOnScreen('rings2.png', confidence=0.5)
    print(f"Found at: {pos}")
    return pos is not None
    
def is_too_blank():
    """
    Determine if the screen is suspiciously blank.
    
    This will happen if we skip ahead past what is buffered, and it won't be
    fixed until we start playback again.
    """
    # We can't look for a black image or we will find it everywhere
    image = pyautogui.screenshot()
    black_count = 0
    to_sample = 300
    for i in range(to_sample):
        x = random.randint(1, image.width - 1)
        y = random.randint(1, image.height - 1)
        pixel_value = image.getpixel((x, y))
        if pixel_value == (0, 0, 0):
            black_count += 1
    
    # If too many of the pixels are black, we probably lost the video.
    blackness =  black_count / to_sample
    print("Image is {:.2f}% black".format(blackness * 100))
    return blackness > 0.5

def skip_ahead():
    """
    Skip the player ahead.
    """
    print("Skipping forward")
    pyautogui.press('l')
    time.sleep(2)
    
def toggle_video():
    """
    Pause or unpause the video.
    """
    print("Toggling video")
    pyautogui.press('k')
    
if __name__ == "__main__":
    time.sleep(3)
    while True:
        if not has_rings():
            print("Logo missing.")
            time.sleep(0.5)
            # This may be a commercial
            if not has_rings():
                print("Logo still missing. Scanning for logo...")
                # Probably a commercial
                
                # Stop the video
                toggle_video()
                
                while not has_rings():
                    skip_ahead()
                    if is_too_blank():
                        # We need to get the video back
                        print("Video has gone away")
                        toggle_video()
                        while is_too_blank():
                            # We need to get the video back
                            time.sleep(2)
                        print("Video has come back")
                        toggle_video()
                print("Logo is back.")
                
                toggle_video()
        # Wait a bit to not hammer the system.
        time.sleep(2)
