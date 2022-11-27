# -*- coding: utf-8 -*-
from getkey import *
import time

events = {}

active_mainloop = True

def mainloop():
    init_mainloop()
    print("Enter mainloop")
    while active_mainloop:
        k = get_key()
        if k != '':
            if k in events:
                f = events[k]
                f()
        else:
            time.sleep(0.01)
    print("Exit mainloop")
        
    clean_mainloop()

touchedB = False
def a_pressed():
    global touchedB
    if touchedB:
        print("B have been pressed")
    print('a pressed')
    
def b_pressed():
    global touchedB
    touchedB = True
    print('b pressed')
    
def x_pressed():
    global active_mainloop
    print('x pressed')
    active_mainloop= False    
    
events['a'] = a_pressed
events['x'] = x_pressed
events['b'] = b_pressed


mainloop()