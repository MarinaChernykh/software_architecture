# Переписать код в соответствии с Liskov Substitution Principle.
from abc import ABC, abstractmethod

class IRectangle(ABC):
    @abstractmethod
    def set_width(self, width):
        pass

    @abstractmethod
    def set_height(self, height):
        pass

    @abstractmethod
    def area(self):
        pass


class Rectangle(IRectangle):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def area(self):
        return self.width * self.height


class Square(IRectangle):
    def __init__(self, side):
        self.side = side

    def set_width(self, width):
        self.side = width

    def area(self):
        return self.side * self.side



# НИЖЕ - ПЕРВОНАЧАЛЬНЫЙ КОД

# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0

#     def setWidth(self, width):
#         self.width = width

#     def setHeight(self, height):
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Square(Rectangle):
#     def setWidth(self, width):
#         self.width = width
#         self.height = width

#     def setHeight(self, height):
#         self.width = height
#         self.height = height