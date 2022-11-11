import time
import pyautogui
import pyperclip


## Open a new tab on google

import webbrowser


url = "https://www.google.com/"

webbrowser.open(url)

## Click the window and type "平泉町　観光"

# pg.moveTo(715, 366)

# pg.click(x=715, y=366, clicks=1, interval=2)

time.sleep(2)
pyperclip.copy("平泉町 観光")
pyautogui.keyDown("command")
pyautogui.press("v")
pyautogui.keyUp("command")
# pyperclip.copy('日本語の文字列')
# pyautogui.hotkey('ctrl', 'v')




# time.sleep(1)
pyautogui.press("enter")

# screenshot
time.sleep(2)
pyautogui.screenshot()
pyautogui.screenshot("screenshot_test1_image.png")


