from tkinter import W
from pkg_resources import working_set
import pyautogui

pyautogui.PAUSE = .159
pyautogui.sleep(5)
pyautogui.keyDown('w')
pyautogui.sleep(5)
pyautogui.keyUp('w')
