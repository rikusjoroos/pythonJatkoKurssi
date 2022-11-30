from getkey import *
import time

######################################
#
# Don't touch the main loop and related variables
events={}
active_mainloop=True

def mainloop():
    init_mainloop()

    print('Enter mainloop()')
    while active_mainloop:
        k=get_key()
        if k!='':
            if k in events:
                f=events[k]
                f()
        else:
            time.sleep(0.01)
    print('Exit mainloop()')
    clean_mainloop()
######################################
count = 0
total = 0

def add_numbers(number):
    global total
    global count
    global active_mainloop
    total = total + number
    count = count + 1
    print(total)
    if count == 10:
        active_mainloop = False

    
def zero_pressed():
    number = 0
    add_numbers(number)
    
def one_pressed():
    number = 1
    add_numbers(number)

def two_pressed():
    number = 2
    add_numbers(number)
    
def three_pressed():
    number = 3
    add_numbers(number)
    
def four_pressed():
    number = 4
    add_numbers(number)
    
def five_pressed():
    number = 5
    add_numbers(number)
    
def six_pressed():
    number = 6
    add_numbers(number)
    
def seven_pressed():
    number = 7
    add_numbers(number)
    
def eight_pressed():
    number = 8
    add_numbers(number)
    
def nine_pressed():
    number = 9
    add_numbers(number)
    

events['0'] = zero_pressed
events['1'] = one_pressed
events['2'] = two_pressed
events['3'] = three_pressed
events['4'] = four_pressed
events['5'] = five_pressed
events['6'] = six_pressed
events['7'] = seven_pressed
events['8'] = eight_pressed
events['9'] = nine_pressed





    

######################################
#
#Don't modify lines below
if __name__ == "__main__":
    mainloop()
