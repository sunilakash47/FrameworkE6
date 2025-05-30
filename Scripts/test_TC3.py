from Generic.assertion import *
from Generic.verification import *
from POM.homepage import *
from POM.loginpage import *
from POM.timetrack_page import *
from POM.create_newtask_page import *

def test_TC3(launch):
    driver = launch
    verify_title("actiTIME - Login", driver)
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title("actiTIME - Enter Time-Track", driver)
    verify_text("Administrator System", driver)
    t = TimeTrackPage(driver)
    t.select_user()
    verify_title("actiTIME - Enter Time-Track", driver)
    t.new_link()
    c = CreateNewTaskPage(driver)
    c.customer_name("ICICI Bank")
    c.project_name("mobile application")
    c.task_name("write scenario and testcase")
    c.estimate_time("9")
    c.create_task()
    verify_text("write scenario and testcase", driver)
    h = HomePage(driver)
    h.logout_link()
    verify_title("actiTIME - Login", driver)
    l = LoginPage(driver)
    l.username("seleniumauto")
    l.password("selenium@123")
    l.login_button()
    verify_title("actiTIME - Enter Time-Track", driver)
    verify_text("selenium automation", driver)
    t.enter_estimate_time(9)
    t.save_changes()
    h.logout_link()
    verify_title("actiTIME - Login", driver)
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title("actiTIME - Enter Time-Track", driver)
    verify_text("Administrator System", driver)
    t.select_user()
    verify_text("9", driver)












