from Generic.read_excel_data import *

class CreateNewTaskPage(ExcelRead):
    def __init__(self, driver):
        self.driver = driver
        self.d = self.read_locator("CreateNewTaskPage")
    def customer_name(self, data):
        self.driver.find_element(*self.d["customer_name"]).send_keys(data)
    def project_name(self, data):
        self.driver.find_element(*self.d["project_name"]).send_keys(data)
    def task_name(self, data):
        self.driver.find_element(*self.d["task_name"]).send_keys(data)
    def estimate_time(self, data):
        self.driver.find_element(*self.d["estimate_time"]).send_keys(data)
    def create_task(self):
        self.driver.find_element(*self.d["create_task"]).click()
        allid = self.driver.window_handles
        self.driver.switch_to.window(allid[0])
    print("create new task page")








