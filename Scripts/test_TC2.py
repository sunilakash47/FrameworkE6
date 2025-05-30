from Generic.verification import *
from POM.loginpage import *
from Generic.assertion import *
from POM.homepage import *
from POM.userlist_page import *

def test_TC2(launch):
    driver = launch
    verify_title("actiTIME - Login", driver)
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title("actiTIME - Enter Time-Track", driver)
    verify_text("Administrator System", driver)
    h = HomePage(driver)
    h.user_tab()
    verify_title("actiTIME - User List", driver)
    u = UserListPage(driver)
    u.user_button()
    verify_text("Create New User", driver)
    u.first_name("selenium")
    u.last_name("automation")
    u.email("seleniumauto@gmail.com")
    u.username("seleniumauto")
    u.password("selenium@123")
    u.retype_password("selenium@123")
    u.create_user_button()
    verify_text("automation, selenium (seleniumauto)", driver)
    h.logout_link()
    verify_title("actiTIME - Login", driver)
    l.username("seleniumauto")
    l.password("selenium@123")
    l.login_button()
    verify_title("actiTIME - Enter Time-Track", driver)
    verify_text("selenium automation", driver)
    h.logout_link()
    verify_title("actiTIME - Login", driver)


