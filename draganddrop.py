import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

action = ActionChains(driver)
## Drag and drop

dropCapital = driver.find_element(By.ID, 'box5')
dropBox = driver.find_element(By.ID, 'box105')

action.drag_and_drop(dropCapital, dropBox).perform()

