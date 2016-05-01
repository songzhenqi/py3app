# coding: utf-8
from selenium import webdriver
import time

__author__ = 'User'
url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
phantom_path = "E:/Programe/phantomjs-2.1.1-windows/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=phantom_path)
driver.get(url)
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()
