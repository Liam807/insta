from tkinter.constants import TRUE
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


def autoMessage():
    checkColor = (pyautogui.pixel(590, 974)[0] == 239 or pyautogui.pixel(589,965)[0] == 239)
    cont = 3
    print(cont)
    if keyboard.is_pressed('-'):
        cont = 1
    if checkColor == False and cont != 1:
        print(checkColor)
    if checkColor == True and cont != 1:
        pyautogui.moveTo(612, 1014, 0)
        click(612, 1014)
        keyboard.write('sup')




# makes it click
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



        


