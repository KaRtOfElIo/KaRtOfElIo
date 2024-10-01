from selenium.webdriver.common.by import By


class ShopContainer:
    def __init__(self, browser):
        self.browser = browser

    # Кликаем на кнопку checkout
    def checkout(self):
        self.check = (By.ID, "checkout")
        self.browser.find_element(*self.check).click()

    # Вводим данные получателя
    def info(self):
         self.first_name = (By.ID, "first-name")
         self.browser.find_element(*self.first_name).send_keys("Evgen")

         self.last_name = (By.ID, "last-name")
         self.browser.find_element(*self.last_name).send_keys("Voronov")

         self.postcode = (By.ID, "postal-code")
         self.browser.find_element(*self.postcode).send_keys("601500")

         self.continue_button = (By.ID, "continue")
         self.browser.find_element(*self.continue_button).click()
     # Получаем итоговую сумму заказа и выводим ее в нужном формате

    def price(self):
     # Ожидаем появления элемента с итоговой суммой
        total_price_element = WebDriverWait(self.browser, 10, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        # Извлекаем текст и форматируем его
        total = total_price_element.text.strip().replace("Total: $", "")
        return total