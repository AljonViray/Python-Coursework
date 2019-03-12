# Submitter: asviray(Viray, Aljon)
# Partner  : dmishkan(Mishkanian, Daniel)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import prompt
import inspect

class Sparse_Matrix:
    
    def __init__(self, rows, cols, *tups):
        assert type(rows) == int, 'Type of rows must be int'
        assert type(cols) == int, 'Type of cols must be int'
        assert rows > 0, '# of rows must be greater than 0'
        assert cols > 0, '# of columns must be greater than 0'
        for tup in tups:
            assert type(tup) == tuple, "Type of 'tups' must be tuple"
            for value in tup:
                assert type(value) in (int, float), 'Values must be integers'
            assert tup[0] < rows, 'Row index must be less than # of rows'
            assert tup[1] < cols, 'Column index must be less than # of columns'

        self.rows, self.cols = rows, cols
        self.matrix = dict()
        
        for tup in tups:
            if tup[2] == 0:
                continue
            assert (tup[0], tup[1]) not in self.matrix.keys(), 'Row & Column indexes must be unique'
            self.matrix.update( {(tup[0], tup[1]) : tup[2]} )


    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
    
    def size(self):
        return (self.rows, self.cols)
    
    
    def __len__(self):
        return self.rows*self.cols
    
    
    def __bool__(self):
        if len(self.matrix) == 0:
            return False
        return True
    
    
    def __repr__(self):
        result = []
        for key, value in self.matrix.items():
            result.append( f'({key[0]},{key[1]},{value})' )
                                
        return f'Sparse_Matrix({self.rows}, {self.cols}, {(", ").join(result)})'
    
    
    def __getitem__(self, index: "2-tuple"):
        if (type(index) != tuple or len(index) != 2 or type(index[0]) != int or type(index[1]) != int or index[0] < 0 or index[0] > self.rows-1 or index[1] < 0 or index[1] > self.cols-1): raise TypeError
        return self.matrix.get(index,0)
    
    
    def __setitem__(self, index: "2-tuple", value: "int or float"):
        if (type(index) != tuple or len(index) != 2 or type(index[0]) != int or type(index[1]) != int or index[0] < 0 or index[0] > self.rows-1 or index[1] < 0 or index[1] > self.cols-1 or type(value) not in (int, float)): raise TypeError
        elif (index not in self.matrix.keys() and value == 0):
            return
        elif (value == 0 and self.matrix[index] != 0):
            del self.matrix[index]
        else:
            self.matrix[index] = value
    
    
    def __delitem__(self, index: "2-tuple"):
        if (type(index) != tuple or len(index) != 2 or type(index[0]) != int or type(index[1]) != int or index[0] < 0 or index[0] > self.rows-1 or index[1] < 0 or index[1] > self.cols-1): raise TypeError
        elif (index not in self.matrix.keys()):
            return
        del self.matrix[index]        
        
    
    def row(self, r: int):
        assert type(r) == int
        assert r >= 0 and r < self.rows

        result = []
        for col in range(self.cols):
            result.append(self.matrix.get((r, col), 0))
        return tuple(result)   
    
    
    def col(self, c: int):
        assert type(c) == int
        assert c >= 0 and c < self.cols

        result = []
        for row in range(self.rows):
            result.append(self.matrix.get((row, c), 0))
        return tuple(result)   
     
    
    def details(self):
        result = []
        for i in range(self.rows):
            result.append(f'{self.row(i)}')
        return f'{self.rows}x{self.cols} -> {self.matrix} -> ({(", ").join(result)})'


    def __call__(self, r: int, c: int):
        matrix_copy = self.matrix.copy()
        for key in matrix_copy.keys():
            if (key[0] > r-1 or key[1] > c-1):
                del self.matrix[key]
        self.rows, self.cols = r, c

 
    def __iter__(self):
        result = []
        for key, value in self.matrix.items():
            result.append( (key[0], key[1], value) )
        result = sorted(result, key = lambda x: x[2])
        
        def generator(iterable):
            for item in iterable:
                yield item
                 
        return generator(result)    
    
    
    def __pos__(self):
        new_sparse_matrix = Sparse_Matrix(self.rows, self.cols)
        new_sparse_matrix.matrix = self.matrix.copy()
        return new_sparse_matrix
    
    
    def __neg__(self):
        new_sparse_matrix = Sparse_Matrix(self.rows, self.cols)
        new_sparse_matrix.matrix = self.matrix.copy()
        for key, value in self.matrix.items():
            new_sparse_matrix.matrix[key] = value * -1
        return new_sparse_matrix
    
    
    def __abs__(self):
        new_sparse_matrix = Sparse_Matrix(self.rows, self.cols)
        new_sparse_matrix.matrix = self.matrix.copy()
        for key, value in self.matrix.items():
            new_sparse_matrix.matrix[key] = abs(value)
        return new_sparse_matrix    
    
    
    def __add__(self, obj):
        new_matrix = Sparse_Matrix(self.rows, self.cols)
            
        if type(obj) == Sparse_Matrix:
            assert (self.rows, self.cols) == (obj.rows, obj.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.__setitem__((i,j), self.__getitem__((i,j)) + obj.__getitem__((i,j)))
            return new_matrix
        
        elif type(obj) in (int, float):
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.__setitem__((i,j), self.__getitem__((i,j)) + obj)
            return new_matrix
        
        else: 
            raise TypeError
        
        
    def __radd__(self, obj):
        return self + obj
        
        
    def __sub__(self, obj):
        new_matrix = Sparse_Matrix(self.rows, self.cols)
            
        if type(obj) == Sparse_Matrix:
            assert (self.rows, self.cols) == (obj.rows, obj.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.__setitem__((i,j), self.__getitem__((i,j)) - obj.__getitem__((i,j)))
            return new_matrix
        
        elif type(obj) in (int, float):
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.__setitem__((i,j), self.__getitem__((i,j)) - obj)
            return new_matrix
        
        else: 
            raise TypeError
        
        
    def __rsub__(self, obj):
        new_matrix = Sparse_Matrix(self.rows, self.cols)
        if type(obj) in (int, float):
            for i in range(self.rows):
                for j in range(self.cols):
                    new_matrix.__setitem__((i,j), obj - self.__getitem__((i,j)))
            return new_matrix
        else:
            raise TypeError
    
    
    def __mul__(self, obj):
        if type(obj) == Sparse_Matrix:
            new_matrix = Sparse_Matrix(self.rows, obj.cols) #for matrix times matrix
            assert self.cols == obj.rows
            for i in range(new_matrix.rows):
                for j in range(new_matrix.cols):
                    r_values = self.row(i)
                    c_values = obj.col(j)
                    mult_values = [r_values[x] * c_values[x] for x in range(len(r_values))]
                    new_matrix.__setitem__((i,j), sum(mult_values))
            return new_matrix
        
        elif type(obj) in (int, float):
            sp_matrix = Sparse_Matrix(self.rows, self.cols) #for matrix times int/float
            for i in range(self.rows):
                for j in range(self.cols):
                    sp_matrix.__setitem__((i,j), self.__getitem__((i,j)) * obj)
            return sp_matrix
        else:
            raise TypeError
    
    
    def __rmul__(self, obj):
        return self * obj    
    
    
    def __pow__(self, obj):
        if type(obj) != int : raise TypeError
        if obj < 1 or self.rows != self.cols: raise AssertionError
        new_matrix = Sparse_Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                new_matrix.__setitem__((i,j), self.__getitem__((i,j))**obj)
        return new_matrix
    
    
    def __eq__ (self, obj):
        if type(obj) == Sparse_Matrix and self.size() == obj.size():
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.__getitem__((i,j)) != obj.__getitem__((i,j)):
                        return False
            return True
        
        elif type(obj) in (int, float):
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.__getitem__((i,j)) != obj:
                        return False
            return True
        
        return False
    
    
    def __ne__(self, obj):
        return not self.__eq__(obj)                
    
    
    def __setattr__(self, name, value):
        calling = inspect.stack()[1]
        if (name in ("rows", "cols", "matrix") and calling.function != "<module>"):
            self.__dict__.update({name:value})
        else:
            raise AssertionError
    



if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
    #Debugging problems with these tests is simpler

    print('Printing')
#     m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
#     print(m)
#     print(repr(m))
#     print(m.details())
   
#     print('\nlen and size')
#     print(len(m), m.size(),)
     
#     print('\ngetitem and setitem')
#     print(m[1,1])
#     m[1,1] = 0
#     m[0,1] = 2
#     print(m.details())
#  
#     print('\niterator')
#     for r,c,v in m:
#         print((r,c),v)
     
#     print('\nm, m+m, m+1, m==m, m==1')
#     print(m)
#     print(m+m)
#     print(m+1)
#     print(m==m)
#     print(m==1)
#     print()
    
    import driver
    driver.default_file_name = 'bscp22F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
