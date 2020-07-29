import unittest
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

class Usando_xpath(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")


    def test_buscar_por_xpathgi(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        buscar_por_xpath = driver.find_element_by_xpath("//input[@name='q']")
        time.sleep(3)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN, Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
