from Lesson_7.Data_types.Pages.MainPage import MainPage
from Lesson_7.Data_types.Pages.DataFields import DataField
def test_assertion(chrome_browser):
    # Инициализация главной страницы
    main_page = DataField(chrome_browser)
    main_page.find_fields()  # Находим поля для заполнения
    main_page.filling_in_the_fields()  # Заполняем поля
    main_page.click_submit_button()  # Подтверждаем заполнение формы

    # Инициализация страницы данных
    data_field = DataField(chrome_browser)
    data_field.find_fields()

    # Получаем значения классов полей
    class_first_name = data_field.get_class_first_name()
    class_last_name = data_field.get_class_last_name()
    class_address = data_field.get_class_address()
    class_phone = data_field.get_class_phone()
    class_city = data_field.get_class_city()
    class_country = data_field.get_class_country()
    class_job_position = data_field.get_class_job_position()
    class_company = data_field.get_class_company()
    class_zip_code = data_field.get_class_zip_code()

    assert "success" in data_field.get_class_first_name()
    assert "success" in data_field.get_class_last_name()
    assert "success" in data_field.get_class_address()
    assert "success" in data_field.get_class_phone()
    assert "success" in data_field.get_class_city()
    assert "success" in data_field.get_class_country()
    assert "success" in data_field.get_class_job_position()
    assert "success" in data_field.get_class_company()
    assert "danger" in data_field.get_class_zip_code()
