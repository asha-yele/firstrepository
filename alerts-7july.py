

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

elementBtn = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
elementBtn.click()
time.sleep(3)
# driver.switch_to.alert.accept()     ## OK ## click on ok button

driver.switch_to.alert.dismiss()     ## cancel ## click on cancel button
