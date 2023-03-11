import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")

inputElement = driver.find_element(By.ID, "dropOption1")
print("Is element displayed : ", inputElement.is_displayed())

inputElement = driver.find_element(By.ID, "myTextInput")
print("Is element displayed : ", inputElement.is_displayed())

### -----------------------------------------------------------------

#inputElement = driver.find_element(By.ID, "radioButton1")
#print("Is element selected : ", inputElement.is_selected())

#inputElement = driver.find_element(By.ID, "radioButton2")
#print("Is element selected : ", inputElement.is_selected())


### =============================================================

inputReadonly = driver.find_element(By.ID, "readOnlyText")
#print(inputReadonly.is_enabled())
inputReadonly.get_attribute('readonly')
# 'true'
# inputElement.get_attribute('readonly')
# inputElement.get_attribute('readonly')
