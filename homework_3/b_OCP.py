# Переписать код SpeedCalculation в соответствии с Open-Closed Principle.
# ​Подсказка:
# создайте два дополнительных класса Car и Bus(наследников Vehicle),напишите метод calculateAllowedSpeed().
# Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP
from abc import ABC, abstractmethod


class ISpeedCalculation(ABC):

    @abstractmethod
    def calculate_allowed_speed(self):
        pass


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        pass


class Car(Vehicle, ISpeedCalculation):
    def __init__(self,  max_speed, brand):
        super().__init__(max_speed)
        self.brand = brand

    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8

    def get_type(self):
        return 'Car'


class Bus(Vehicle, ISpeedCalculation):
    def __init__(self,  max_speed, brand):
        super().__init__(max_speed)
        self.brand = brand

    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6

    def get_type(self):
        return 'Bus'


# НИЖЕ - ПЕРВОНАЧАЛЬНЫЙ КОД

# class SpeedCalculation:
#     def calculate_allowed_speed(self, vehicle):
#         if vehicle.get_type().lower() == "car":
#             return vehicle.get_max_speed() * 0.8
#         elif vehicle.get_type().lower() == "bus":
#             return vehicle.get_max_speed() * 0.6
#         return 0.0

# class Vehicle:
#     def init(self, max_speed, type):
#         self.max_speed = max_speed
#         self.type = type

#     def get_max_speed(self):
#         return self.max_speed

#     def get_type(self):
#         return self.type