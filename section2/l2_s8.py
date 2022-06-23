from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


browser = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name = 'firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name = 'lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name = 'email']")
    input3.send_keys("petrov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(10)
    browser.quit()
