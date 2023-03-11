from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
#parenthover=driver.find_element(By.ID,'myDropdown')
#dropdown1=driver.find_element(By.ID,'dropOption1')

actionobj=ActionChains(driver)
#actionobj.move_to_element(parenthover).move_to_element(dropdown1).click().perform()

#Doubleclick
#btn=driver.find_element(By.ID,'myButton')
#actionobj.double_click(btn).perform()

#Rightclick
#inputtxt=driver.find_element(By.ID,'myTextInput')
#actionobj.context_click(inputtxt).perform()

#DragandDrop

urllink=driver.find_element(By.ID,'myLink1')
linktxt=driver.find_element(By.XPATH,'/html/body')
actionobj.drag_and_drop(urllink,linktxt).perform()


driver.find_element(By.ID, 'checkBox1').click()

dropCapital = driver.find_element(By.XPATH, '//*[@id="logo"]')
dropBox = driver.find_element(By.ID, 'drop2')

actionobj.drag_and_drop(dropCapital, dropBox).perform()

