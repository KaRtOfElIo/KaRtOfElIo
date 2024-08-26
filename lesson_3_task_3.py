from Address import Address 
from Mailing import Mailing
cost_track= Mailing ("83838", "ЕЕ29292929")
to_address = Address("123456", "Москва", "Тверская" "2", "2")
from_address = Address("654321", "Санкт-Петербург", "Невский","2", "2")
print(f"Отправление от {from_address} до {to_address}")
print(f"Стоимость: {cost_track} руб.")