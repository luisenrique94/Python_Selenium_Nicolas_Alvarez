import unittest
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("http://www.google.com")
        myDynamicElement = driver.find_element_by_name("q")



if __name__ == '__main__':
    unittest.main()
