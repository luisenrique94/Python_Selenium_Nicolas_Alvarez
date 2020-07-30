from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome (executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.falabella.com.pe/falabella-pe/")
all_cookies = driver.get_cookies()
print(all_cookies)