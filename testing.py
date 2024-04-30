from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pygetwindow as gw
import pyautogui

driver = webdriver.Firefox(executable_path=r'C:\Users\user\Downloads\FinPro JBOS\geckodriver')
keywords = "indonesia"

# Go to Page
driver.get("https://www.wikipedia.org/")
# driver.maximize_window()
time.sleep(5)

driver.find_element_by_id("js-link-box-en").click()
time.sleep(3)
search_box = driver.find_element("name","search")
search_box.send_keys(keywords)
search_box.send_keys(Keys.ENTER)
time.sleep(3)

print("Start Moving")

# import pygetwindow as gw
# import pyautogui

def activate_window(window_name):
    window = gw.getWindowsWithTitle(window_name)
    if len(window) > 0:
        window[0].activate()
        print("Window Activated")
        return window[0]  # Return the activated window object
    else:
        print(f"Window with name '{window_name}' not found.")
        return None

def perform_actions_on_window(window):
    if window is not None:
        # Example action: simulate pressing the "C" key
        print("Start auto")
        time.sleep(5)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(5)
        pyautogui.press('enter')
        print("Sent Ctrl+C and Enter.")
        time.sleep(5)
        pyautogui.press('Y')
        time.sleep(5)
        pyautogui.press('enter')
        print("Close Session JBos Success")

window_name = "Untitled - Notepad"
activated_window = activate_window(window_name)
time.sleep(3)
perform_actions_on_window(activated_window)

window_name = "Firefox"
activated_window = activate_window(window_name)
print("Finish")
