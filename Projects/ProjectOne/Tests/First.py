from selenium import webdriver
import time
import unittest
from Projects.ProjectOne.Pages.loginPage import LoginPage
from Projects.ProjectOne.Pages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/arun/PycharmProjects/Project1/Executables/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        home = HomePage(driver)
        home.click_welcome()
        home.click_logout()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test completed")


if __name__ == '__main__':
    unittest.main()