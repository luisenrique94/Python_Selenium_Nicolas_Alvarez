from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("tucorreo@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_id("password")
password.send_keys("12345")
password.send_keys(Keys.ENTER)