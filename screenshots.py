import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

## Question Absolut path vs relative path

# option 1
driver.get_screenshot_as_file("C:/asha/python files/Facebook.png")

# option 2
driver.save_screenshot("screenshot.png")
