from Generic.read_excel_data import *

class TimeTrackPage(ExcelRead):
    def __init__(self, driver):
        self.driver = driver
        self.d = self.read_locator("TimeTrackPage")
    def select_user(self):
        self.driver.find_element(*self.d["select_user_arrow"]).click()
        self.driver.find_element(*self.d["select_user"]).click()
    def new_link(self):
        self.driver.find_element(*self.d["new_link"]).click()
        allid = self.driver.window_handles
        self.driver.switch_to.window(allid[1])
    def enter_estimate_time(self, data):
        self.driver.find_element(*self.d["enter_estimate_time"]).send_keys(data)
    def save_changes(self):
        self.driver.find_element(*self.d["save_changes"]).click()









