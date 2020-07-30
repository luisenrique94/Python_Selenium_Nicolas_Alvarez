import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_something(self):
        driver = self.driver
        palabra_busqueda = "sele"
        driver.get("https://www.google.com")
        time.sleep(5)
        busqueda = driver.find_element_by_name("q").send_keys(palabra_busqueda)
        time.sleep(5)
        for i in range(1,11):
            elementos = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span/b").text
            print(palabra_busqueda + elementos)
            driver.close()


if __name__ == '__main__':
    unittest.main()
