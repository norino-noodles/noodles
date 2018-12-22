from __future__ import annotations
import math
import vector3

class Matrix44:

    def __init__(self):
        self.m = [[1.0,0.0,0.0,0.0],[0.0,1.0,0.0,0.0],[0.0,0.0,1.0,0.0],[0.0,0.0,0.0,1.0]] # identity 4x4 matrix

    def get_entry(self, r: int, c: int) -> float:
        return self.m[r][c]
    
    def set_entry(self, r: int, c: int, v: float) -> None:
        self.m[r][c] = v

    def multiply(self, rhsM: Matrix44) -> Matrix44:
        result = Matrix44()

        for r in range(4):
            for c in range(4):
                result.set_entry(r, c, self.m[r][0] * rhsM.get_entry(0, c) +
                                        self.m[r][1] * rhsM.get_entry(1, c) +
                                        self.m[r][2] * rhsM.get_entry(2, c) +
                                        self.m[r][3] * rhsM.get_entry(3, c))

        return result

    """
    v: xyz vector
    return: xyz vector

    a 1x4 point times a 4x4 matrix
    """
    def multVecMatrix(self, v: Vec3) -> Vec3:
        result = Vec3():
        result.x = v.x * self.m[0][0] + v.y * self.m[1][0] + v.z * self.m[2][0] + self.m[3][0]
        result.y = v.x * self.m[0][1] + v.y * self.m[1][1] + v.z * self.m[2][1] + self.m[3][1]
        result.z = v.x * self.m[0][2] + v.y * self.m[1][2] + v.z * self.m[2][2] + self.m[3][2]
        w = v.x * self.m[0][3] + v.y * self.m[1][3] + v.z * self.m[2][3] + self.m[3][3]

        if (w != 1 && w != 0):
            result.x = result.x / w
            result.y = result.y / w
            result.z = result.z / w

        return result
    
    """
    v: xyz vector
    return: xyz vector

    a 1x4 vector times a 4x4 matrix (note: translation does not matter for vectors)
    """
    def multDirMatrix(self, v: Vec3) -> Vec3:
        result = Vec3():
        result.x = v.x * self.m[0][0] + v.y * self.m[1][0] + v.z * self.m[2][0]
        result.y = v.x * self.m[0][1] + v.y * self.m[1][1] + v.z * self.m[2][1]
        result.z = v.x * self.m[0][2] + v.y * self.m[1][2] + v.z * self.m[2][2]

        return result