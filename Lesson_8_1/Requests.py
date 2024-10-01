import requests
from EmployeesApi import WorkersApi

api = WorkersApi("https://x-clients-be.onrender.com")

def test_add_new_employee():
    # Создать новую компанию
    name = "DavingShop"
    descr = "Diving equipment"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # Получить список сотрудников
    employees_before = api.get_employees_list(companyId)
    len_before = len(employees_before)

    # Добавить нового сотрудника
    new_employee = api.create_employee(
        first_name="Artem",
        last_name="Vologdin",
        middle_name="Leonidovich",
        company_id=companyId,
        email="ar_daving@gmail.com",
        url="string",
        phone="89999999999",
        birthdate="1998-12-30",
        is_active=True
    )
    emp_id = new_employee["id"]

    # Получить список сотрудников новой компании
    employees_after = api.get_employees_list(companyId)
    len_after = len(employees_after)

    # Проверки
    assert len_after - len_before == 1
    assert employees_after[-1]["firstName"] == "Artem"
    assert employees_after[-1]["lastName"] == "Vologdin"
    assert employees_after[-1]["middleName"] == "Leonidovich"
    assert employees_after[-1]["companyId"] == companyId
    assert employees_after[-1]["phone"] == "89999999999"
    assert employees_after[-1]["birthdate"] == "1998-12-30"
    assert employees_after[-1]["isActive"] == True
    assert employees_after[-1]["id"] == emp_id

def test_get_employees_id():
    # Создать новую компанию
    name = "Что-то неизвестное"
    descr = "Просто расскажем"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Обращаемся к компании по ID
    companyId = new_company['id']

    # Получить список сотрудников новой компании
    employees_before = api.get_employees_list(companyId)
    len_before = len(employees_before)

    # Добавить нового сотрудника
    new_employee = api.create_employee(
        first_name="Иван",
        last_name="Медведев",
        middle_name="Сергеевич",
        company_id=companyId,
        email="midew346@mail.ru",
        url="string",
        phone="865837387609",
        birthdate="1999-07-10",
        is_active=True
    )
    emp_id = new_employee["id"]

    # Получить список сотрудников новой компании
    employees_after = api.get_employees_list(companyId)
    len_after = len(employees_after)

    # Проверки
    assert len_after - len_before == 1
    assert employees_after[-1]["firstName"] == "Иван"
    assert employees_after[-1]["lastName"] == "Медведев"
    assert employees_after[-1]["middleName"] == "Сергеевич"
    assert employees_after[-1]["companyId"] == companyId
    assert employees_after[-1]["phone"] == "865837387609"
    assert employees_after[-1]["birthdate"] == "1999-07-10"
    assert employees_after[-1]["isActive"] == True
    assert employees_after[-1]["id"] == emp_id

def test_patch_employee():
    # Создать новую компанию
    name = "ETS"
    descr = "Симулируем грузо-перевозки"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Добавить нового сотрудника
    new_employee = api.create_employee(
        first_name="Артём",
        last_name="Леонов",
        middle_name="Артёмович",
        company_id=new_id,
        email="gruz-rem@mail.ru",
        url="string",
        phone="86564567877",
        birthdate="1986-12-12",
        is_active=True
    )
    emp_id = new_employee["id"]

    # Изменить информацию по сотруднику
    edited_employee = api.edit_employee(
        employee_id=emp_id,
        last_name="Марков",
        email="sana-x@mail.ru",
        url="_Updated_",
        phone="Updated",
        is_active=False
    )

    # Проверки
    assert edited_employee["email"] == "sana-x@mail.ru"
    assert edited_employee["url"] == "_Updated_"
    assert edited_employee["isActive"] == False

def test_delete_employee():
    # Создать новую компанию
    name = "Окна"
    descr = "Видно всё"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Добавить нового сотрудника
    new_employee = api.create_employee(
        first_name="Марина",
        last_name="Перова",
        middle_name="Александровна",
        company_id=new_id,
        email="perova-mar@mail.ru",
        url="string",
        phone="865422377865",
        birthdate="1980-05-06",
        is_active=True
    )
    emp_id = new_employee["id"]

    # Удалить сотрудника
    deleted_employee = api.delete_employee(emp_id)

    # Проверка, что сотрудник был удален
    assert deleted_employee is not None, "Сотрудник не был удален"
