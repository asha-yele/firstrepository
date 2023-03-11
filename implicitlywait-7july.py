import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.implicitly_wait(10)  # Comes from selenium. It will pause maximun for given sec and min till element appears on html
## once defined it wil be applicable to all controls

driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

###time.sleep(5)           ## it comes from python, it will pause script for minimun given sec
elementLoding = driver.find_element(By.XPATH, '//*[@id="loading"]')
print(elementLoding.get_attribute('innerHTML'))

###time.sleep(10)       ##time.sleep(5)           ## it comes from python, it will pause script for minimun given sec
element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(element.get_attribute('innerHTML'))


