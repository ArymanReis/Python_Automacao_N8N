import pyautogui
import time

#1-Tamanho da tela
print(pyautogui.size())

#2-Pegar a posição atual do cursor
print(pyautogui.position())

#3-Aplicação para vê o mouse em tempo real
"""
Digite o comando python no terminal
from pyautogui import mouse
mouseInfo()

"""

#4-Mover o cursor do mouse
pyautogui.moveTo(1250, 15, duration=0.8)
time.sleep(1)
pyautogui.click()

#5 - Realizando o Scroll
pyautogui.moveTo(1060, 461)
pyautogui.click()
time.sleep(1)
pyautogui.scroll(3000)
