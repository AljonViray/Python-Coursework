# Submitter: asviray(Viray, Aljon), 86285526

import prompt,re
import math
from goody import type_as_str

class Point:
        
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z
        self.coords = (x,y,z)
        
        err_str = f'Point parameters should be integers'
        assert type(self.x) == int, err_str
        assert type(self.y) == int, err_str
        assert type(self.z) == int, err_str


    def __repr__(self):
        return f'Point({self.x},{self.y},{self.z})'
    
    
    def __str__(self):
        return f'(x={self.x},y={self.y},z={self.z})'
    
    
    def __bool__(self):
        return (self.x, self.y, self.z) != (0,0,0)
        

    def __add__(self, obj):
        if type(obj) != Point:
            raise TypeError(f'Input should be Point; NOT {type(obj)}')
        else:
            new_x = self.x + obj.x
            new_y = self.y + obj.y
            new_z = self.z + obj.z
            return Point(new_x, new_y, new_z)


    def __mul__(self, right): #For x*2
        if type(right) != int:
            raise TypeError(f'Input should be integer; NOT {type(right)}')
        return Point(self.x*right, self.y*right, self.z*right)
        
    
    def __rmul__(self, right): #For 2*x
        if type(right) != int:
            raise TypeError(f'Input should be integer; NOT {type(right)}')
        return Point(self.x*right, self.y*right, self.z*right)

    
    def __lt__(self, obj):
        dist1 = (self.x + self.y + self.z)/3
        if type(obj) == Point:
            dist2 = (obj.x + obj.y + obj.z)/3
            return dist1 < dist2
        elif type(obj) in (int, float):
            dist2 = obj
            return dist1 < dist2
        else:
            raise TypeError(f'Input should be Point, integer, or float; NOT {type(obj)}')
    

    def __getitem__(self, obj):
        if type(obj) not in (str,int):
            raise IndexError(f'Input should be strings: x,y,z OR integers: 0,1,2; NOT {obj}')
        elif obj == 'x' or obj == 0:
            return self.x
        elif obj == 'y' or obj == 1:
            return self.y
        elif obj == 'z' or obj == 2:
            return self.z
        else:
            raise IndexError(f'Input should be strings: x,y,z OR integers: 0,1,2; NOT {obj}')


    def __call__(self, a, b, c):
        err_str = f'Parameters should be integers'
        assert type(a) == int, err_str
        assert type(b) == int, err_str
        assert type(c) == int, err_str
        self.x, self.y, self.z = a, b, c




if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test Point before doing bsc tests

    print('Start simple testing\n')
    
    p1 = Point(1,2,3)
    print(p1.x, p1.y, p1.z)
    print()
     
#     p2 = Point('a','b','c')
#     print(p2.x, p2.y, p2.z)
#     print()
     
    p3 = Point(1,2,3)
    print(p3)
    print()


    print()
    import driver
    
    driver.default_file_name = 'bscq31F18.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
