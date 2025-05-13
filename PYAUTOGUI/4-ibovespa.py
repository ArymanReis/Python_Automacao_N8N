# 240 x 80
import pyautogui
import time

pyautogui.press("winleft")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.moveTo(179, 65, duration=0.7)
time.sleep(1)
pyautogui.click()
pyautogui.write("ibovespa hoje", interval=0.10)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.screenshot("ibovespa.png")
pyautogui.alert(
  text="Gerada a imagem na raiz",
  title="Automação realizada",
  button="OK"
)