import unittest
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        chomeOptions = Options()
        chomeOptions.add_experimental_option("prefs",{ "download.default_directory":
        "C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers" })

        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
    def test_something(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")
        time.sleep(4)
        driver.switch_to.frame(driver.find_element_by_xpath())



if __name__ == '__main__':
    unittest.main()
