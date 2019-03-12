print( 'map()' )
print( map(lambda x: x+'yeet', ['a','b','c']) )
print( list(map(lambda x: x+'yeet', ['a','b','c'])) )
print()

print( map(lambda x: x ** 2, [1, 2, 3, 4, 5]) )
print( list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])) )
print()

print('~~~\n')

print( 'filter()' )
import predicate
print ( filter(lambda x: predicate.is_positive(x), [1, -1, 2, -2, 3, -3]) )
print ( list(filter(lambda x: predicate.is_positive(x), [1, -1, 2, -2, 3, -3])) )
print()

print ( filter(lambda x: x < 0, [1, -1, 2, -2, 3, -3]) )
print ( list(filter(lambda x: x < 0, [1, -1, 2, -2, 3, -3])) )

print('~~~\n')
 
print('Structure of Recursive Functions')

def recursive(x):
    if x == 0:
        print(x)
        return 0
    else:
        print(x)
        return recursive(x-1)
        
recursive(10)

print('~~~\n')

db = {'Al': {'plumbing':4, 'painting':2}, 'Barb': {'painting':3}, 'Carl': {'building': 5, 'painting': 3} }
def expertise(db):
    return sorted(db, key=lambda x: ( (-sum(db[x].values()))/len(db[x]), x) ) 
print(expertise(db))



