import os
import time
import pyautogui

DIRECTORY = ""


def a_setup(dirpath):
    """Setup the directory path where we look for any screenshot"""
    global DIRECTORY
    DIRECTORY = dirpath


def a_click(image: str, confidence=0.9, clicks=1, button="left", grayscale=False):
    """Finds a given image. One can reduce the confidence if having trouble
    to match the image.

    :param image: Name of the image without the .png extension
    :param confidence: Default value is 0.9
    :param clicks: number of clicks, default 1

    :returns: True on success, False on error
    """
    global DIRECTORY
    filepath = os.path.join(DIRECTORY, f"{image}.png")
    if not os.path.exists(filepath):
        Exception("Screenshot not found on disk.")

    try:
        x, y, = pyautogui.locateCenterOnScreen(
            filepath, confidence=confidence, grayscale=grayscale
        )
        pyautogui.click(x, y, clicks, button=button)
    except (pyautogui.PyAutoGUIException, TypeError):
        return False

    return True


def a_doubleclick(image: str, confidence=0.9):
    """Double clicks with the left mouse button.

    :param image: Name of the image without .png extension
    :param confidence: Default value is 0.9

    :returns: True on success, False on error
    """
    a_click(image, confidence=confidence, clicks=2)
