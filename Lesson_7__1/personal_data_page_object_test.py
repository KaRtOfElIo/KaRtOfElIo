import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PersonalDataPage import PersonalDataPage


@allure.id("PersonalData")
@allure.epic("Персональные данные")
@allure.severity("blocker")
@allure.story("Заполнение персональных данных")
@allure.feature("CREATE")
@allure.title("Заполнить персональные данные")
@allure.suite("Тесты на работу формы с заполнением персональных данных")
def test_form_elements():
    with allure.step("Открытие веб-страницы Chrome"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Создание переменной, которая хранит экземпляр класса PersonalDataPage"):
        personal_data_page = PersonalDataPage(driver)

    personal_data_page.personal_data("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "79858999987", "Москва",
                                     "Россия", "QA", "SkyPro")

    assert personal_data_page.zip_code_red() == True, "Почтовый индекс не имеет красного цвета"
    assert personal_data_page.other_fields_green() == True, "Некоторые поля не имеют зеленого цвета"

    personal_data_page.close_driver()
