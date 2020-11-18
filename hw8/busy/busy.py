import time
import pyautogui

oldepoch = time.time()
mousePos = pyautogui.position()

def tenseconds_passed(oldepoch):
    return time.time() - oldepoch >= 10

def mouse_moved(mousePos):
    if pyautogui.position() == mousePos:
        return True



while mouse_moved(mousePos) is True:
    if tenseconds_passed(oldepoch) is True:
        pyautogui.move(1919, 0, duration=3000)
       
