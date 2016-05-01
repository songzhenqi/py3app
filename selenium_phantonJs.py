# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__author__ = 'User'
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
phantom_path = "E:/Programe/phantomjs-2.1.1-windows/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=phantom_path)
driver.get(url)
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()
