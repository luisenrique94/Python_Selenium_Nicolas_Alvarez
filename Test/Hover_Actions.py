import unittest
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver import  ActionChains
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_something(self):
        driver = self.driver
        driver.get("https://google.com")
        time.sleep(3)
        elem = driver.find_element_by_link_text("Privacidad")
        hover = ActionChains(driver).move_to_element(elem)
        hover.perform()


if __name__ == '__main__':
    unittest.main()
