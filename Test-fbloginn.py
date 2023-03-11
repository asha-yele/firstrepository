from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
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



