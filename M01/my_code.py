import sys
import time

class NumericString:
    def __init__(self, v):
         if v < 0:
             raise ValueError ("Vain positiiviset luvut käyvät")
         else:
             self.v = v
             print (self.v)
             
    def __add__(self, o):
       n1 = ""
       n2 = ""
       if type(o) == int:
           n2 = str(o)
       else:
           n2 = str(o.v)
       
       if type(self) == int:
            n1 = str(self)
       else:
            n1 = str(self.v)
           
       result=""
       
       if len(n1) - len(n2) > 0:
           adds = len(n1) - len(n2)
           n2 = adds*"0" + n2
       elif len(n2) - len(n1) > 0:
           adds2 = len(n2) - len(n1)
           n1 = adds2*"0" + n1
       
       for i in range(0, len(n1)):
           if int(n1[i]) + int(n2[i]) >= 10:
               result = result + str(int(n1[i]) + int(n2[i]) - 10)
           else:
               result = result + str(int(n1[i]) + int(n2[i]))
       return NumericString(int(result))
   
    def __radd__(self, o):
       n1 = ""
       n2 = ""
       if type(o) == int:
           n2 = str(o)
       else:
           n2 = str(o.v)
       
       if type(self) == int:
            n1 = str(self)
       else:
            n1 = str(self.v)
           
       result=""
       
       if len(n1) - len(n2) > 0:
           adds = len(n1) - len(n2)
           n2 = adds*"0" + n2
       elif len(n2) - len(n1) > 0:
           adds2 = len(n2) - len(n1)
           n1 = adds2*"0" + n1
       
       for i in range(0, len(n1)):
           if int(n1[i]) + int(n2[i]) >= 10:
               result = result + str(int(n1[i]) + int(n2[i]) - 10)
           else:
               result = result + str(int(n1[i]) + int(n2[i]))
       return NumericString(int(result))
   
    
    def __mul__(self, o):
       n1 = ""
       n2 = ""
       if type(o) == int:
            n2 = str(o)
       else:
            n2 = str(o.v)
        
       if type(self) == int:
             n1 = str(self)
       else:
             n1 = str(self.v)
       result=""
       
       if len(n1) - len(n2) > 0:
           adds = len(n1) - len(n2)
           n2 = adds*"0" + n2
       elif len(n2) - len(n1) > 0:
           adds2 = len(n2) - len(n1)
           n1 = adds2*"0" + n1
       
       for i in range(0, len(n1)):
           if int(n1[i]) * int(n2[i]) >= 10:
               mult = str(int(n1[i]) * int(n2[i]))
               result = result + mult[-1]
           else:
               result = result + str(int(n1[i]) * int(n2[i]))
       return NumericString(int(result))
   
    def __str__(self):
        return str(self.v)

    def __rmul__(self, o):
       n1 = ""
       n2 = ""
       if type(o) == int:
             n2 = str(o)
       else:
             n2 = str(o.v)
         
       if type(self) == int:
              n1 = str(self)
       else:
              n1 = str(self.v)
        
       result=""
       
       if len(n1) - len(n2) > 0:
           adds = len(n1) - len(n2)
           n2 = adds*"0" + n2
       elif len(n2) - len(n1) > 0:
           adds2 = len(n2) - len(n1)
           n1 = adds2*"0" + n1
       
       for i in range(0, len(n1)):
           if int(n1[i]) * int(n2[i]) >= 10:
               mult = str(int(n1[i]) * int(n2[i]))
               result = result + mult[-1]
           else:
               result = result + str(int(n1[i]) * int(n2[i]))
       return NumericString(int(result))

       
        


        

testest1 = NumericString(123)
testest2 = NumericString(12)
print("minä")
print(12 + testest2)
print("minä2")
print(testest1*testest2)
print("minä3")

print(type(testest1+testest2))


            
          
    


        

if __name__ == "__main__":
    #Sample test program you can use to test your implementation

    #Create test objects and test value limit
    o16=NumericString(16)
    try:
        print('Initializing with negative integer...', end=' ')
        o_exception=NumericString(-1)
        got_exception=False
    except:
        got_exception=True

    assert got_exception
    print('Got exception -- ok')
    
    o124=NumericString(124)
    o19=NumericString(19)
    o0=NumericString(0)
    o1=NumericString(1)

    def test(o1, o2, expected_value1, expected_value2):
        res1=str(o1+o2)
        print(str(o1)+'+'+str(o2)+'='+res1, end='  ')
        assert res1==expected_value1
        print('ok')
        res2=str(o1*o2)
        print(str(o1)+'*'+str(o2)+'='+res2, end='  ')
        assert res2==expected_value2
        print('ok')
        
    #Test results of addition and multiplication
    test(o124, o19, '133', '26')
    test(o124, o0, '124', '0')
    test(o124, o1, '125', '4')

    test(o19, o124, '133', '26')
    test(o0, o124, '124', '0')
    test(o1, o124, '125', '4')

    res1=str(o19+o124+o1)
    print(str(o19)+'+'+str(o124)+'+'+str(o1)+'='+str(res1), end='  ')
    assert res1=='134'
    print('ok')

    res2=str((o19+o124)*o1)
    print('('+str(o19)+'+'+str(o124)+')'+'*'+str(o1)+'='+res2, end='  ')
    assert res2=='3'
    print('ok')

    #Check types
    type_o1=type(o1)
    if 'NumericString' in str(type_o1):
        print('Type of NumericString(1) is ok')
    else:
        assert False

    type_o1_plus_o124=type(o1+o124)
    if 'NumericString' in str(type_o1_plus_o124):
        print('Type of NumericString(1)+NumericString(124) is ok')
    else:
        assert False

    type_o1_times_o124=type(o1+o124)
    if 'NumericString' in str(type_o1_times_o124):
        print('Type of NumericString(1)*NumericString(124) is ok')
    else:
        assert False

