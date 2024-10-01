from Lesson_7.Swag_Labs.Pages.Shopmain import ShopmainPage
from Lesson_7.Swag_Labs.Pages.Shopcontainer import ShopContainer


def test_shop(chrome_browser):
    expected_total = "58.29"  # Ожидаемая итоговая сумма
    shopmain = ShopmainPage(chrome_browser)

    shopmain.registration_fields()  # Регистрация
    shopmain.buy_issue()  # Выбор товаров
    shopmain.click_issue()  # Клик на добавление товаров
    shopmain.into_container()  # Переход в корзину

    container = ShopContainer(chrome_browser)
    container.checkout()  # Оформление заказа
    container.info()  # Ввод данных получателя

    total_price = container.price()  # Получаем итоговую сумму
    assert expected_total in total_price  # Проверяем, что итоговая сумма равна $58.29
    print(f"Итоговая сумма равна ${total_price}")
