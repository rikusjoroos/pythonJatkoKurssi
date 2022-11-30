from abc import ABC, abstractmethod

class BaseClass(ABC):
    def __init__(self, v):
        self.v = v

    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def __str__(self):
        pass
    
class ForwardClass(BaseClass):
    def __init__(self, v):
        self.v = v
        
    def __str__(self):
        return(str(self.v))
        
    def print(self):
        print(self.__str__())
    

class BackwardClass(BaseClass):
    def __init__(self, v):
        self.v = v
        
    def __str__(self):
        return(str(self.v)[::-1])
    
    def print(self):
        print(self.__str__())
    

if __name__ == "__main__":
    try:
        print('Trying to create BaseClass object...', end=' ')
        b=BaseClass('s')
    except TypeError:
        print('Got TypeError exception - ok')

    for test_value in ['abcdef', 9876, ['ab', 3.14159265,[1, 2, 3]]]:
        print(32*'-')
        print('Create ForwardClass('+str(test_value)+')')
        fw=ForwardClass(test_value)
        print('Test ForwardClass.print():', end=' ')
        fw.print()
        print('Test ForwardClass.__str__():', end=' ')
        s=str(fw)
        print('value="'+s+'"', end=' ')
        assert s==str(test_value)
        print('ok ')

        print(32*'-')

        print('Create BackwardClass('+str(test_value)+')')
        bw=BackwardClass(test_value)
        print('Test BackwardClass.print():', end=' ')
        bw.print()
        print('Test BackwardClass.__str__():', end=' ')
        s=str(bw)
        bw_testvalue=str(test_value)[::-1]
        print('value="'+s+'"', end=' ')
        assert s==bw_testvalue
        print('ok ')
    
