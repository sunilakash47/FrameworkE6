import pytest
from selenium.webdriver import Chrome
from Generic.log_file import *

@pytest.fixture
def launch():
    driver = Chrome()
    logg("info", "Opening the browsr")
    driver.get("http://localhost/login.do")
    logg("info", "Entering a url")
    driver.maximize_window()
    logg("info", "Maximizing browser")
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    logg("info", "Closing the browser")


