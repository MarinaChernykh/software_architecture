# Переписать код в соответствии с Dependency Inversion Principle.
# Разорвать зависимость классов Car и PetrolEngine. У машины же может быть DieselEngine.
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


class PetrolEngine(Engine):
    def start(self):
        pass


class Car(PetrolEngine):
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


# НИЖЕ - ПЕРВОНАЧАЛЬНЫЙ КОД

# class Car:
#     def __init__(self, engine):
#         self.engine = engine

#     def start(self):
#         self.engine.start()

# class PetrolEngine:
#     def start(self):
#         pass