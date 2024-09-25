from selenium.webdriver.common.by import By
from configuration import *

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)

    # Ввод логина и пароля
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()

    # Добавление товаров в корзину
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    # Переход в корзину
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()

    # Оформление заказа
    chrome_browser.find_element(By.ID, "checkout").click()
    chrome_browser.find_element(By.ID, "first-name").send_keys("Evgen")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Voronov")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("601500")
    chrome_browser.find_element(By.ID, "continue").click()

    # Получение итоговой суммы
    total_price = chrome_browser.find_element(By.CLASS_NAME, "summary_total_label")
    total = total_price.text.strip().replace("Total: $", "")

    # Ожидаемая сумма
    expected_total = "58.29"

    # Проверяем, что итоговая сумма равна $58.29
    assert total == expected_total, f"Ожидаемая сумма {expected_total}, но получено {total}"

    # Выводим сообщение в случае успешного выполнения
    print(f"Итоговая сумма равна ${total}")