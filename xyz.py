from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://www.facebook.com")
all_handles = driver.window_handles
print("All window handles : ", all_handles)

print("current window Handle  : ", driver.current_window_handle)

driver.switch_to.window(all_handles[-1])        ## all_handles[-1]  # gives latest or lastly opned window
