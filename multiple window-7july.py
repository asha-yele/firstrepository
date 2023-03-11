import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.LINK_TEXT, 'Click Here').click()

all_handles = driver.window_handles
print("All window handles : ", all_handles)

print("current window Handle  : ", driver.current_window_handle)

driver.switch_to.window(all_handles[-1])        ## all_handles[-1]  # gives latest or lastly opned window

h3Element = driver.find_element(By.XPATH, '/html/body/div/h3')
print(h3Element.text)
print(h3Element.get_attribute('innerHTML'))

## facebook.com
## gmail.com
## amazon.com
## flipkart.com
## Credence.com


## handles.find("Facebook.com")
# for handle in all_handles:
#     driver.switch_to.window(handle)
#     print(driver.title)
#     if(driver.title == "Facebook.com"):
#         break
## perform operation on facebook.com





