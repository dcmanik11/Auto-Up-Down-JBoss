import time
import ctypes
import subprocess
import pyautogui
import pygetwindow as gw

def dbtool_up(script_path1, script_path2, window_name):
    if 1 > 0:
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", script_path1, None, None, 1)
            print("Batch script executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing batch script: {e}")
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Script execution interrupted by user.")
    
    if 1 > 0:
        print(f"Waiting {script_path1}")
        time.sleep(15)
        pyautogui.typewrite("JQL CLEAR-FILE F.TSA.STATUS")
        pyautogui.press("enter")
        time.sleep(1)
        
        pyautogui.typewrite("CLEAR-FILE F.BATCH.STATUS")
        pyautogui.press("enter")
        time.sleep(1)
        
        # Exit
        pyautogui.typewrite("x")
        pyautogui.press("enter")
        time.sleep(3)
        
    if 1 > 0:
        window = gw.getWindowsWithTitle(window_name)
        if 1 > 0:
            window.close()
        else:
            print(f"Window with name '{window_name}' not found.")
        
    # Open JbosGUAT
    if 1 > 0:
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", script_path2, None, None, 1)
            print("Batch script executed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing batch script: {e}")
        except KeyboardInterrupt:
            print("KeyboardInterrupt: Script execution interrupted by user.")
        
    

#script_path1 = r"C:\Temenos\BSGDEV\DBTools.bat"
#script_path2 = r"C:\Temenos\BSGDEV\jBossBSGDEV.bat"
#dbtool_up(script_path1, script_path2)
