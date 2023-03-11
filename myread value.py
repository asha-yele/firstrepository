import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
s=Service("C:\\Users\\Indrajit Yele\\AppData\\Local\\Programs\\Python\\Python310\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://seleniumbase.io/demo_page")
inputelement = driver.find_element(By.ID, "myTextInput")
inputelement.send_keys("ashayele")
print("input text field:", inputelement.get_attribute("id"))
print("input text field:", inputelement.get_attribute("value"))
print("input text field:", inputelement.get_attribute("Xpath"))
time.sleep(5)
driver.back()
#time.sleep(3)
#driver.forward()    # Redirect to next

#driver.quit()