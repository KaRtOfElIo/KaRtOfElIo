from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Lesson_7.data import *
from  Lesson_7.constants import Test_form_URL

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Test_form_URL)
# Находим необходимые поля для заполнения на главной странице
def find_fields(self, send_keys=None):
    self.first_name = (By.NAME, "first-name")
    self.last_name = (By.NAME, "last-name")
    self._address = (By.NAME, "address")
    self.email = (By.NAME, "e-mail")
    self.phone = (By.NAME, "phone")
    self.zip_code = (By.NAME, "zip-code")
    self.city = (By.NAME, "city")
    self.country = (By.NAME, "country")
    self.job_position = (By.NAME, "job-position")
    self.company = (By.NAME, "company")
    self.button = (By.TAG_NAME, "button")
    # Заполняем найденные поля
    def filling_in_the_fields(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position,
                              company):
        self.browser.find_element(*self.first_name).send_keys(first_name)
        self.browser.find_element(*self.last_name).send_keys(last_name)
        self.browser.find_element(*self.address).send_keys(address)
        self.browser.find_element(*self.email).send_keys(email)
        self.browser.find_element(*self.phone).send_keys(phone)
        self.browser.find_element(*self.zip_code).send_keys(zip_code)
        self.browser.find_element(*self.city).send_keys(city)
        self.browser.find_element(*self.country).send_keys(country)
        self.browser.find_element(*self.job_position).send_keys(job_position)
        self.browser.find_element(*self.company).send_keys(company)


# Нажимаем на кнопку подтверждения
def click_submit_button(self):
    WebDriverWait(self.browser, 40, 0.1).until(EC.element_to_be_clickable(self.button)).click()

