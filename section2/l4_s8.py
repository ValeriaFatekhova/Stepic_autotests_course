import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 13).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    browser.quit()