# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 20:54:54 2022

@author: riku.sjoroos
"""

class Vehicle:
    next_reg = 0
    
    def __init__(self, x_init = 0.0, r = -1):
        print("Constructor")
        self._x = x_init
        self.reg = Vehicle.get_next_reg()
        
        
    @staticmethod
    def get_next_reg(increase = True):
        if increase:
            Vehicle.next_reg = Vehicle.next_reg + 1
        else:
            return Vehicle.next_reg + 1
        
        Vehicle.next_reg = Vehicle.next_reg + 1
        return Vehicle.next_reg
        
    
    
    def __del__(self):
        print("Destructor")
        
    def drive(self, v, t):
        print("Drive", v, t)
        self.x = self._x + (v * t)
    
    def get_x(self):
        print("x getter")
        return self._x
    
    def set_x(self, v):
        print("x setter")
        self._x = v
        
    x = property(get_x, set_x)
    
    

car = Vehicle(1000)

print("car.x =", car.x)
car.drive(100, 0.5)
print("car.x =", car.x)
car.x = -700
print("car.x =", car.x)

cars = []
N = 4


for i in range(N):
    cars.append(Vehicle())
    
for c in cars:
    print(c.reg, c.x)

cars.append(Vehicle())



del car

    