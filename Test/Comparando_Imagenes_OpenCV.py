import unittest
from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
import cv2
import time

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\Luis\\Desktop\\Python_Selenium_Nicolas_Alvarez\\Drivers\\chromedriver.exe")

    def test_something(self):
        driver = self.driver
        driver.get("http://google.com")
        driver.save_screenshot('img2.png')
        time.sleep(3)
    def test_comparando_imagenes(self):
        img1= cv2.imread('img1.png')
        img2= cv2.imread('img2.png')
        diferencia = cv2.absdiff(img1,img2)
        imagen_gris = cv2.ctvColor(diferencia, cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)



if __name__ == '__main__':
    unittest.main()
