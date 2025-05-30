from Generic.verification import *
from POM.loginpage import *
from Generic.assertion import *
from POM.homepage import *

def test_TC1(launch):
    driver = launch

    verify_title("actiTIME - Login", driver)
    l = LoginPage(driver)
    l.username("admin")
    l.password("manager")
    l.login_button()
    verify_title("actiTIME - Enter Time-Track", driver)
    verify_text("Administrator System", driver)
    h = HomePage(driver)
    h.logout_link()
    verify_title("actiTIME - Login", driver)
















