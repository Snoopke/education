import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    knopka = browser.find_element_by_css_selector('button')
    knopka.click()
    alert = browser.switch_to.alert
    alert.accept()
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('input')
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
