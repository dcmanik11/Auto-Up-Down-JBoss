from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'C:\Users\user\Downloads\FinPro JBOS\geckodriver.exe')
keywords = "START.TSM"
driver.get("https://172.18.247.187:8443/TAFJEE/index.html")
driver.maximize_window()
time.sleep(5)

driver.find_element_by_link_text("Execute servlet").click()
time.sleep(3)
search_box = driver.find_element_by_name("command")
search_box.send_keys(keywords)
search_box = driver.find_element_by_id("submit").click()
time.sleep(3)