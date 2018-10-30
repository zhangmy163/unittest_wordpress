import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
print(BASE_DIR)
from page_obj.loginpage import LoginPage
from selenium import webdriver
import unittest

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.page = LoginPage(cls.dr)
        cls.page.get("http://39.105.110.85:8000/wp-login.php")
    @classmethod
    def setTearDown(cls):
        cls.dr.quit()

    def testlogin(self):
        # page.loginsuccess(user,passwd)
        user = 'pyse19'
        passwd = 'pyse19'
        self.page.loginsuccess(user,passwd)

if __name__ == '__main__':
    unittest.main()
