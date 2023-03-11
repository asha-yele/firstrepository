12import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # Creating class object of Chrome
driver.get("https://seleniumbase.io/demo_page")

parentHover = driver.find_element(By.ID, 'myDropdown')
###parentHover.click()     ## is not clickable# we can not perform this operration

#drop3 = driver.find_element(By.ID, 'dropOption3')
### drop3.click()  ## element not interactable # we can not directly reach to element before reaching to parent
#actionObj = ActionChains(driver)
#actionObj.move_to_element(parentHover).move_to_element(drop3).click().perform()

### -----------------------------------------------
## Double click

# btn = driver.find_element(By.ID, 'myButton')
# actionObj.double_click(btn).perform()
#
# ###---------------------------------------------------
# ### right click
#
# actionObj.context_click().perform() ## option 1 : without element right click in webpage
# actionObj.context_click(btn).perform() ## option 2 : right click on given element
# ### ==================================================
#
#
# ## Drag and drop
#
# driver.find_element(By.ID, 'checkBox1').click()
#
# dropCapital = driver.find_element(By.XPATH, '//*[@id="logo"]')
# dropBox = driver.find_element(By.ID, 'drop2')
#
# actionObj.drag_and_drop(dropCapital, dropBox).perform()
