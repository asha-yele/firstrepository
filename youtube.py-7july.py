import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://amazon.in")
driver.maximize_window()
time.sleep(2)
driver.execute_script("window.open('https://www.google.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.flipkart.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.cricbuzz.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.youtube.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.irctc.co.in');")
time.sleep(2)
driver.execute_script("window.open('https://www.naukri.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.shaadi.com');")
time.sleep(2)
driver.execute_script("window.open('https://www.oyorooms.com/');")
time.sleep(2)
driver.execute_script("window.open('https://www.ibibo.com/');")

all_handles = driver.window_handles


urlHandle = {}

for handle in all_handles:
    driver.switch_to.window(handle)
    urlHandle.update({driver.current_url: handle})

print(urlHandle)


driver.switch_to.window(urlHandle['https://www.youtube.com/'])

searchBox = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')

searchBox.click()
searchBox.send_keys("filhaal Full song")
driver.implicitly_wait(5)
BtnSearch = driver.find_element(By.ID, "search-icon-legacy")
driver.implicitly_wait(5)
BtnSearch.click()
driver.implicitly_wait(5)
# SongString = driver.find_element(By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/div[2]")