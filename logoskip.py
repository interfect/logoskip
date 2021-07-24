#!/usr/bin/env python3

import time

import cv2
import pyautogui

def has_rings():
    """
    Determine if we can see the ring logo.
    """
    pos = pyautogui.locateOnScreen('rings.png', confidence=0.5)
    print(f"Found at: {pos}")
    return pos is not None
    
def skip_ahead():
    """
    Skip the player ahead.
    """
    print("Skipping forward")
    pyautogui.press('l')
    time.sleep(1)
    
def toggle_video():
    """
    Pause or unpause the video.
    """
    print("Toggling video")
    pyautogui.press('k')
    
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
            print("Logo is back.")
            
            toggle_video()
