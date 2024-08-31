from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

search_locator = "#elements"

driver.find_element(By.CLASS_NAME, "btn-primary")
  
sleep(5)