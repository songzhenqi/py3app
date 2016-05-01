from selenium import webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

__author__ = 'User'


def wait_for_load(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


driver1 = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
driver1.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
wait_for_load(driver1)
print(driver1.page_source)
