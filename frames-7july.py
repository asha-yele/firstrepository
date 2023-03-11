import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

driver.switch_to.frame('iframeResult')  # go to perticular  iframe by name
btnElement = driver.find_element(By.XPATH, '/html/body/button')
btnElement.click()
