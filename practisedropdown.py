from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

element=driver.find_element(By.ID,"mySelect")
dropdown=Select(element)
dropdown.select_by_index(2)
time.sleep(5)
dropdown.select_by_visible_text("Set to 25%")
dropdown.select_by_value("50%")
dropdown.first_selected_option




