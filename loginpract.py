from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
import time
driver.get("http://facebook.com")
time.sleep(3)
Email = driver.find_element(By.ID, "email")
Email.send_keys("ashathorat13@gmail.com")
password = driver.find_element(By.ID, "pass")
password.send_keys("surekha67123")
loginbutton = driver.find_element(By.NAME, "login").click()
driver.quit()

# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/span/div/div[1]/div/svg/g/image").click()
# driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div[2]/div/div[5]/div/div[1]/div[2]/div/div/div/div/span").click()