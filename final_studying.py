#FINAL EXAM PRACTICE REVIEW

#NUMBER 1
def select(pred_list):
    
    def func(iterable):
        result = []
        for i in iterable:
            check = True
            for p in pred_list:
                if p(i) == False:
                    check = False
            if check == True:
                result.append(i)
        return result
    return func

big_odd = select([(lambda x: x % 2 == 1), (lambda x: x > 5)]) 
print('#1a', big_odd(range(1,10)) )


import math
def dist(pt1,pt2):
    return math.sqrt( (pt1[0]-pt2[0])**2 + (pt1[1]-pt1[0])**2) 

def closest(ref_pts, pt):
    distances = [(x, dist(x, pt)) for x in ref_pts]
    distances = sorted(distances, key=lambda x: x[1])
    return distances[0][0]

print('#1b',  closest([(2,6), (2,1)], (0,0)) )


#NUMBER 4
def filter(iterable, p):
    iterator = iter(iterable)
    while True:
        try:
            x = next(iterator)
            if p(x) == True:
                yield x
        except StopIteration:
            break
        
print('#4a', list (filter(range(5), (lambda x: x % 2 == 0)) ) )

 
def match_indexes(pattern, text):
    result = ''
    left = 0
    right = len(pattern)
    for i in range(len(text)):
        if text[left:right] == pattern:
            yield left
        left += 1
        right += 1
    

for i in match_indexes ('ab','aabbaabacab'):
    print(i,end=' ')
print()
    

#Problem 3
class Poly:
    def __init__(self, args):
        self.dict = dict()
        for x in args:
            self.dict.update( {x[1]: x[0] } )
            
    def __getitem__(self, item):
        if item < 0:
            raise TypeError
        if item not in self.dict:
            return 0.0
        return self.dict[item]
    
    def __call__(self, arg):
        total = 0
        for k,v in self.dict.items():
            if k == 0:
                total += v
            else:
                sub = v*(arg**k)
                total += sub
        return total
                              
p = Poly([(3.0, 2), (2.0, 1), (-1.0, 0)]) 
print(p.dict)
print(p[2], p[3], p[0])
print(p(1.5))
    
    
# #Problem 5 
# def separate(p, l):
#     if l == []:
#         return []
#     
#     else:
#         if p(l[0]) == True:
#             return ( [l[0]] + separate(p, l[1:])[0], [] + separate(p, l[1:])[1] )
#         else:
#             return ( [] + separate(p, l[1:])[0], [l[0]] + separate(p, l[1:])[1] )
#  
# print( separate(lambda x: x % 2 == 0, [1,2,3,4,5]) )

