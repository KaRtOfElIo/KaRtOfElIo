from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep

# Указываем путь к драйверу Firefox (GeckoDriver)
service = Service(executable_path="путь_к_драйверу/geckodriver")
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://uitestingplayground.com/classattr")
    
    for _ in range(3):
        blue_button = driver.find_element(
            "xpath", 
            "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
        )
        blue_button.click()
        sleep(2)
        driver.switch_to.alert.accept()

except Exception as ex:
    print(ex)

finally:
    driver.quit()
