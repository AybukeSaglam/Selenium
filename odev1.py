from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_SauceOdev:
    def test_username(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.get("https://www.saucedemo.com")
       driver.maximize_window() #ekranı büyütür
       sleep(5)
       usernameInput = driver.find_element(By.ID,"user-name")
       usernameInput.send_keys("")
       sleep(5)
       passwordInput = driver.find_element(By.ID,"password")
       passwordInput.send_keys("")
       sleep(5)
       loginButton = driver.find_element(By.ID,"login-button")
       loginButton.click()
       sleep(5)
       errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       testResult = errorMessage.text == "Epic sadface: Username is required"
       print(f"TEST SONUCU: {testResult}")


    def test_password(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.get("https://www.saucedemo.com")
       driver.maximize_window() #ekranı büyütür
       sleep(5)
       usernameInput = driver.find_element(By.ID,"user-name")
       usernameInput.send_keys("locked_out_user")
       sleep(5)
       passwordInput = driver.find_element(By.ID,"password")
       passwordInput.send_keys("")
       sleep(5)
       loginButton = driver.find_element(By.ID,"login-button")
       loginButton.click()
       sleep(5)
       errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       testResult = errorMessage.text == "Epic sadface: Password is required"
       print(f"TEST SONUCU: {testResult}")



    def test_invalid_login(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.get("https://www.saucedemo.com")
       driver.maximize_window() #ekranı büyütür
       sleep(5)
       usernameInput = driver.find_element(By.ID,"user-name")
       usernameInput.send_keys("locked_out_user")
       sleep(5)
       passwordInput = driver.find_element(By.ID,"password")
       passwordInput.send_keys("secret_sauce")
       sleep(5)
       loginButton = driver.find_element(By.ID,"login-button")
       loginButton.click()
       sleep(5)
       errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
       testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
       print(f"TEST SONUCU: {testResult}")

    def test_valid_login(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       driver.get("https://www.saucedemo.com")
       driver.maximize_window() #ekranı büyütür
       sleep(5)
       usernameInput = driver.find_element(By.ID,"user-name")
       usernameInput.send_keys("standard_user")
       sleep(5)
       passwordInput = driver.find_element(By.ID,"password")
       passwordInput.send_keys("secret_sauce")
       sleep(5)
       loginButton = driver.find_element(By.ID,"login-button")
       loginButton.click()
       sleep(5)
       listOfCourses = driver.find_elements(By.CLASS_NAME, "inventory_item")
       testResult = len(listOfCourses) == 6
       print(f"TEST SONUCU: {testResult}")


testClass = Test_SauceOdev()
testClass.test_username()
testClass.test_password()
testClass.test_invalid_login()
testClass.test_valid_login()