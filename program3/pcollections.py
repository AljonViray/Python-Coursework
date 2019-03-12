# Submitter: asviray(Viray, Aljon)
# Partner  : dmishkan(Mishkanian, Daniel)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable= False):
    def show_listing(s):
        for line_num, line_text in enumerate(s.split('\n'), 1):
            print(f' {line_num: >3} {line_text.rstrip()}')
    
    #COPIED FROM COURSE NOTES
    def unique(iterable):
        iterated = set()
        for i in iterable:
            if i not in iterated:
                iterated.add(i)
                yield i
    
    #FOR USE BELOW            
    def gen_init(field_list):
        field_str, vars_str = str(), str()
        for field in field_list:   
            if field == field_list[-1]:
                field_str += field
            else:
                field_str += f'{field}, '
            vars_str += f'''
        self.{field} = {field}'''
        
        init_str = f'''
    def __init__(self, {field_str}):
        {vars_str}
        self._fields = {field_list}
        self._mutable = False'''
                
        return init_str
    
    
    def gen_repr(type_name, field_list):
        repr_str = '''
    def __repr__(self):
        d = self.__dict__
        d_keys = list(d.keys())[:-2]
        fields_str = str()
        
        for key in d_keys:   
            if key == d_keys[-1]:
                fields_str += f'{key}={d[key]}'
            else:
                fields_str += f'{key}={d[key]},'
        
        return f'{type(self).__name__}({fields_str})' '''
        return repr_str
    
    
    def gen_gets(field_list):
        gets_str = ''''''
        for field in field_list:
            gets_str += f'''
    def get_{field}(self):
        return self.{field}
        '''
        return gets_str
    
    
    def gen_getitem():
        getitem_str = f'''
    def __getitem__(self, index):
        if (type(index) == str):
            if (index in self.__dict__):
                return self.__dict__[index]
            raise IndexError
        elif (type(index) == int):
            try:
                return self.__dict__[self._fields[index]]
            except(IndexError):
                raise IndexError
        else:
            raise IndexError'''
        return getitem_str
    
    
    def gen_eq():
        eq_str = f'''
    def __eq__(self, obj):
        if (type(self) != type(obj)):
            return False
        for i in range(len(self._fields)):
            if self[i] != obj[i]:
                return False
        return True'''
        return eq_str
    
    
    def gen_replace(type_name, field_list):
        replace_str = f'''
    def _replace(self, **kargs):
        print(kargs)
        if self._mutable == False:
            new_obj = {type_name}(field_list)
            for k in kargs:
                new_obj.k = 1
            return new_obj
            
        elif self._mutable == True:
            for k,v in kargs:
                print(kargs)
            return None
        '''
        return replace_str


    #####STEP 1: TEST TYPE AND FIELD LEGALITY#####
    #Checks if type_name is legal
    type_check1 = re.match('^[a-zA-Z][\w|_]*$', str(type_name))
    if type_check1 == None or str(type_name) in keyword.kwlist: #type_check is None if type_name does not match
        raise SyntaxError ('type_name must be legal (start with a letter, plus 0 or more letters, digits, or underscores)')
    
    #Checks type of field_names, organizes into field_list format
    if type(field_names) == list:
        field_list = [x for x in unique(field_names)]
    elif type(field_names) == str:
        if ',' in field_names:
            field_list = [x.strip() for x in unique(field_names.split(','))]
        else:
            field_list = [x.strip() for x in unique(field_names.split())]

    else:
        raise SyntaxError('field_names must be type string or list')
    
    #Checks if each field in field_list is legal
    for field in field_list:   
        type_check2 = re.match('^[a-zA-Z][\w|_]*$', field)
        if type_check2 == None or str(field) in keyword.kwlist:
            raise SyntaxError ('field_names must be legal (start with a letter, plus 0 or more letters or digits)')
            
    
    #STEP 2: CREATE CLASS DEFINITION   
    # bind class_definition (used below) to the string constructed for the class
    
    
    class_definition = f'''
class {type_name}:

    {gen_init(field_list)}

    {gen_repr(type_name, field_list)}

    {gen_gets(field_list)}
    
    {gen_getitem()}
    
    {gen_eq()}
    
    {gen_replace(type_name, field_list)}
    '''  


    # While debugging, remove comment below showing source code for the class
    # show_listing(class_definition)
    
    # Execute this class_definition str in a local name space; then, bind the
    #   source_code attribute to class_defintion; after that try, return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__  =  f'pnamedtuple_{type_name}')
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):   
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test pnamedtuple in script below: use Point = pnamedtuple('Point','x,y')


    #driver tests
    import driver
    driver.default_file_name = 'bscp3S18.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
