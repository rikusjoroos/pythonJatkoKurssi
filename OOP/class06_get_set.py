# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:33:06 2022

@author: riku.sjoroos
"""

class Vehicle:
   
    
    def __init__(self):
        print("Constructor")
        self._x = 0.0
 
    def drive(self, v, t):
        self._x = self._x + (v * t)
        
    @property
    def x(self):
        print("x getter")
        return self._x
    
    @x.setter
    def x(self, v):
        print("x setter")
        self._x = v
        

car = Vehicle()
car.drive(20, 100)

car.x = 2

print("Car position is %02.f." %(car.x))        
        