import unittest
import unittest
from  selenium import webdriver
import time
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
       # self.Ie = webdriver.Ie(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\IEDriverServer.exe")
        self.driver.maximize_window()


    def test_1(self):
        self.driver.get("http://www.google.com/")
        self.busqueda= self.driver.find_element_by_name("q")
        self.busqueda.send_keys("selenium")
        self.busqueda.submit()
        time.sleep(5)

    def test_2(self):
        self.driver.get("https://www.falabella.com.pe/falabella-pe/")
        driver = self.driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)
        driver.close()

    def test_3(self):
        self.driver.get("https://www.w3schools.com/html/html_tables.asp")
        valor = self.driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text
        print(valor)
        rows = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
        col = len(self.driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))
        print(rows)
        print(col)
        for n in range(2, rows + 1):
            for b in range(1, col + 1):
                dato = self.driver.find_element_by_xpath(
                    "//*[@id='customers']/tbody/tr[" + str(n) + "]/td[" + str(b) + "]").text
                print(dato, end='         ')
            print()

        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultados de mi test plan'))
