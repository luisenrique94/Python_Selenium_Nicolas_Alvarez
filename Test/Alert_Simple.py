import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
    def test_something(self):

        btn = self.driver.find_element_by_xpath("//iframe[@id='iframeResult']")
        btn.click()
        time.sleep(5)
        btn = self.driver.switch_to_alert()
        btn.dismiss()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
