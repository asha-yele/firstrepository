
from selenium import webdriver
driver = webdriver.Chrome()
import time
from selenium.webdriver.common.by import By
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button').click()
time.sleep(5)
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
driver.close()
