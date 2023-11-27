from typing import List

from service import Point3D, Angle3D, Color, Type


class Poligon:
    def __init__(self, points: List[Point3D]=[]):
        self.points:List[Point3D] = self.set_points(points)

    def set_points(self, points: List[Point3D]) -> None:
        if points:
            self.points = points
        else:
            self.points = [Point3D()]


class Texture:
    pass


class PoligonalModel:
    def __init__(self, textures: List[Texture]=[]):
        self.poligons: List[Poligon] = []
        self.textures: List[Texture] = textures
        self.poligons.append(Poligon(Point3D()))


class Flash:
    def __init__(self, power=1.0):
        self.location: Point3D = Point3D()
        self.angle: Angle3D = Angle3D()
        self.color: Color = Color()
        self.power: float = power

    def rotate(self, angle: Angle3D) -> None:
        self.angle = angle

    def move(self, point_3d: Point3D) -> None:
        self.location = point_3d


class Camera:
    def __init__(self):
        self.location: Point3D = Point3D()
        self.angle: Angle3D = Angle3D()

    def rotate(self, angle: Angle3D) -> None:
        self.angle = angle

    def move(self, point_3d: Point3D) -> None:
        self.location = point_3d


class Scene:

    def __init__(
        self,
        id: int,
        models: List[PoligonalModel],
        cameras: List[Camera],
        flashes: List[Flash]=[]
    ):
        self.id: int = id
        self.flashes = flashes
        if len(models) > 0:
            self.models = models
        else:
            raise Exception("Должна быть хотя бы одна модель")
        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception("Должна быть хотя бы одна камера")

    def method1(self, some_obj: Type) -> Type:
        pass

    def method2(self, some_obj_1: Type, some_obj_2: Type) -> Type:
        pass
