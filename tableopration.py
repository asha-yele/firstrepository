import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/html/html_tables.asp")

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th[1]').text)

# print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[2]').get_attribute('innerHTML'))

print(driver.find_element(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td[2]').text)



elementList = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr')
print("Number of rows : ", len(elementList))
print("Number of rows : ", elementList.__len__())

elementList = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th')
print("Number of column: ", len(elementList))
print("Number of column : ", elementList.__len__())

elementList = driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[2]/td')
print("Number of column : ", len(elementList))
print("Number of column : ", elementList.__len__())


## assignment :  print all table values by using loop