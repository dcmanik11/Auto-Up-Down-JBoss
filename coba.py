import time
import pyautogui
print("start")
time.sleep(5)
print("mulai")
for i in range(5):
    pyautogui.press("tab")
    time.sleep(2)
print("arah kanan")
pyautogui.press("right")
print("tab 12x")
for i in range(12):
    pyautogui.press("tab")
    time.sleep(2)
print("start enter")
pyautogui.press("enter")
print("DONE")

# Jboss Guat
# Pindah dlu ke window J
pyautogui.hotkey('ctrl','c')
# est time 51s
time.sleep(60)
pyautogui.typewrite("Y")
time.sleep(2)
pyautogui.press("enter")

# DBTool
time.sleep(15) #after open est time 15s
pyautogui.typewrite("JQL CLEAR-FILE F.TSA.STATUS")
pyautogui.press("enter")
time.sleep(5)
pyautogui.typewrite("CLEAR-FILE F.BATCH.STATUS")
pyautogui.press("enter")
time.sleep(5)
pyautogui.typewrite("x")
pyautogui.press("enter")
print("DONE")
#Up JBoss
#est time 75s part 1
#est time 47s part 2

#Login T24

#TAFJEE

