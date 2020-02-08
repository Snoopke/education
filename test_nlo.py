import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_answer_after_input(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    print(link)
    browser.get(link)
    input1 = browser.find_element_by_css_selector('.textarea')
    answer = math.log(int(time.time()))
    input1.send_keys(str(answer))
    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    feedback = browser.find_element_by_css_selector('.smart-hints__hint')
    warning = feedback.text
    assert warning == "Correct!", feedback