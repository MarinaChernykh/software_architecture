from abc import ABC, abstractmethod
from typing import List

from model_elements import PoligonalModel, Scene, Flash, Camera


class IModelChangeObserver(ABC):
    @abstractmethod
    def apply_update_model(self) -> None:
        pass


class IModelChanger(ABC):
    @abstractmethod
    def notify_change(self, sender) -> None:
        pass


class ModelStore(IModelChanger):
    def __init__(self, changeObservers: List[IModelChangeObserver]):
        self.models: List[PoligonalModel] = [PoligonalModel()]
        self.scenes: List[Scene] = [Scene(
            id=1,
            models=self.models,
            flashes=self.flashes
        )]
        self.flashes: List[Flash] = [Flash()]
        self.cameras: List[Camera] = [Camera()]
        self._change_observers = changeObservers

    def get_scene(self, id):
        for scene in self.scenes:
            if scene.id == id:
                return scene
        return None

    def notify_change(self, sender) -> None:
        return super().notify_change(sender)
