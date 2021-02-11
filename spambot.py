import pyautogui, time
time.sleep(20)
f = open("script", 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")