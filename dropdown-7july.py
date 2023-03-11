import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")

# Manual way to do this.. which creates complexity when we multiple combinations
#driver.find_element(By.XPATH, '//*[@id="mySelect"]/option[3]').click()


    #####/html/body/form/table/tbody/tr[7]/td[2]/select/option[3]        ### copy full xpath
    #### //*[@id="mySelect"]/option[3]          ## optimized version of xpath

###---------------------------------------------------------------------------------


# element = driver.find_element(By.ID, 'mySelect')
# dropdown = Select(element)
#
# time.sleep(3)
# dropdown.select_by_index(3)     ## it will select 3rd index from dropdown
#
# time.sleep(3)
# dropdown.select_by_value('25%')     ## it will select option whose value attribute is 25%
#
# time.sleep(3)
# dropdown.select_by_visible_text('Set to 75%')       # it will select option whose visible text on webpage is 'set to 75%'
#
#
# all_options = dropdown.options      # """Returns a list of all options belonging to this select tag"""
# print("Number of options : ", len(all_options))
#
### Task : I want to print all the options visible text and value

#for item in all_options:
    #print(item.get_attribute('innerHTML'))
    #print(item.text)

##---------------------------------------------------------

elements = driver.find_elements(By.TAG_NAME, 'a')
for item in elements:
    print(item.get_attribute('href'))
