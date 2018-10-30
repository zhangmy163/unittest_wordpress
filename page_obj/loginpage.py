from .page_objects import PageObject,PageElement,PageElements
from selenium import webdriver
import unittest

class LoginPage(PageObject):

    username = PageElement(id_='user_login')
    password = PageElement(id_='user_pass')
    login_button = PageElement(css = '#wp-submit')

    def loginsuccess(self,user,passwd):
        self.username.send_keys(user)
        self.password.send_keys(passwd)
        self.login_button.click()
if __name__ == '__main__':
    dr = webdriver.Chrome()
    page = LoginPage(dr)
    page.get("http://39.105.110.85:8000/wp-login.php")
    page.loginsuccess('pyse19','pyse19')
