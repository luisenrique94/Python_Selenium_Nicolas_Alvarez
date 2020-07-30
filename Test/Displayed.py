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
        driver.get("https://google.com")
        time.sleep(3)
        display = driver.find_element_by_name("btnI")
        print(display.is_displayed())
        print(display.is_enabled())
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
