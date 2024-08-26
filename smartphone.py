# lesson_3_task_2.py

class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand
        self.model = model
        self.phone_number = phone_number

# Создание переменной catalog, которая хранит список экземпляров Smartphone
catalog = [
    Smartphone("Apple", "iPhone 14", "+7123456"),
    Smartphone("Samsung", "Galaxy S21", "+7875335"),
    Smartphone("Xiaomi", "Mi 11", "+4567999"),
    Smartphone("OnePlus", "9 Pro", "+65676544"),
    Smartphone("Google", "Pixel 6", "+87765333")
]

# Цикл для печати всего каталога
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.phone_number}")