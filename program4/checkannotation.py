# Submitter: asviray(Viray, Aljon)
# Partner  : dmishkan(Mishkanian, Daniel)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

from goody import type_as_str
import inspect
from _ast import Assert

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self,check,param,value,check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation:
    # Below, setting the class attribute to True allows checking to occur
    #   (but only if self._checking_on is also True)
    checking_on  = True
  
    # set self._checking_on to True too, for checking the decorated function 
    def __init__(self, f):
        self._f = f
        self._checking_on = True
                        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        error_msg = f"{param} failed annotation check(wrong type):\n \
value = {value} was type {type(value)} ...should be type {annot}\n \
{check_history}"

        error_msg_2 = f"{param} annotation inconsistency:\n \
dict should have 1 item but had \n \
annotation = {annot}"
               
        def check_type(self,param,annot,value,check_history):
            assert isinstance(value, annot), error_msg
        
        #works for both lists and tuples!
        def check_list_tuple(self,param,annot,value,check_history):
            assert type(value) == type(annot), error_msg #1) value must be a list
            if len(annot) == 1:
                count = 0
                for inner_value in value: #Checking every element in the list
                    try:
                        self.check(param, annot[0], inner_value, check_history)
                    except AssertionError:
                        check_history += f"list[{count}] check: {annot[0]}\n"
                        assert self.check(param, annot[0], inner_value, check_history), error_msg
                    count += 1
                        
            else:
                for i in range(len(annot)):
                    try:
                        self.check(param, annot[i], value[i])
                    except IndexError:
                        raise AssertionError     
        
        def check_dict(self,param,annot,value,check_history):
            assert type(value) == dict or type(value) in dict.__bases__, error_msg #1) value must be a list
            assert len(annot) == 1, error_msg_2  

            for key in value.keys(): #Checking every element in the list
                self.check(param, list(annot.keys())[0], key, check_history)
            for val in value.values():
                self.check(param, list(annot.values())[0], val, check_history)
                
        def check_set(self,param,annot,value,check_history):
            assert type(value) == type(annot), error_msg #1) value must be a set
            assert len(annot) == 1, error_msg_2 
            correct_annot = [x for x in annot][0] #cannot index a set for the type annotation so had to do this
            
            for v in value:
                self.check(param, correct_annot, v, check_history)
                
        def check_lambda(self,param,annot,value,check_history):
            try:
                annot(value)
            except(TypeError):
                raise AssertionError       
            assert len(annot.__code__.co_varnames) == 1, error_msg
            assert annot(value) == True, error_msg
            
        def check_if_check_method_not_present(self,param,annot,value,check_history):
            try:
                annot.__check_annotation__(self.check,param,value,check_history)
            except(AttributeError):
                raise AssertionError
            
        def check_str(self,param,annot,value,check_history):
            pass
            
        
        
        #Calls to helper functions
        if annot == None: 
            pass #Succeed silently
        elif type(annot) is type: 
            check_type(self,param,annot,value,check_history)
        elif isinstance(annot, list) or isinstance(annot, tuple):
            check_list_tuple(self,param,annot,value,check_history)
        elif isinstance(annot, dict): 
            check_dict(self,param,annot,value,check_history)
        elif isinstance(annot, set) or isinstance(annot, frozenset):
            check_set(self,param,annot,value,check_history)
        elif inspect.isfunction(annot):
            check_lambda(self,param,annot,value,check_history)
        elif (isinstance(annot, str)):
            check_str(self,param,annot,value,check_history)
        else:
            check_if_check_method_not_present(self,param,annot,value,check_history)
            


        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Below, decode check function's annotation; check it against arguments

        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, storing the function header's parameters in order)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if not (param.name in bound_f_signature.arguments):
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
        if type(self).checking_on == False or self.checking_on == False:
            return self._f(*args, **kargs)
        
        try:
#             print('param_arg_bindings:', param_arg_bindings())
#             print('annotations:', self._f.__annotations__, '\n')
            
            # Check the annotation for all parameters (if there are any)
            for param in self._f.__annotations__:
                if param == 'return':
                    continue
                annot = self._f.__annotations__[param] #class/type
                value = param_arg_bindings()[param] #actual value
                self.check(param, annot, value)
                      
            # Compute/remember the value of the decorated function
            
            # If 'return' is in the annotation, check it
            if 'return' in self._f.__annotations__:
                param = 'return'
                annot = self._f.__annotations__[param]
                value = self._f(*args, **kargs)
                self.check(param, annot, value)
            
            # Return the decorated answer
            return self._f(*args, **kargs)
                    
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    def f(x:[[int]]) -> [[int]]:        
        return x
    f = Check_Annotation(f)    
    print(   f([[1,2],[3,4],[5,'a']]) ) #passing case
#     f({1: 2}) #error case
           
    #driver tests
    import driver
    driver.default_file_name = 'bscp4F18.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
