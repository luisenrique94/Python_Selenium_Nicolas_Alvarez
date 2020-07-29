import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_camviar_ventana(self):
        driver = self.driver
        driver.get("http://google.com")
        time.sleep(3)
        driver.execute_script("window.open('');")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1])
        driver.get("http://stackoverflow.com")
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
