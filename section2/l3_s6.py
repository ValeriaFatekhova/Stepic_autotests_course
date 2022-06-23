import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    new_window = browser.window_handles[1]
    first_window = browser.window_handles[0]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(10)
    browser.quit()
