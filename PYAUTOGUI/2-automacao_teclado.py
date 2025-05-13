import pyautogui
import time

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("calculadora", interval=0.10)
time.sleep(1)
pyautogui.press("enter")

# Tecla de atalho
pyautogui.hotkey("ctrl", "shift", "esc")


