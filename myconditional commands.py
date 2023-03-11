from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
#element=driver.find_element(By.ID, "mySelect")
#print("is input dropdown enbled:",element.is_enabled())
#element.get_attribute("readonly")

paragraphinput=driver.find_element(By.ID,"svgRect")
print("is paragraph text is enable:", paragraphinput.is_enabled())
paragraphinput.get_attribute('readonly')