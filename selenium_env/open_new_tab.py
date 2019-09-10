import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    button = browser.find_element_by_css_selector("button")
    time.sleep(1)
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('input')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()