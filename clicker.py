import keyboard
import pyautogui

pyautogui.PAUSE = 0.001
while True:
	if keyboard.is_pressed('2'):
		pyautogui.rightClick()
	if keyboard.is_pressed('1'):
		pyautogui.click()
