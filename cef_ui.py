# Hello world example. Doesn't depend on any third party GUI framework.
# Tested with CEF Python v57.0+.

import platform
import sys

import win32con
from cefpython3 import cefpython as cef
from winerror import ERROR_ALREADY_EXISTS

import win32gui
from win32api import GetLastError
from win32event import CreateMutex


def main():
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://www.google.com/",
                          window_title="Hello World!")
    cef.MessageLoop()
    cef.Shutdown()


if __name__ == '__main__':
    main()