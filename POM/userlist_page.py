from Generic.read_excel_data import *

class UserListPage(ExcelRead):
    def __init__(self, driver):
        self.driver = driver
        self.d = self.read_locator("UserListPage")
    def user_button(self):
        self.driver.find_element(*self.d["user_button"]).click()
    def first_name(self, data):
        self.driver.find_element(*self.d["first_name"]).send_keys(data)
    def last_name(self, data):
        self.driver.find_element(*self.d["last_name"]).send_keys(data)
    def email(self, data):
        self.driver.find_element(*self.d["email"]).send_keys(data)
    def username(self, data):
        self.driver.find_element(*self.d["username"]).send_keys(data)
    def password(self, data):
        self.driver.find_element(*self.d["password"]).send_keys(data)
    def retype_password(self, data):
        self.driver.find_element(*self.d["retype_password"]).send_keys(data)
    def create_user_button(self):
        self.driver.find_element(*self.d["create_user_button"]).click()













