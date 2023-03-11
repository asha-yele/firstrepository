import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, 'Click Here').click()

all_handles = driver.window_handles
myhandledict={
"facebook.com":"CDwindow-661A6A1C49BDA5106E34C39ED2A6D058",
"Credence.com":"CDwindow-39C9FE3E90CC63DFC83394D4C5648D37"

}
myhandledict.get("Credence.com")