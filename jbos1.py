from selenium import webdriver
import time
import pyautogui
import pygetwindow as gw

def t24_stop(username, password, keywords):
    driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\Documents\jbost24\geckodriver.exe')

    #T24 Login page
    driver.get("https://172.18.247.187:8443/BSGDEV/servlet/BrowserServlet")
    driver.maximize_window()
    time.sleep(1)

    # find username/email field and send the username itself to the input field
    driver.find_element("id", "signOnName").send_keys(username)
    time.sleep(1)

    # find password input field and insert password as well
    driver.find_element("id", "password").send_keys(password)
    time.sleep(1)

    # click login button
    driver.find_element("id", "sign-in").click()
    time.sleep(3)

    print("[+] Login")
    time.sleep(3)

    # TS, I TSM
    pyautogui.typewrite(keywords)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)

    # Stop Service
    for i in range(5):
        pyautogui.press("tab")
        time.sleep(0.1)

    pyautogui.press("right")
    for i in range(14):
        pyautogui.press("tab")
        time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(1)
    driver.maximize_window()
    time.sleep(1)
    driver.maximize_window()
    print("[+] Jbos1")
    time.sleep(2)
    window_name = ", - Mozilla Firefox"
    window = gw.getWindowsWithTitle(window_name)
    window[0].close()
    print(f"Window '{window_name}' closed.")
    time.sleep(2)
    

#username = "ORPUSER1"
#password = "P@Ssw0rd"
#keywords = "TS, I TSM"
#t24_stop(username, password, keywords)