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
        driver.get("https://mdbootstrap.com/plugins/jquery/file-upload")
        time.sleep(4)
        self.driver.find_element_by_id("input-file-now-custom-2").send_keys("C:\\Users\\Luis\\Desktop\\SPRING LOVE\\20191228_180018.jpg")
        time.sleep(4)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
