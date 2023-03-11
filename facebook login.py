
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

##
##inputEmail = driver.find_element_by_id("email")
inputEmail = driver.find_element(By.ID, "email")
inputEmail.send_keys("batch10@credence.com")

##inputPass = driver.find_element_by_id("pass")
inputPass = driver.find_element(By.ID, "pass")
inputPass.send_keys("Password@123")

btnLogin = driver.find_element(By.NAME, "login")
btnLogin.click()


### Id value will be unique on web page
## name can be duplicate

## driver.find_element(By.XPATH, '//*[@id="u_0_5_k3"]')        ## id will get changed all the time so for facebook we can not trust on xpath

driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')