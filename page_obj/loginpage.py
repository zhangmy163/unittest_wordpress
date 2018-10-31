import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from page_obj.page_objects import PageObject,PageElement
from page_obj.dashboardpage import DashboardPage
from selenium import webdriver

class LoginPage(PageObject):

    username = PageElement(id_='user_login')
    password = PageElement(id_='user_pass')
    login_button = PageElement(css = '#wp-submit')

    def login(self,user,passwd):
        self.username.send_keys(user)
        self.password.send_keys(passwd)
        self.login_button.click()
        return DashboardPage(self.driver)
if __name__ == '__main__':
    dr = webdriver.Chrome()
    page = LoginPage(dr)
    page.get("http://39.105.110.85:8000/wp-login.php")
    page.login('pyse19','pyse19')
