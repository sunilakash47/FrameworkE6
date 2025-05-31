from Generic.screenshot import *
from time import sleep

def verify_text(etext, driver):
    try:
        sleep(2)
        assert etext in driver.page_source
    except:
        take_screenshot(driver)
        raise Exception ("Text not matches")



