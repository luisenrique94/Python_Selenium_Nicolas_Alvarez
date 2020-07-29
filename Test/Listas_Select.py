import unittest
from  selenium import webdriver
from  selenium.webdriver.common.keys import  Keys
import time

from selenium.webdriver.support.select import Select


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_something(self):

        driver = self.driver
        driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
        driver.maximize_window()
        time.sleep(3)
        select = driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")
        opcion = select.find_element_by_tag_name("option")
        time.sleep(3)
        for option in opcion:
            print("Los valores son : %s" % option.get_attribute("value"))
            option.click()
            time.sleep(3)
        seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select"))
        seleccionar.select_by_value("10")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
