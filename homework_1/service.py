
class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x: float = x
        self.y: float = y
        self.z: float = z


class Angle3D:
    def __init__(self, angle=0):
        self.angle: int = angle


class Color:
    def __init__(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b


class Type:
    def __init__(self):
        pass
