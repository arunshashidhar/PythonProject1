import unittest
from selenium import webdriver


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Safari()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()


    def test_1(self):
        self.driver.get("http://selenium-python.readthedocs.io/getting-started.html")


    def test_2(self):
        self.driver.get("https://www.google.co.in/")

    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    
    
