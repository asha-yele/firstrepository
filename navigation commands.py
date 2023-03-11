from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")      ## open website/ url
driver.maximize_window()
print("Page title : ", driver.title)        ## get title of website
print("Page URL : ", driver.current_url)    ## get current url of website

driver.get("https://www.amazon.com/")

print("Page title : ", driver.title)        ## get title of website
print("Page URL : ", driver.current_url)    ## get current url of website

driver.back()

driver.forward()

driver.get("https://www.gmail.com/")
driver.minimize_window()
print("Page title : ", driver.title)        ## get title of website
print("Page URL : ", driver.current_url)    ## get current url of website
driver.close()      ## close current window of browser
driver.quit()       ## quits all windows opened by our script


