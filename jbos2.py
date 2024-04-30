import time
import pyautogui
import pygetwindow as gw

def jboss_down(window_name):
    if 1 > 0:
        window = gw.getWindowsWithTitle(window_name)
        if 1 > 0:
            window[0].activate()
        else:
            print(f"Window with name '{window_name}' not found.")

        # Start terminate
        print("Start Terminate")
        pyautogui.hotkey("ctrl","c")
        print("[+] Start Countdown 70s")
        time.sleep(70) #60s
        print("[+] Finish Countdown")

        # Commit terminate/Close JBossGUAT
        pyautogui.typewrite("Y")
        time.sleep(1)
        pyautogui.press("enter")
    else :
        print(f"{window_name} not found")
    print("[+] Jbos2")
    
#window_name = "Administrator:  JBoss BSGDEV"
#jboss_down(window_name)
    

