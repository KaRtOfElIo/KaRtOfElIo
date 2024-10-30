import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage

@allure.id("Calculator")
@allure.epic("калькулятор")
@allure.severity("blocker")
@allure.suite("Тесты на работу с калькулятором")
@allure.story("Выполнение математических операций на калькуляторе")
@allure.title("Сложение чисел на калькуляторе")
@allure.feature("CREATE")
def test_form_calculator():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экземпляр класса CalculatorPage"):
        calculator_page = CalculatorPage(driver)

    calculator_page.delay(45)  # Установить задержку на 45 секунд
    calculator_page.sum_of_the_numbers(7, 8)  # Передача чисел для сложения
    result = calculator_page.get_result()

    assert result == "15", f"Ожидалось '15', но получено '{result}'"  # Проверка результата
    calculator_page.close_driver()
