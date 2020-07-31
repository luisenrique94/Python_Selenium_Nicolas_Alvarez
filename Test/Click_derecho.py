import unittest
from  selenium import webdriver
from  selenium.webdriver.common.by import  By
from selenium.webdriver import ActionChains
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()

    def test_something(self):
        self.driver.get("http://nicolasalvarez.com")
        time.sleep(4)
        youtube = self.driver.find_element_by_xpath("//div[@class='inner-wrap clearfix']//i[@class='fa fa-youtube']")
        actions = ActionChains(self.driver)
        actions.context_click(youtube).perform()
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
