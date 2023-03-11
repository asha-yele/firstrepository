import time

from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
driver.get("https://www.facebook.com")
# driver.maximize_window()
# time.sleep(3)
# driver.minimize_window()
# time.sleep(2)
# driver.get("https://www.amazon.com/")
# print("Title: ", driver.title)
# print("Url: ", driver.current_url)
# time.sleep(5)
#
# driver.close()
driver.find_element(By.NAME,"pass")
