import unittest
from selenium import webdriver
from  selenium.webdriver.common.by import By
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
    def test_something(self):
        driver = self.driver
        driver.get("https://www.google.com/intl/es/gmail/about/#")
        crearcuenta=driver.find_element_by_xpath("//a[@class='h-c-button h-c-button--primary hero-carousel__cta hero-carousel__cta--reg']")
        crearcuenta.click()
        print(self.driver.current_window_handle)
        handles= self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            print(self.driver.title)
        time.sleep(5)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
