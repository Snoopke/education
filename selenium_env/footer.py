import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_css_selector('[id=input_value]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);")
    checkbox = browser.find_element_by_css_selector('[id=robotCheckbox]')
    checkbox.click()
    radiobatton = browser.find_element_by_css_selector('[id=robotsRule]')
    radiobatton.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(15)
    browser.quit()