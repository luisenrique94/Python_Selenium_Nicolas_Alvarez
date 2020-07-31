import unittest
from  selenium import webdriver
import time

from selenium.webdriver import ActionChains


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
    def test_something(self):
       self.driver.get("https://nicolasalvarez.com")
       time.sleep(5)
       mouse_mov=self.driver.find_element_by_xpath("//li[@id='menu-item-68']/a")
       mouse_mov2=self.driver.find_element_by_xpath("//li[@id='menu-item-82']/a")
       movimiento=ActionChains(self.driver)
       movimiento.move_to_element(mouse_mov).move_to_element(mouse_mov2).click().perform()
       time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
