from Generic.read_excel_data import *

class HomePage(ExcelRead):
    def __init__(self, driver):
        self.driver = driver
        self.d = self.read_locator("HomePage")
    def logout_link(self):
        self.driver.find_element(*self.d["logout_link"]).click()
    def user_tab(self):
        self.driver.find_element(*self.d["user_tab"]).click()
    





