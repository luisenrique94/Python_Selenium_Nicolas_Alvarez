import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_something(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        encontrar_link = driver.find_element_by_link_text('Learn PHP')
        encontrar_link.click()
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
