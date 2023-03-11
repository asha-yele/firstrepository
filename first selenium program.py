
from selenium import webdriver          ## importing selenuim module

driver = webdriver.Chrome()             ## create and and load chrome driver obejct
    #####driver = webdriver.chrome()  dont use c small chrome             ## create and and load chrome driver obejct
    ###driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")             ## create and and load chrome driver obejct

driver.get("https://www.facebook.com")      ## open website/ url
driver.maximize_window()
print("Page title : ", driver.title)        ## get title of website
print("Page URL : ", driver.current_url)    ## get current url of website


driver.get("https://www.amazon.com/")
driver.minimize_window()
print("Page title : ", driver.title)        ## get title of website
print("Page URL : ", driver.current_url)    ## get current url of website

driver.close()      ## close current window of browser
driver.quit()       ## quits all windows opened by our script


### -===============================================================================

### For latest version

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# s=Service('C:/chromedriver.exe')
# driver = webdriver.Chrome(service=s)
# driver.get('https://www.google.com')
