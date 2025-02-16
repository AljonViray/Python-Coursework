#Submitter: Viray, Aljon - 86285526 - asviray

# p is a predicate: it returns True/False when called on one argument
def separate(p : callable, l : [object]) -> ([object],[object]): #DONE!
    #Base Case
    if (l == []):
        return ([], [])
    
    #Recursive Case
    else:
        x, y = separate(p, l[1:]) #Produces two lists
        
        if (p(l[0]) == True):
            return (x + [l[0]], y) #Concatenating to list x
        else:
            return (x, y + [l[0]]) #Concatenating to list y
                      
              
def is_sorted(l : [object]) -> bool: #DONE!
    #Base Case
    if len(l) < 2:
        return True
    
    #Recursive Case
    else:
        if l[0] <= l[1]:
            return is_sorted(l[1:])
        else:
            return False


def sort(l : [object]) -> [object]: #DONE!
    #Base Case
    if l == []:
        return []
    
    #Recursive Case
    else:
        less, more = separate(lambda x: x <= l[0], l[1:])
        return sort(less) + [l[0]] + sort(more)


def merge_chars(a : str, b : str) -> str: #DONE!
    #Base Case
    if a == '' and b == '':
        return ''
    
    #Recursive Case
    else:
        if a != '': #If a is not an empty string
            if b == '' or a[0] <= b[0]: #If b is empty string OR first a is greater than first b
                return a[0] + merge_chars(a[1:], b)
            
            elif b != '' or a[0] > b[0]: #If opposite of above
                return b[0] + merge_chars(a, b[1:])
        
        elif a == '': #If a is an empty string (after this, nothing else matters)
            if b != '' or a[0] > b[0]:
                return b[0] + merge_chars(a, b[1:])
        
 
def nested_count(l : 'any nested list of int', a : int) -> int: #DONE!
    #Base Case
    if len(l) == 0:
        return 0
    
    #Recursive Case
    else:
        total = nested_count(l[1:], a)
        
        if type(l[0]) == int and l[0] == a:
            return total + 1
        elif type(l[0]) == list:
            return total + nested_count(l[0], a)
    
    return total



if __name__=="__main__":
    import driver,random,predicate
    from goody import irange
    
    print('Testing separate')
    print(separate(predicate.is_positive,[]))
    print(separate(predicate.is_positive,[1, -3, -2, 4, 0, -1, 8]))
    print(separate(predicate.is_prime,[i for i in irange(2,20)]))
    print(separate(lambda x : len(x) <= 3,'to be or not to be that is the question'.split(' ')))
    print(separate(lambda x : x <= 'm','to be or not to be that is the question'.split(' ')))
        
    print('\nTesting is_sorted')
    print(is_sorted([]))
    print(is_sorted([0]))
    print(is_sorted([-5,-4]))
    print(is_sorted([1,2,3,4,5,6,7]))
    print(is_sorted([1,2,3,7,4,5,6]))
    print(is_sorted([1,2,3,4,5,6,5]))
    print(is_sorted([7,6,5,4,3,2,1]))
    
    print('\nTesting sort')
    print(sort([1,2,3,4,5,6,7]))
    print(sort([7,6,5,4,3,2,1]))
    print(sort([4,5,3,1,2,7,6]))
    print(sort([1,7,2,6,3,5,4]))
    l = [i+1 for i in range(30)]
    random.shuffle(l)
    print(l)
    print(sort(l))
     
    print('\nTesting merge_chars')
    print(merge_chars('',''))
    print(merge_chars('','abc'))
    print(merge_chars('abc',''))
    print(merge_chars('ace','bdf'))
    print(merge_chars('abc','xyz'))
    print(merge_chars('abxy','lmzzz'))
    print(merge_chars('acdeghilmnosu','bfjkpqrtvwxyz'))
    print(merge_chars('bcgprvyz','adefhijklmnoqstuwx'))
    print(merge_chars('cdefghijklmnpqrstuvw','aboxyz'))
    
    print('\nTesting nested_count')
    print(nested_count([1,2,4,1,8,1,3,2,1,1],1))
    print(nested_count([[1,2,4,1,8],[1,3,2],1,1],1))
    print(nested_count([[1,2,[4,[1],8],[1,3,2]],[1,1]],1))
    

    driver.default_file_name = "bscq5F18.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
    
