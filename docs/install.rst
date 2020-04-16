Installation
------------


Dependencies
============

On Debian

```
sudo apt-get install libopencv-dev scrot
```

On Fedora

```
sudo dnf install opencv scrot -y
```


Create a virtualenv and install Python dependencies
====================================================

::

    python3 -m venv venv
    source venv/bin/activate
    python3 setup.py sdist
    python3 -m pip install dist/chalchitra-0.2.0.tar.gz

