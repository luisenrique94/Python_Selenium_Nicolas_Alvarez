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
        driver.get("https://www.google.com/")
        titulo = driver.title
        print(titulo)
        time.sleep(5)
        self.assertNotEqual("Google1", titulo, "el titulo de la pagina  es igual ")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
