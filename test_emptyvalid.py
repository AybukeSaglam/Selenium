#Kullanıcı adı ve şifreyi boş bırakma

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

class test_login:
    def web_page(self):
       self.driver = webdriver.Chrome()
       self.driver.get("https://tobeto.com/giris")
       self.driver.maximize_window()
       sleep(2)

    
    
    def test_emptyLogin(self):   
       self.web_page()
       email = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "email")))
       email.send_keys("")
       
       password = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
       password.send_keys("")
       sleep(5)
       
       loginButton = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary w-100 mt-6']")))
       loginButton.click()

       sleep(5)
       quit()
      
       
    
testClass = test_login()
testClass.test_emptyLogin()