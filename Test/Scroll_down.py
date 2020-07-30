import unittest
from  selenium import webdriver
import time
class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.falabella.com.pe/falabella-pe/")
    def test_something(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        driver.close()



if __name__ == '__main__':
    unittest.main()
