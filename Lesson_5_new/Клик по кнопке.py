from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    
    for _ in range(5):
        add_button = driver.find_element(By.XPATH, '//button[text()="Add Element"]')
        add_button.click()
    
    delete_buttons = driver.find_elements(By.CLASS_NAME, 'added-manually')
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    driver.quit()
