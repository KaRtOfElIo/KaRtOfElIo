from selenium.webdriver.common.by import By

class CalMain:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("Calculator_URL")  # Замените "Calculator_URL" на фактический URL

    # Находим элемент и устанавливаем время ожидания
    def insert_time(self):
        delay_input = self.browser.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(45)

    # Кликаем на элементы калькулятора поочередно
    def clicking_buttons(self):
        # Click on the buttons:
        # 7
        self.browser.find_element(By.XPATH, "//span[text() = '7']").click()
        # +
        self.browser.find_element(By.XPATH, "//span[text() = '+']").click()
        # 8
        self.browser.find_element(By.XPATH, "//span[text() = '8']").click()
        self.browser.find_element(By.XPATH, "//span[text() = '='").click()

    # Ожидаем появление элемента и преобразуем значение в текст
    def wait_button_get_text(self):
        # Ожидание завершения вычисления
        WebDriverWait(self.browser, 46).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "")
        )
        return self.browser.find_element(By.CLASS_NAME, "screen").text