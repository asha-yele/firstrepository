import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")

inputElement = driver.find_element(By.ID, "myTextInput2")
#print("Input Text: ", inputElement.text)
print("Input Text: ", inputElement.get_attribute("value"))
print("Input type: ", inputElement.get_attribute("type"))
print("Input ID: ", inputElement.get_attribute("id"))
print("Input Name: ", inputElement.get_attribute("name"))

time.sleep(5)
driver.back()  # redirect to previous page/url
time.sleep(5)
driver.forward()    # Redirect to next

inputElement.clear()