from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PATH = "E:\Python (VS CODE)\Bots\chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://sims.rutgers.edu/webreg/')
time.sleep(.7)

Un = driver.find_element_by_name("coursesToAdd[0].courseIndex")
course = "07331"
Un.send_keys(course)
