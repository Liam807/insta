from re import I
from tkinter.constants import TRUE
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def pfpClicker():
    for x in range(1000):
        Oldpfp = "pfp already used"
        orignalPic = "originalPic"
        oldPic = "Old Pic"
        newPic = "new Pic"
        staticImage = "staticImage"
        if static image != staticImage and originalPic != newPic "static image":
            click(345,247)
            "Thing thats commented out"
            
            oldpic = newPic
        




        """
        print("Typing...")
      pyautogui.moveTo(637, 1029, 0)
      click(612, 1014)
      keyboard.write(Response)
      keyboard.press_and_release('enter')
      time.sleep(.8)"""