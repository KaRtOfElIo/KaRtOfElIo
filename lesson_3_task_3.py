from Address import Address 
from Mailing import Mailing

# Создаем объекты Address с правильными аргументами
to_address = Address("123456", "Москва", "Тверская", "2", "2")
from_address = Address("654321", "Санкт-Петербург", "Невский", "2", "2")

# Создаем объект Mailing и связываем его с Address
cost_track = Mailing(to_address, from_address, 83838, "ЕЕ29292929")

# Печатаем информацию об отправлении
print(f"Отправление {cost_track.track} из {cost_track.from_address.index}, {cost_track.from_address.city}, {cost_track.from_address.street}, {cost_track.from_address.house} - {cost_track.from_address.apartment} в {cost_track.to_address.index}, {cost_track.to_address.city}, {cost_track.to_address.street}, {cost_track.to_address.house} - {cost_track.to_address.apartment}. Стоимость {cost_track.cost} рублей.")
