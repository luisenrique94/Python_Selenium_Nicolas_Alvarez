import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_usando_Explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.NAME,"q")))
        finally:
            driver.quit()



if __name__ == '__main__':
    unittest.main()
