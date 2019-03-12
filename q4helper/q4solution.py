#Submitter: Viray, Aljon - 86285526 - asviray

# Generators must be able to iterate through any kind of iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


# The combination of return and yield None make each of the following
#   a generator (yield None) that immediately raises the StopIteration
#   exception (return)

def sequence(*iterables): #DONE!
    for iterable in iterables:
        for item in iterable:
            yield item

            
def group_when(iterable, p): #DONE!
    result = []
    for item in iterable:
        x = item #For remembering final character
        
        if p(item) == False: #If item is not in the lambda, append & restart loop
            result.append(item)
            continue
        elif p(item) == True: #If item is in the lambda, append & yield result
            result.append(item)
                    
        yield result        
        result = [] #Reset list
        
    if p(x) == False: #Yields last character if it is False in p
        yield [x]


def drop_last(iterable, n): #DONE!
    iterator = iter(iterable)
    last = [next(iterator) for i in range(n)]

    while True:
        try:
            x = next(iterator) #Store next value after "last" list is made  
            last.append(x) #Append this next value to last
            yield last.pop(0) #Yield the front value from last
                
        except StopIteration: #If generator is done, break out of loop
            break
    
        
def yield_and_skip(iterable, skip): #DONE!
    iterator = iter(iterable)
    current = next(iterator) #First call to next()
    while True:
        try:
            yield current #Append first character
            to_skip = skip(current) #Store value found by that character in lambda
            
            for i in range(to_skip+1): #Skips through i many characters, plus 1
                current = next(iterator)
                
        except StopIteration:
            break
        

def alternate_all(*args): #DONE!
    generators = [iter(arg) for arg in args]
    done = set()
    
    while True:
        for gen in generators:
            try:
                yield next(gen)
            except StopIteration:
                done.add(gen)
        
        if len(done) == len(generators): #If all generators done, break from while loop
            break


def min_key_order(adict):
    if not adict:
        return
    
    min_value = min(adict)
    yield min_value,adict[min_value]
    
    while True:
        # Scan dict keys, finding min_bigger: the smallest one > min_value
        min_bigger = None
        for key in adict:
            if key > min_value and (min_bigger == None or key < min_bigger):
                min_bigger = key
        
        if min_bigger == None:
            return
        else:
            min_value = min_bigger
            yield min_value,adict[min_value]
           
       
         
if __name__ == '__main__':
    from goody import irange
    
    # Test sequence; you can add any of your own test cases
    print('Testing sequence')
    for i in sequence('abc', 'd', 'ef', 'ghi'):
        print(i,end='')
    print('\n')
 
    print('Testing sequence on hidden')
    for i in sequence(hide('abc'), hide('d'), hide('ef'), hide('ghi')):
        print(i,end='')
    print('\n')


    # Test group_when; you can add any of your own test cases
    print('Testing group_when')
    for i in group_when('combustibles', lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')

    print('Testing group_when on hidden')
    for i in group_when(hide('combustibles'), lambda x : x in 'aeiou'):
        print(i,end='')
    print('\n')


    # Test drop_last; you can add any of your own test cases
    print('Testing drop_last')
    for i in drop_last('combustible', 5):
        print(i,end='')
    print('\n')

    print('Testing drop_last on hidden')
    for i in drop_last(hide('combustible'), 5):
        print(i,end='')
    print('\n')


    # Test sequence; you can add any of your own test cases
    print('Testing yield_and_skip')
    for i in yield_and_skip('abbabxcabbcaccabb',lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')

    print('Testing yield_and_skip on hidden')
    for i in yield_and_skip(hide('abbabxcabbcaccabb'),lambda x : {'a':1,'b':2,'c':3}.get(x,0)):
        print(i,end='')
    print('\n')


    # Test alternate_all; you can add any of your own test cases
    print('Testing alternate_all')
    for i in alternate_all('abcde','fg','hijk'):
        print(i,end='')
    print('\n')
    
    print('Testing alternate_all on hidden')
    for i in alternate_all(hide('abcde'), hide('fg'),hide('hijk')):
        print(i,end='')
    print('\n\n')
       
         
    # Test min_key_order; add your own test cases
    print('\nTesting Ordered')
    d = {1:'a', 2:'x', 4:'m', 8:'d', 16:'f'}
    i = min_key_order(d)
    print(next(i))
    print(next(i))
    del d[8]
    print(next(i))
    d[32] = 'z'
    print(next(i))
    print(next(i))
    


         
         
    import driver
    driver.default_file_name = "bscq4F18.txt"
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
