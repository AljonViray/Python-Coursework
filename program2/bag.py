# Submitter: asviray(Viray, Aljon)
# Partner  : dmishkan(Mishkanian, Daniel)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from collections import defaultdict
from goody import type_as_str
import prompt

class Bag:
    
    def __init__(self, iterable=None):
        self._dict = dict()
        if (iterable != None):
            for element in sorted(iterable):
                if element not in self._dict:
                    self._dict.update({element:1})
                else:
                    self._dict.update({element:self._dict[element]+1})


    def __repr__(self) -> str:
        result = []
        for key , value in self._dict.items():
            result.extend([key for i in range(value)])
        return f'Bag({result})'


    def __str__(self):
        result = []
        for key, value in self._dict.items():
            result.append(f'{key}[{value}]')
        return f'Bag{tuple(result)}'
    
    
    def __len__(self):
        return sum(self._dict.values())
    
    
    def unique(self):
        return len(self._dict.keys())
    
    
    def __contains__(self, arg):
        return arg in self._dict
    
    
    def count(self, arg):
        if arg in self._dict:
            return self._dict[arg]
        else:
            return 0


    def add(self, arg):
        if arg not in self._dict:
            self._dict.update({arg: 1})
        else:
            self._dict.update({arg: int(self._dict[arg])+1})

    
    def __add__(self, obj): #NEEDS WORK
        if type(obj) != Bag:
            raise TypeError
        
        result = Bag()        
        for x in self._dict:
            if x in self._dict and x in obj._dict:
                result._dict.update({x: self._dict[x] + obj._dict[x]})
                
            elif x in self._dict and x not in obj._dict:
                result._dict.update({x: self._dict[x]})
                
            elif x in obj._dict and x not in self._dict:
                result._dict.update({x: obj._dict[x]})

        for x in obj._dict:      
            if x not in result._dict:
                result._dict.update({x: obj._dict[x]})
        
        return result
    
    
    def remove(self, arg):
        if arg not in self._dict:
            raise ValueError(f'{arg} could not be removed from Bag object')
        else:
            self._dict.update({arg: self._dict[arg]-1})
            if self._dict[arg] == 0:
                del self._dict[arg]
                
                
    def __eq__(self, obj):
        if type(obj) != Bag or self._dict != obj._dict:
            return False
        elif type(obj) == Bag and self._dict == obj._dict:
            return True
    
    
    def __ne__(self, obj):
        if type(obj) != Bag or self._dict != obj._dict:
            return True
        elif self._dict == obj._dict:
            return False

        
    def __iter__(self):
        copy = self._dict.copy()
        
        def generator(iterable):
            for key in copy:
                for i in range(copy[key]):
                    yield key
        return generator(copy)




if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
#     print(repr(b+b))
#     print(str(b+b))
#     print()
#     print(repr(b))    
#     print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
#             
#     for i in b:
#         print(i)
   
    b2 = Bag(['a','a','b','x','d'])     
#     print(repr(b2+b2))
#     print(str(b2+b2))
#     print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
#     b = Bag(['a','b','a'])
#     print(repr(b))

#     print(b)
#     print(b2)
#     print('b+b2:', b+b2)

 
    print()
    import driver
    driver.default_file_name = 'bscp21F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
