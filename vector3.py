from __future__ import annotations
import math

class Vec3:

    def __init__(self, x: float=0, y: float=0, z: float=0):
        self.x = x
        self.y = y
        self.z = z

    def length(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def dot(self, v: Vec3) -> float:
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self, v: Vec3) -> Vec3:
        return Vec3(self.y * v.z - self.z * v.y, 
                    self.z * v.x - self.x * v.z,
                    self.x * v.y - self.y * v.x)

    def normalize(self) -> None:
        len = self.length()

        if (len > 0):
            invLen = 1 / len
            self.x = self.x * invLen
            self.y = self.y * invLen
            self.z = self.z * invLen

    def add(self, v: Vec3) -> Vec3:
        return Vec3(self.x + v.x. self.y + v.y, self.z + v.z)

    def subtract(self, v: Vec3) -> Vec3:
        return Vec3(self.x - v.x. self.y - v.y, self.z - v.z)

    def scale(self, c: float) -> Vec3:
        return Vec3(self.x * c. self.y * c, self.z * c)
    
    def __repr__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"

if __name__ == "__main__":
    vector1 = Vec3(2,2,2)
    print(vector1)
    print(vector1.length())
    vector1.normalize()
    print(vector1)