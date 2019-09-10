import math
from selenium import webdriver
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input1 = browser.find_element_by_css_selector('input')
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector('[id=robotCheckbox]')
    checkbox.click()
    radiobatton = browser.find_element_by_css_selector('[id=robotsRule]')
    radiobatton.click()
    time.sleep(5)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()