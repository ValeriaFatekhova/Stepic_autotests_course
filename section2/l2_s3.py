from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser.get(link)

    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    z = int(x)+int(y)
    print(z)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(z))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
