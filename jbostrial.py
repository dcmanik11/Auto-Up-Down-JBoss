# from selenium import webdriver
import pyautogui
# from selenium.webdriver.support.ui import WebDriverWait
# import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# usr n pass
username = "ORPUSER1"
password = "P@Ssw0rd"

# initialize the Edge driver
# options = webdriver.FirefoxOptions()
# options.add_experimental_option("detach", True)
driver = webdriver.Firefox(executable_path=r'C:\Users\user\Downloads\FinPro JBOS\geckodriver')

#T24 Login page
driver.get("https://172.18.247.187:8443/BSGDEV/servlet/BrowserServlet")
time.sleep(5)
# driver.find_element("id", "details-button").click()
# time.sleep(2)
# driver.find_element("id", "proceed-link").click()
# time.sleep(2)

# find username/email field and send the username itself to the input field
driver.find_element("id", "signOnName").send_keys(username)
time.sleep(2)

# find password input field and insert password as well
driver.find_element("id", "password").send_keys(password)
time.sleep(2)

# click login button
driver.find_element("id", "sign-in").click()
time.sleep(3)

# get the errors (if there are)
error_message = "Incorrect username or password."
errors = driver.find_elements("css selector", ".flash-error")

# print the errors optionally
for e in errors:
    print(e.text)
# if we find that error message within errors, then login is failed
if any(error_message in e.text for e in errors):
    print("[!] Login failed")
else:
    print("[+] Login successful")
    
# driver.maximize_window()
time.sleep(15)

henti = "TS, I TSM"
print("Logout")
driver.find_element_by_link_text("Sign Off").click()
# driver.find_element_by_name("commandValue").send_keys(henti)
# time.sleep(3)

# driver.find_element_by_id("cmdline_img").click()
# time.sleep(3)
# pyautogui.typewrite("ping 8.8.8.8 -t")
# pyautogui.press("enter")
# time.sleep(10)

# if any(error_message in e.text for e in errors):
#     print("[!] CMD failed")
# else:
#     print("[+] CMD successful")
    
# pyautogui.hotkey('ctrl','c')

# time.sleep(3)
# driver.maximize_window()