import subprocess
import pyautogui
import time
import ctypes
import pygetwindow as gw

def jshell_batch_script(script_path):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script_path, None, None, 1)
        print("Batch script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing batch script: {e}")
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Script execution interrupted by user.")

def jshell_button():
    time.sleep(5)
    pyautogui.typewrite('DBTools')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(20)
    pyautogui.typewrite('JQL CLEAR-FILE F.TSA.STATUS WITH @ID NOT LIKE ...OLTP...')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('x')
    time.sleep(5)
    pyautogui.press('enter')
    time.sleep(5)

def close_jshell(program_name):
    try:
        window = gw.getWindowsWithTitle(rf'"{program_name}"')[0]
        window.close()
        print(f"Closed {program_name} window.")
    except IndexError:
        print(f"Error: {program_name} window not found.")

jshell_batch_path = r'E:\Temenos\BSGPROD\jShel.bat'
jshell_batch_script(jshell_batch_path)
jshell_button()
time.sleep(5)
close_jshell('Database Operations')