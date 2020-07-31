import unittest
from  selenium import webdriver
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
    def test_something(self):
        driver = self.driver
        driver.get("http://google.com")
        time.sleep(4)
        click1 = driver.find_element_by_xpath("//*[@id='gbwa']/div/a")
        time.sleep(3)
        click1.click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath())



if __name__ == '__main__':
    unittest.main()
