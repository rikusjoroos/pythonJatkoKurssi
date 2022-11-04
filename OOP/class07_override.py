# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:40:21 2022

@author: riku.sjoroos
"""

class Vect2d:
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y
    
    def __add__(self, v):
        return Vect2d(self.x + v.x, self.y+ v.y)

    def __sub__(self, v):
        return Vect2d(self.x - v.x, self.y - v.y)
    
    def __mul__(self , v):
        return Vect2d(self.x * v.x, self.y * v.y)
    
    def __truediv__(self , v):
        return Vect2d(self.x / v.x, self.y / v.y)

    def __str__(self):
        return "(%f, %f)"%(self.x, self.y)

v1 = Vect2d(1, 2)
v2 = Vect2d(3, 7)

print(v1 * v2)