import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)
        self._driver.maximize_window()

    @allure.step("Установка задержки перед выполнением следующего шага")
    def delay(self, seconds: int):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input[id = "delay"]')
        input_delay.clear()
        input_delay.send_keys(str(seconds))

    @allure.step("Ввод чисел в калькулятор и запуск операции сложения")
    def sum_of_the_numbers(self, num1: int, num2: int):
        self._driver.find_element(By.XPATH, f'//span[contains(text(),"{num1}")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"+")]').click()
        self._driver.find_element(By.XPATH, f'//span[contains(text(),"{num2}")]').click()
        self._driver.find_element(By.XPATH, '//span[contains(text(),"=")]').click()

    @allure.step("Получение результата сложения")
    def get_result(self):
        WebDriverWait(self._driver, 48).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15"))
        return self._driver.find_element(By.CSS_SELECTOR, "div.screen").text

    @allure.step("Закрытие драйвера веб-браузера")
    def close_driver(self):
        self._driver.quit()

