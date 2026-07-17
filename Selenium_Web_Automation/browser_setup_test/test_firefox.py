# test_firefox.py
# Erstellt: 10.07.26 um 14:19
# Autor: natalya
# Projekt: QA-Portfolio


import time

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.profile = (
    "/Users/natalya/Library/Application Support/"
    "Firefox/Profiles/yk2cvvhc.default-release"
)

driver = webdriver.Firefox(options=options)

driver.get("https://automationexercise.com/")

time.sleep(20)

driver.quit()
