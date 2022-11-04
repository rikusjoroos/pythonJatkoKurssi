# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:22:21 2022

@author: riku.sjoroos
"""

from abc import ABC, abstractmethod

class Vehicle(ABC): #abstrakti luokka. tästä ei voi tehdä oliota
    def __init__(self):
        print("Vehicle.__init__()")
        self.x = 0.0
    
    @abstractmethod
    def drive(self, v, t):
        pass

class Car(Vehicle):
    def __init__(self):
        print("Car.__init__()")
        Vehicle.__init__(self)
        
    def drive(self, v, t):
        print("Car.drive()")
        self.x = self.x + (v*t)
        
car = Car()
car.drive(100, 2)
print("car position is: %02.f." %(car.x))