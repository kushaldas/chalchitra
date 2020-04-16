
# Chalchitra

A small Python module to help creating GUI based tests, using mouse clicks and
keyboard typing. This is built on top of the excellent
[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest) module.


## Dependency

On Debian

```
sudo apt-get install libopencv-dev
```

On Fedora

```
sudo dnf install opencv -y
```

Create the virtualenv and install from source.

```
python3 -m venv venv
source venv/bin/activate
python3 setup.py sdist
python3 -m pip install dist/chalchitra-0.2.0.tar.gz
```


## Usage guide

Please have a look at the [documentation](https://chalchitra.readthedocs.io/en/latest/usage.html).
