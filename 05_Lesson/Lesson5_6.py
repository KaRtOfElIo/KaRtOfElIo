from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Firefox()

try:
    driver.get("http://the-internet.herokuapp.com/login")
    
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")
    sleep(1)
    
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")
    sleep(1)
    
    login_button = driver.find_element(By.TAG_NAME, "button")
    login_button.click()
    
    sleep(2)
    
except Exception as ex:
    print(ex)
    
finally:
    driver.quit()
