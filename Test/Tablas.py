import unittest
from selenium import webdriver
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.w3schools.com/html/html_tables.asp")
    def test_something(self):
        valor = self.driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
        print(valor)
        rows= len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        col= len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
        print(rows)
        print(col)
        for n in range(2,rows+1):
            for b in range(1, col+1):
                dato = self.driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(n)+"]/td["+str(b)+"]").text
                print(dato, end= '         ')
            print()

        time.sleep(5)



if __name__ == '__main__':
    unittest.main()
