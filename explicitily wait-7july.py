import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.XPATH, '//*[@id="start"]/button').click()


##elementLoding = driver.find_element(By.XPATH, '//*[@id="loading"]')
locator = By.XPATH, '//*[@id="loading"]'
elementLoding = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locator))
print(elementLoding.get_attribute('innerHTML'))

element = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="finish"]/h4')))
##element = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(element.get_attribute('innerHTML'))


## DOM => Document object model


## Presence => code is available in HTML

## visiblity => visible on screen/page irrespective of presence