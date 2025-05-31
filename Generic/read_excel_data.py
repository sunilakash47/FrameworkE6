from xlrd import *

class ExcelRead:
    def read_locator(self, sheetname):
        d = {}              #d={'customer_name': ('name', 'customerName'), 'project_name': ('name', 'projectName'), 'task_name': ('name', 'task[0].name'), 'estimate_time': ('name', 'task[0].budgetedTimeStr'), 'create_task': ('xpath', "//input[@value='Create Tasks']")}
        wb = open_workbook("../Excelfiles/Locators.xlsx")
        sh = wb.sheet_by_name(sheetname)
        row_count = sh.nrows
        for i in range(1, row_count):
            data = sh.row_values(i)     #data = [componet name, locator name, locatr value]
            d[data[0]]  = (data[1], data[2])
        return d








