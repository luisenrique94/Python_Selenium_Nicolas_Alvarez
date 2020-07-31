import unittest
from selenium import  webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
driver.get("https://sandbox.chazki.com/#/login")
time.sleep(5)
#inicial ciclo de auto llenado
with open("C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Test\\login.txt") as file:
    for i, line  in enumerate(file):
        usuario = (line)
        sep = ","
        dividir = usuario.split(sep)
        try:
            gotdata = dividir[1]
            user = dividir[0]
            pas = dividir[1]
        except IndexError:
            gotdata='null'
        print(user)
        print(pas)
        driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[1]/span/input").clear()
        driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[1]/span/input").send_keys(user)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[2]/span/input").send_keys(pas)
        driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div/form/div/div[3]/button").click()
        time.sleep(2)
file.close()
driver.close()







if __name__ == '__main__':
    unittest.main()
