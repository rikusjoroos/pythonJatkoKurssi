# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 17:12:52 2022

@author: riku.sjoroos
"""

class Base:
    def __init__(self):
        self.a = "public"
        self._b = "protected"
        self.__c = "private"
     
    
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class:")   
        print(self._b)
        try:
            print("calling private member of base class:")
            print(self.__c)
        except:
            print("got exception")
  

base1 = Derived()
#print(base1.a)      
#print(base1._b)
#print(base1.__c)      