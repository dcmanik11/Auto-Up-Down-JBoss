from selenium import webdriver
import time

def tafjee_start(keywords2):
    driver = webdriver.Firefox(executable_path=r'C:\Users\Administrator\Documents\jbost24\geckodriver.exe')
    driver.get("https://172.18.247.187:8443/TAFJEE/")
    driver.maximize_window()
    time.sleep(1)

    driver.find_element_by_link_text("Execute servlet").click()
    time.sleep(1)
    search_box = driver.find_element_by_name("command")
    search_box.send_keys(keywords2)
    search_box = driver.find_element_by_id("submit").click()
    time.sleep(1)

    # coba refresh
    driver.find_element_by_name("apply").click()
    print("[+] Jbos2")
    print("[+] DONE BANG")

    # tutup window

#keywords2 = "START.TSM"
#tafjee_start(keywords2)