from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

try:
    link = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block .third")
    input3.send_keys("petrov@mail.ru")
    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block .first")
    input4.send_keys("1111")
    input4 = browser.find_element(By.CSS_SELECTOR, "div.second_block .second")
    input4.send_keys("address")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
