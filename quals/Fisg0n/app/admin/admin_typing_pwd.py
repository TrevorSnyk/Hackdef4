#!/usr/bin/python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
import os


USERNAME = "admin"
URL = "http://172.17.0.2:3142/" 
FLAG = "hackdef{st0r3d_xss_c4n_b3_d4n93r0u$_t0o!}"


def send_with_delay(field, word, delay ):
	for char in word:
		field.send_keys(char)
		sleep(delay)

def admin_typing():
	username = browser.find_element_by_name('username')
	send_with_delay(username,USERNAME,0.3)
	password = browser.find_element_by_name('password')
	send_with_delay(password,FLAG,0.3)
	browser.quit()


chromeOptions = Options()
chromeOptions.headless = True
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-dev-shm-usage")
chromeOptions.add_argument('--headless')

browser = webdriver.Chrome(options=chromeOptions)

browser.get(URL)

try:
        while True:
            WebDriverWait(browser, 1).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            alert.accept()
except TimeoutException:
        admin_typing()
