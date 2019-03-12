#asviray, 86285526, Aljon Viray

from collections import defaultdict
from math import sqrt,atan2


def integrate(f : callable, n : int) -> callable: #FIX
    if type(n) != int:
        raise AssertionError('n must be an int')
    elif n < 0:
        raise AssertionError('n must be an greater than 0')


    def calculate(a : float, b: float):    
        if a > b:
            raise AssertionError('a must be less than or equal to b')
        dx = (b-a)/n
        for i in range(n):
            area = f(a+(n-1)*dx)
        return area
    
    return calculate


def sorted1 (ps : {int:(int,int)}) -> [(int,(int,int))]: #DONE!!!
    return sorted(sorted([(x, ps[x]) for x in ps], key=lambda x:x[1][1]), key=lambda x:x[1][0])


def sorted2 (ps : {int:(int,int)}) -> [(int,int)]: #DONE!!!
    return sorted(sorted([ps[x] for x in ps], key=lambda x:sqrt(x[0]**2 + x[1]**2)), key=lambda x:atan2(x[1],x[0]), reverse=True)


def sorted3 (ps : {int:(int,int)}) -> [int]: #DONE!!!
    #list = []
    #for x in ps:
    #    list.append(x)
    #sorted(list, key=lambda ...)
    return sorted([x for x in ps], key=lambda x:sqrt(ps[x][0]**2+ps[x][1]**2))


def points (ps : {int:(int,int)}) -> [(int,int)]: #DONE!!!
    #list = []
    #for x in ps:
    #    list.append(ps[x])
    return [ps[x] for x in ps]


def first_quad (ps : {int:(int,int)}) -> {(int,int):float}: #DONE!!!
    return {ps[x] : sqrt((ps[x][0]**2 + ps[x][1]**2)) for x in ps if ps[x][0]>=0 and ps[x][1]>=0}


def movie_rank(db : {str:{(str,int)}}) -> [(str,float)]: #DONE!!! 
    movie_list = []
    for movie in db:
        rate_list = db[movie]   #Stores the dict {(str, int)}
        ratings = 0
        
        for rating in rate_list:
            ratings += rating[1]
            
        avg_score = float(ratings/len(rate_list))
        review = (movie, avg_score)
        movie_list.append(review)
    
    return sorted(sorted(movie_list, key=lambda x: x[0]), key=lambda x:x[1], reverse=True)


def reviewer_dict(db : {str:{(str,int)}}) -> {str:{(str,int)}}: #DONE!!!
    d = {}
    for movie in db:
        rate_list = db[movie]   #Stores the dict {(str, int)
        
        for rating in rate_list:
            person = rating[0]
            
            if person not in d:
                d.update({person: {(movie, rating[1])}})
            else:
                d[person].add((movie, rating[1]))

    return d




if __name__ == '__main__':
    # This code is useful for debugging your functions, especially
    #   when they raise exceptions: better than using driver.driver().
    # Feel free to add more tests (including tests showing in the bscF18.txt file)
    # Use the driver.driver() code only after you have removed any bugs
    #   uncovered by these test cases.
    
    print('Testing integrate')
    f = integrate( (lambda x : x), 100)
    print(f(0,1),f(0,2),f(-1,1))
    f = integrate( (lambda x : 3*x**2 - 2*x + 1), 1000)
    print(f(0,1),f(0,2),f(-1,1))
 
    print('\nTesting sorted1')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted1(ps1))
    print(sorted1(ps2))
 
    print('\nTesting sorted2')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted2(ps1))
    print(sorted2(ps2))
 
    print('\nTesting sorted3')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(sorted3(ps1))
    print(sorted3(ps2))
    
    print('\nTesting points')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(points(ps1))
    print(points(ps2))
 
    print('\nTesting first_quad')
    ps1 = {1:(1,1),2:(3,2),3:(3,-3),4:(-3,4),5:(-2,-2)} 
    ps2 = {1:(0,5), 2:(2,3), 3:(-3,2), 4:(-5,1), 5:(-3,-2), 6:(4,-2), 7:(5,0), 8:(0,-5)}  
    print(first_quad(ps1))
    print(first_quad(ps2))
 
    print('\nTesting movie_rank')
    db1 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), }, 'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(movie_rank(db1))
    print(movie_rank(db2))
 
    print('\nTesting reviewer_dict')
    db1 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1)}, 'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)}, 'Up': {('Alan',2), ('Diane',5)} }
    db2 = {'Psycho':  {('Bob',5),  ('Carrie',5), ('Alan', 1), ('Diane', 1), ('Evan',4), ('Fawn',2)},
           'Amadeus': {('Bob',3),  ('Carrie',3), ('Diane',3)},
           'Up': {('Alan',2), ('Diane',5)},
           'Casablaca': {('Alan',2), ('Diane',5), ('Evan',2)},
           'Rashamon': {('Alan',2), ('Diane',5), ('Fawn',3), ('Gary',4)},
           'Alien': {('Alan',2), ('Diane',5), ('Evan',5), ('Fawn',5)}}
    print(reviewer_dict(db1))
    print(reviewer_dict(db2))
 
 
    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = "bscq1F18.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()           

