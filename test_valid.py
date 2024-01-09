#başarılı giriş

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from selenium.webdriver.common.keys import Keys

class test_login:
    def web_page(self):
       self.driver = webdriver.Chrome()
       self.driver.get("https://tobeto.com/giris")
       self.driver.maximize_window()
       sleep(2)

    
    
    def test_validLogin(self):   
       self.web_page()
       email = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "email")))
       email.send_keys("aybuke.toksoy@gmail.com")
       
       password = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.NAME, "password")))
       password.send_keys("123456")
       
       
       loginButton = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary w-100 mt-6']")))
       loginButton.click()

     
       #assert self.driver.find_element(By.CSS_SELECTOR, ".toast-header").text == "TOBETO "
       loginMessage = WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div[class='toast-body']")))
       assert loginMessage.text == "• Giriş başarılı."
      
       sleep(5)

     
    
testClass = test_login()
testClass.test_validLogin()





  