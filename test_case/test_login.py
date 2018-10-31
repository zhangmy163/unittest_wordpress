import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from page_obj.loginpage import LoginPage
from page_obj.dashboardpage import DashboardPage
from selenium import webdriver
import unittest
from time import sleep

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.page = LoginPage(cls.dr)
        cls.page.get("http://39.105.110.85:8000/wp-login.php")
        sleep(3)
    @classmethod
    def setTearDown(cls):
        cls.dr.quit()

    def testlogin(self):
        # page.loginsuccess(user,passwd)
        user = 'pyse19'
        passwd = 'pyse19'
        dashpage = self.page.login(user,passwd)
        print(dashpage.name.text())

if __name__ == '__main__':
    unittest.main()
