from re import I
from tkinter.constants import TRUE
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

class ReplyBot:
 # def __init__(self):
 #  self._Action = ""

  #def setAction(self, action):
    #self._Action = action 
    
  def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#Checks if there is a message based on if there is a new message on screen
def checkColor():
  i=0
  for i in range(3):
    x=565+(2*i)
    y=943+(2*i)
    checkColor = pyautogui.pixel(x, y)[0] == (239 or 240 or 238 or 241 or 242 or 243 or 244 or 245 or 246) or pyautogui.pixel(x+1, y+1)[0] == (239 or 240 or 238 or 241 or 242 or 243 or 244 or 245 or 246)
    if checkColor == True:
      break 
  return checkColor

#Takes the input and if there is new message prints new message   
def autoMessage():
  Response = input("What would ur auto message be? ")
  counta = 2
  for x in range (999999999999999):
    if keyboard.is_pressed('a'):
      x=10001
    if (checkColor() == False and counta != 1):
      continue
    if checkColor()  == True and counta != 1:
      print("Typing...")
      pyautogui.moveTo(637, 1029, 0)
      click(612, 1014)
      keyboard.write(Response)
      keyboard.press_and_release('enter')
      time.sleep(.8)

 
autoMessage()
    

"""    
 Action = int(input("What would you like to do?"))
    
    if Action ==1:
        autoMessage(1)
        
  def checkColor():--
    for i in range(20):
      x=580+i
      y=962+i-
      bool = pyautogui.pixel(x, y)[0] == 239
      if bool == True:Peein
        break 
    return bool


Works( for i in range(20):
  x=580+i
  y=962+i
  checkColor = pyautogui.pixel(x, y)[0] == 239
  if checkColor == True:
    break 
print(checkColor)
counta = 2
print(counta)
if keyboard.is_pressed('-'):
  counta = 1
if (checkColor == False and counta != 1):
  print(bool)
if checkColor  == True and counta != 1:
  pyautogui.moveTo(612, 1014, 0)
  click(612, 1014)
  keyboard.write('sup'))
    """



        


