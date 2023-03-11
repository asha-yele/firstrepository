from selenium import webdriver
driver = webdriver.Chrome()
import time
from selenium.webdriver.common.by import By
driver.get('https://www.youtube.com/')
driver.find_element(By.XPATH, '/html/body/script[1]').click()
