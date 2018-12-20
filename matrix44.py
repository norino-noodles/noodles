from __future__ import annotations
import math

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
                                        