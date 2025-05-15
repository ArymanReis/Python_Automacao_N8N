"""
Nome: 285 x 301
Email: 286 x 340
Botão: 344 x 367
"""
import pyautogui
from time import sleep

with open("files/alunos.txt", "r", encoding="utf-8") as file:
  for line in file:
    nome = line.split(",")[0]
    email = line.split(",")[1]
    pyautogui.click(285, 301, duration=0.70)
    pyautogui.write(nome)
    pyautogui.click(286, 340, duration=0.70)
    pyautogui.write(email)
    pyautogui.click(344, 367, duration=0.4)
    pyautogui.screenshot(f"files/img/{nome}.png")
    sleep(1)