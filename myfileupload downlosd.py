import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(3)

driver.find_element(By.ID, 'file-upload').send_keys("C:\\Users\\Indrajit Yele\\Documents\\ct10\\New folder\\xyz.txt")
time.sleep(9)
driver.find_element(By.ID, 'file-submit').click()
