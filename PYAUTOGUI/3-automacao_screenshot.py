import pyautogui
import time
"""
pyautogui.moveTo(1250, 15, duration=0.7)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.screenshot("doc.png")
time.sleep(1)
pyautogui.alert(text="Imagem salva com sucesso", title="Captura de imagem", button="ok")
"""

while True:
  pyautogui.screenshot(f"image_{time.time()}.png")
  time.sleep(3)

