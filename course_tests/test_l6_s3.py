import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')
    yield browser
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"
                                  ])
def test_guest_should_see_login_link(browser, link):
    # link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)

    answer = math.log(int(time.time()))
    element = WebDriverWait(browser, 13).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
    element.send_keys(answer)
    button = WebDriverWait(browser, 2).until(
        expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()
    res = WebDriverWait(browser, 4).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text
    assert res == "Correct!"

