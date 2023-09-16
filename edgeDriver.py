from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from bs4 import BeautifulSoup
import os
from datetime import datetime
from selenium.webdriver import ActionChains

driver = webdriver.Edge(executable_path = 'C:\\Users\\Downloads\\edgedriver_win32\\msedgedriver.exe')
def get_trulia_estimate(address):
    driver.get('https://www.trulia.com/')
    print(address)
    element = (By.ID, 'homepageSearchBoxTextInput')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(element)).send_keys(address)

    search_button = (By.CSS_SELECTOR, "button[data-auto-test-id='searchButton']")

    WebDriverWait(driver, 50).until(EC.element_to_be_clickable(search_button)).click()

    time.sleep(3) 