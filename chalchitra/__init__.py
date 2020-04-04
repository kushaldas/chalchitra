import os
import time
import pyautogui

DIRECTORY = ""


def a_setup(dirpath):
    """Setup the directory path where we look for any screenshot"""
    global DIRECTORY
    DIRECTORY = dirpath


def a_click(image: str, confidence=0.9, clicks=1, button="left"):
    """Finds a given image. One can reduce the confidence if having trouble
    to match the image.

    : param image: Name of the image without the .png extension
    : param confidence: Default value is 0.9
    : param clicks: number of clicks, default 1
    """
    global DIRECTORY
    filepath = os.path.join(DIRECTORY, f"{image}.png")
    if not os.path.exists(filepath):
        Exception("Screenshot not found on disk.")

    try:
        x, y, = pyautogui.locateCenterOnScreen(filepath, confidence=confidence)
        pyautogui.click(x, y, clicks, button=button)
    except pyautogui.PyAutoGUIException:
        raise Exception("Could not find the screenshot on screen.")
