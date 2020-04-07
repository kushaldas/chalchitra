Usage
======


All functions from the library is starting with **a_**, this way you can still
easily use *pyautogui* inside your code if you want to.


Call a_setup first
------------------

In every code base, remember to call `a_setup` if you are using screenshots to
verify or do mouse clicks on the items on the screen. The function takes one
argument, the directory path where we store the screenshots for the project.

::

    a_setup("images")



Example to open a new tab in the terminal
------------------------------------------

In the following example, we open a new tab in the Gnome terminal, and then go to the */tmp* directory.
As we are not using any screenshot here, we skip the *a_setup* call.

::

    import time
    from chalchitra import *


    def goto_path(path=""):
        a_hotkey(["ctrl", "shift", "t"])
        time.sleep(0.5)
        a_typetext("cd {}".format(path))
        a_keypress("enter")


    if __name__ == "__main__":
        goto_path("/tmp")


In the `goto_path` function, first we are pressing a hotkey combination, the keys are passed into the
*a_hotkey* function as a list. Then we wait for 0.5 seconds for the terminal tab to open, and then
type the command using *a_typetext* function call. Finally using the *a_keypress* function we press the
`enter` key in the keyboard.

.. image:: img/terminal_goto.gif

If you want to see all the keys you can use in *a_keypress* or *a_hotkey*,
below is the list (stored in the *KEYS* variable).

::

    ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']

