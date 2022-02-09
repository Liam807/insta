from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def checkColor():
  i=0
  for i in range(3):
    x=565+(2*i)
    y=943+(2*i)
    checkColor = pyautogui.pixel(x, y)[0] == (239 or 240 or 238 or 241 or 242 or 243 or 244 or 245 or 246) or pyautogui.pixel(x+1, y+1)[0] == (239 or 240 or 238 or 241 or 242 or 243 or 244 or 245 or 246)
    if checkColor == True:
      break 
  return checkColor

def ResponseBot(Name, Pass,user):
  PATH = "E:\Python (VS CODE)\Bots\chromedriver"
  driver = webdriver.Chrome(PATH)
  driver.get('https://www.instagram.com/')
  time.sleep(.7)
  Un = driver.find_element_by_name("username")
  #Name = "leeyum.archive"#input("Username: ")
 # Pass = "Liam5years!"#input("Password: ")
  Un.send_keys(Name)
  Pw = driver.find_element_by_name("password")
  Pw.send_keys(Pass)
  Pw.send_keys(Keys.RETURN)
  time.sleep(2.8)
  DM = driver.find_element_by_class_name('xWeGp')
  DM.click()
  time.sleep(1.2)
  NotNow = driver.find_element_by_class_name('HoLwm')
  NotNow.click()
  time.sleep(1)
  send =driver.find_element_by_xpath("//button[@type='Send Message']")
  send.click
  time.sleep(3)
  Search = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button')
  Search.send_keys(user)
  time.sleep(.5)
  button = driver.find_element_by_class_name('wpO6b').click




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

  while(True):
    pass


  
ResponseBot("leeyum.archive", "Liam5years!", "liamavila_")