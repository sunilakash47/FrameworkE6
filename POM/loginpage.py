from Generic.read_excel_data import *

class LoginPage(ExcelRead):
    def __init__(self, driver):
        self.driver = driver
        self.d = self.read_locator("LoginPage")
    def username(self, data):
        # self.driver.find_element("id", "username").send_keys(data)
        self.driver.find_element(*self.d["username"]).send_keys(data)
    def password(self, data):
        # self.driver.find_element("name", "pwd").send_keys(data)
        self.driver.find_element(*self.d["password"]).send_keys(data)
    def login_button(self):
        # self.driver.find_element("id", "loginButton").send_keys(data)
        self.driver.find_element(*self.d["login_button"]).click()
    










