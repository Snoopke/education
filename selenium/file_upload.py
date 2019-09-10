import os
from selenium import webdriver
import time

try:

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('misha')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('zamotin')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('cyegb@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    file_upload = browser.find_element_by_name('file')
    file_upload.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(15)
    browser.quit()








