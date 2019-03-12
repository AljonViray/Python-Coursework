from   bag import Bag
import unittest  # use unittest.TestCase
import random    # use random.shuffle,random.randint

#random.shuffle(alist) mutates its alist argument to be a random permutation
#random.randint(1,10)  returns a random number in the range 1-10 inclusive


class Test_Bag(unittest.TestCase):
    
    def setup(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
            
    def test_len(self):
        self.setup()  
        self.assertEqual( self.bag.__len__(), 7 ) #Initial Bag should have 7 items
        count = 7
        random.shuffle(self.alist) #Shuffle alist
        for x in self.alist:
            self.bag.remove(x) #Remove random item in bag
            count -= 1
            self.assertEqual( self.bag.__len__(), count ) #Check if item count went down
        
    def test_unique(self):
        self.setup()           
        self.assertEqual( self.bag.unique(), 4 )
        random.shuffle(self.alist) #Shuffle alist
        for x in self.alist:
            self.bag.remove(x) #Remove random item in bag
            self.assertEqual( self.bag.unique(), len(self.bag.counts) )
             
    def test_contains(self):
        self.setup()  
        self.assertTrue( self.bag.__contains__('a') ) and self.assertTrue( self.bag.__contains__('b') ) and self.assertTrue( self.bag.__contains__('c') )
        self.assertFalse( self.bag.__contains__('x') )
         
    def test_count(self):
        self.setup()
        self.assertEqual( self.bag.counts['a'], 1 )
        self.assertEqual( self.bag.counts['b'], 2 )
        self.assertEqual( self.bag.counts['c'], 1 )
        self.assertEqual( self.bag.counts['d'], 3 )
        self.assertEqual( self.bag.counts['x'], 0 )
        
        count = sum(self.bag.counts.values())
        random.shuffle(self.alist) #Shuffle alist
        for x in self.alist:
            self.bag.remove(x)
            count -= 1
            self.assertEqual( sum(self.bag.counts.values()), count)
             
    def test_equals(self):
        rand_list = [random.randint(1,10) for i in range(0,1000)] #Make 1000-value random list
        bag1 = Bag(rand_list) #Create bag from random list
        random.shuffle(rand_list) #Shuffle random list
        bag2 = Bag(rand_list) #Create another bag from shuffled random list
        self.assertTrue( bag1.__eq__(bag2) ) #They should be equal
        bag1.remove(rand_list[0]) #Remove 1 value from one bag
        self.assertFalse( bag1.__eq__(bag2) ) #They should NOT be equal
        
    def test_add(self):
        rand_list = [random.randint(1,10) for i in range(0,1000)] #Make 1000-value random list
        bag1 = Bag(rand_list) #Create bag from random list
        bag2 = Bag() #Create another bag from shuffled random list
        random.shuffle(rand_list) #Shuffle random list
        for x in rand_list:
            bag2.add(x)
        self.assertEqual( bag1, bag2 )
        
    def test_remove(self):
        rand_list = [random.randint(1,10) for i in range(0,1000)] #Make 1000-value random list
        bag1 = Bag(rand_list) #Create bag from random list
        with self.assertRaises(ValueError):
            bag1.remove(43)
            
        bag2 = Bag(rand_list)
        random.shuffle(rand_list) #Shuffle random list
        for x in rand_list:
            bag2.add(x)
        for x in rand_list:
            bag2.remove(x)
        self.assertEqual( bag1, bag2 )
    
    
if __name__ == '__main__':
    unittest.main()

