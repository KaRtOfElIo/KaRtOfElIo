from selenium.webdriver.common.by import By
from Lesson_7.constants import Shop_URL

class ShopMainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Shop_URL)

    # Заполняем поля для регистрации
    def registration_fields(self):
        self.name = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.log_button = (By.ID, "login-button")

        self.browser.find_element(*self.name).send_keys("standard_user")
        self.browser.find_element(*self.password).send_keys("secret_sauce")
        self.browser.find_element(*self.log_button).click()

    def buy_items(self):
        self.sauce_labs_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.sauce_labs_bolt_tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.sauce_labs_onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    def click_items(self):
         self.browser.find_element(*self.sauce_labs_backpack).click()  # Клик по кнопке рюкзака
         self.browser.find_element(*self.sauce_labs_bolt_tshirt).click()  # Клик по кнопке футболки
         self.browser.find_element(*self.sauce_labs_onesie).click()  # Клик по кнопке комбинезона

    def into_container(self):
        self.container = (By.ID, "shopping_cart_container")  # Исправлено имя переменной
        self.browser.find_element(*self.container).click()  # Кликаем по корзине