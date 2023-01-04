import pyautogui

# Specific coordinates
# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

# Relative coordinates

pyautogui.moveRel(15, 0, duration=0.5)
pyautogui.moveRel(-15, 0, duration=0.5)
# pyautogui.moveRel(-100, 0, duration=0.25)
# pyautogui.moveRel(0, -100, duration=0.25)