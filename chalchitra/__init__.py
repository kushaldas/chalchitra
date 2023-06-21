import os
import time
from datetime import datetime
from collections import namedtuple
import pyautogui

__version__ = "0.3.0"

__all__ = [
    "KEYS",
    "Point",
    "a_click",
    "a_doubleclick",
    "a_hotkey",
    "a_keydown",
    "a_keyup",
    "a_keypress",
    "a_screenshot",
    "a_setup",
    "a_typetext",
    "a_verify",
    "a_wait",
]
DIRECTORY = ""

KEYS = pyautogui.KEYBOARD_KEYS
"""KEYS contains all keyboard keys"""

Point = namedtuple("Point", ["x", "y"])


def a_setup(dirpath):
    """Setup the directory path where we look for any screenshot"""
    global DIRECTORY
    DIRECTORY = dirpath


def _find_location(image="", confidence=0.9, grayscale=False):
    """Finds a given image. One can reduce the confidence if having trouble
    to match the image.

    :param image: Name of the image without the .png extension
    :param confidence: Default value is 0.9
    :param grayscale: To search in grayscale for faster result

    :returns: False or error, or namedtuple Point
    """
    global DIRECTORY
    filepath = os.path.join(DIRECTORY, f"{image}.png")
    if not os.path.exists(filepath):
        Exception("Screenshot not found on disk.")

    try:
        x, y, = pyautogui.locateCenterOnScreen(
            filepath, confidence=confidence, grayscale=grayscale
        )
        return Point(x, y)
    except (pyautogui.PyAutoGUIException, TypeError):
        return False


def a_verify(image="", confidence=0.9, grayscale=False):
    """Verifies that a given image (screenshot) in on the screen. One can reduce the confidence if having trouble
    to match the image. Having grayscale=True will the search a bit faster.

    :param image: Name of the image without the .png extension
    :param confidence: Default value is 0.9
    :param grayscale: To search in grayscale for faster result

    :returns: True if it can find the screenshot, or else False
    """
    location = _find_location(image, confidence, grayscale)
    if not location:
        return False
    return True


def a_wait(image="", confidence=0.9, grayscale=False, timeout=10):
    """Wait till the given timeout seconds to verify that a given image (screenshot) in on the screen. One can reduce the confidence if having trouble
    to match the image. Having grayscale=True will the search a bit faster.

    :param image: Name of the image without the .png extension
    :param confidence: Default value is 0.9
    :param grayscale: To search in grayscale for faster result
    :param timeout: Timeout in seconds, 10 is the default value

    :returns: True if it can find the screenshot within the given timeout seconds, or else False
    """
    waittime = 0
    while waittime < timeout:
        ret = a_verify(image, confidence, grayscale)
        if not ret:
            waittime += 1
            time.sleep(1)
        else:
            return True
    # Could not find the screenshot in the given time
    return False


def a_click(image="", confidence=0.9, clicks=1, button="left", grayscale=False):
    """Finds a given image. One can reduce the confidence if having trouble
    to match the image. If no image is provided, then it clicks on the current place of the mouse pointer.

    :param image: Name of the image without the .png extension, if none, it will click on the current position and always returns `True` when no image name is provided.
    :param confidence: Default value is 0.9
    :param clicks: number of clicks, default 1
    :param button: "left", "middle" or "right", left button is the default one
    :param grayscale: Boolean, by default False. To search in grayscale mode for the image.

    :returns: True on success, False on error
    """
    if not image:
        pyautogui.click(clicks=clicks, button=button)
        return True
    location = _find_location(image, confidence, grayscale)
    if not location:
        return False
    pyautogui.click(location.x, location.y, clicks, button=button)

    return True


def a_doubleclick(image: str, confidence=0.9, grayscale=False):
    """Double clicks with the left mouse button.

    :param image: Name of the image without .png extension, this can be None if you want to click on the current mouse position.
    :param confidence: Default value is 0.9
    :param grayscale: Boolean, by default False. To search in grayscale mode for the image.

    :returns: True on success, False on error
    """
    return a_click(image, confidence=confidence, clicks=2, grayscale=grayscale)


def a_screenshot(filename=""):
    """Saves a screenshot and then returns the filename and the image data.

    :returns: Tuple containing the saved file path and the image data.
    """
    if not filename:
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d-%H-%M-%S.png")
    image = pyautogui.screenshot(filename)
    return filename, image


def a_typetext(text="", interval="0.01"):
    """Types the text with the given interval speed.

    :param text: String text to be typed
    :param interval: speed of typing, default is 0.01 (fast)
    """
    pyautogui.write(text, interval=interval)


def a_keypress(key=""):
    """Presses the key once (key down and then key up)

    :param key: The keyboard key to press, (see KEYS values for the full list)
    """
    pyautogui.press(key)


def a_keydown(key=""):
    """Kept pressing the given key. Remember to all a_keyup when you are down.

    :param key: The keyboard key to press, (see KEYS values for the full list)
    """
    pyautogui.keyDown(key)


def a_keyup(key=""):
    """Removes the pressure from the given key. To be used along with a a_keydown call.

    :param key: The keyboard key, (see KEYS values for the full list)
    """
    pyautogui.keyUp(key)


def a_hotkey(keys):
    """Special function to keep pressing the given keys in order, and then keyup in the reverse order.

    :param keys: A list of the keys.
    """
    pyautogui.hotkey(*keys)
