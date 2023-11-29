# Переписать код SpeedCalculation в соответствии с Open-Closed Principle.
# ​Подсказка:
# создайте два дополнительных класса Car и Bus(наследников Vehicle),напишите метод calculateAllowedSpeed().
# Использование этого метода позволит сделать класс SpeedCalculation соответствующим OCP


class Vehicle:
    def __init__(self, max_speed, type):
        self.max_speed = max_speed
        self.type = type

    def get_max_speed(self):
        return self.max_speed

    def get_type(self):
        return self.type


class Car(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.8


class Bus(Vehicle):
    def calculate_allowed_speed(self):
        return self.get_max_speed() * 0.6


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