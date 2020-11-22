import os
import re
import traceback
from time import sleep
from selenium import webdriver
from urllib.parse import quote_plus, unquote, urlparse
from selenium.webdriver.firefox.options import Options


URL = "http://localhost"
PORT = 3142
URL_BASE = URL + ':' +str(PORT)
FLAG = "hackdef{csp_4nd_*.gO0gl3.c0m_d0n7_90_w3Ll}"
CREDS = "YWRtaW46YWJiMlhFQXQ4TE5TUExR"

def same_site(URL):
    url_obj = urlparse(URL)
    url_usr = url_obj.scheme + '://' + url_obj.netloc
    if URL_BASE == url_usr:
        return True 
    return False

def visitor(URL):
	try:
		options = Options()
		options.headless = True

		driver = webdriver.Firefox(options=options)
		driver.get(URL)
		driver.add_cookie({"name": "flag", "value": FLAG})
		driver.add_cookie({"name": "creds", "value": CREDS})
		driver.refresh()
		sleep(2)
		driver.quit()

	except Exception as e:
		traceback.print_exc()