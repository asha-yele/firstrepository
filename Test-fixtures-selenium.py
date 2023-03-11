import pytest
from selenium import webdriver

driver = None


@pytest.fixture
def setup():
    global driver ## global => to access it outside function
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield   ## divide before and after activity
    print(driver.title)
    driver.close()


def test_1(setup):
    driver.get("https://facebook.com")
    ## other test logic to login facebook


def test_2(setup):
    driver.get('https://gmail.com')
    ## other test logic


def test_3(setup):
    driver.get('https://amazon.com')
    ## other test logic