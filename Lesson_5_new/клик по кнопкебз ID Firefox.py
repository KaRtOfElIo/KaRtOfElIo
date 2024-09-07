from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from time import sleep

# Указываем путь к драйверу Firefox (GeckoDriver)
service = Service(executable_path="путь_к_драйверу/geckodriver")
driver = webdriver.Firefox(service=service)

try:
    count = 0
    driver.get("http://uitestingplayground.com/dynamicid")
    
    for _ in range(3):
        blue_button = driver.find_element(
            "xpath", "//button[text()='Button with Dynamic ID']").click()
        count = count + 1
        sleep(2)
        
    print(count)

except Exception as ex:
    print(ex)

finally:
    driver.quit()
