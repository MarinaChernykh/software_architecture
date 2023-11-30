from datetime import datetime
from decimal import Decimal
from typing import List


class Person:
    def __init__(self, id, last_name, first_name, patronymic, email, login, password):
        self._id: int = id
        self._last_name: str = last_name
        self._first_name: str = first_name
        self._patronymic: str = patronymic
        self._email: str = email
        self._login: str = login
        self._password: str = hash(password)
        # в процессе оплаты пользователь при желании может сохранить данные карты,
        # но может этого не делать
        self._card_number: int = None

    def get_id(self):
        return self._id

    def get_last_name(self):
        return self._last_name

    def get_first_name(self):
        return self._first_name

    def get_patronymic(self):
        return self._patronymic

    def get_email(self):
        return self._email

    def get_login(self):
        return self._login

    # Используется при смене пароля
    def set_password(self, password):
        # Проверка пароля на сложность и тд
        self._password = hash(password)

    # Используется для сохранения номера карты
    def set_card_number(self, card_number):
        # Проверка валидности номера карты
        self._card_number = hash(card_number)


class TransportZone:
    def __init__(self, id, comment):
        self._id: int = id
        self._comment: str = comment

    def get_id(self):
        return self._id

    def get_comment(self):
        return self._comment

    # Возможно нужно будет подкорректировать описание
    def set_comment(self, comment):
        self._comment = comment


class BusStop:
    def __init__(self, id, name, attitude, latitude, zone):
        self._id: int = id
        self._name: str = name
        self._attitude: int = attitude
        self._latitude: int = latitude
        self._zone: TransportZone = zone

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_attitude(self):
        return self._attitude

    def get_latitude(self):
        return self._latitude

    def get_zone(self):
        return self._zone

    # Зонирование может измениться
    # (например, при пересмотре тарифов решат сделать больше зон)
    def set_zone(self, zone):
        self._zone = zone


class BusRoute:
    def __init__(self, id, comment, capacity, bus_stops):
        self._id: int = id
        self._comment: str = comment
        self._capacity: int = capacity
        self.bus_stops: List[BusStop] = bus_stops

    def get_id(self):
        return self._id

    def get_comment(self):
        return self._comment

    # Возможно нужно будет подкорректировать описание
    def set_comment(self, comment):
        self._comment = comment

    def get_capacity(self):
        return self._capacity

    def get_bus_stops(self):
        return self._bus_stops

    # Возможно список остановок изменится (напр., появилась новая), поэтому предусмотрен сеттер
    def set_bus_stops(self, bus_stops):
        self._bus_stops = bus_stops


class Ticket:
    def __init__(self, id, price, date, start_point, finish_point, has_luggage, seat, bus_route):
        self._id: int = id
        self._price: Decimal = price
        self._date: datetime = date
        self._start_point: BusStop = start_point
        self._finish_point: BusStop = finish_point
        self._has_luggage: bool = has_luggage
        self._seat: int = seat
        self._bus_route: BusRoute = bus_route

    def get_id(self):
        return self._id

    def get_price(self):
        return self._price

    def get_date(self):
        return self._date

    def get_start_point(self):
        return self._start_point

    def get_finish_point(self):
        return self._finish_point

    def get_has_luggage(self):
        return self._has_luggage

    def get_seat(self):
        return self._seat

    def get_bus_route(self):
        return self._bus_route
