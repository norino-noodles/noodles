from vector3 import Vec3

class rtsphere:

    def __init__(self, ctr: Vec3, r: float, sColor: Vec3, eColor: Vec3, transparency: float, reflection: float):
        self.center = ctr
        self.radius = r
        self.surfaceColor = sColor
        self.emmisionColor = eColor
        self.transparency = transparency
        self.reflection = reflection

    def intersect(self, rayPos: Vec3, rayDir: Vec3) -> bool:
        return True

