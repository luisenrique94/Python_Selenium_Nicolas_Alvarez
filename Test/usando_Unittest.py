import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        self.driver.maximize_window()
    def test_google(self):
        elemento= self.driver.find_element_by_name("q")
        elemento.send_keys("selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontro el elemento:" not in self.driver.page_source

    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
