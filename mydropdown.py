import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
element = driver.find_element(By.ID, "mySelect")
dropdown = Select(element)
#dropdown.first_selected_option
#time.sleep(5)
alloptions=dropdown.options

#for item in alloptions:
    #print(item.get_attribute("innerHTMl"))
   # print(item.text)

elements = driver.find_elements(By.TAG_NAME, 'a')
for item in elements:
    print(item.get_attribute('href'))    gets url all item

