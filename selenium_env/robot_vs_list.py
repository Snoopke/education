from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def sum(x,y):
    return str(int(x) + int(y))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('[id=num1]')
    x = x_element.text
    y_element = browser.find_element_by_css_selector('#num2')
    y = y_element.text
    jojo = sum(x,y)

    select = Select(browser.find_element_by_css_selector('select'))
    select.select_by_value(jojo)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()