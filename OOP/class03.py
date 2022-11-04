# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:05:57 2022

@author: riku.sjoroos
"""

class Base:
    def __init__(self):
        self.a = "in base"
    
    def modify(self, v):
        self.a = v
        
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.b = "in derived"
        
obj1 = Derived()

print(obj1.a)

obj1.modify("modified")

print(obj1.a, obj1.b)

