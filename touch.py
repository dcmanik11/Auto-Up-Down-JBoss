import pygetwindow as gw
import pyautogui
import time

def activate_window(window_name):
    window = gw.getWindowsWithTitle(window_name)
    if len(window) > 0:
        window[0].activate()
        return window[0]  # Return the activated window object
    else:
        print(f"Window with name '{window_name}' not found.")
        return None

def perform_actions_on_window(window):
    if window is not None:
        # Example action: simulate pressing the "C" key
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

window_name = "Firefox"

activated_window = activate_window(window_name)

perform_actions_on_window(activated_window)