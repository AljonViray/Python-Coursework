# Submitter: dmishkan(Mishkanian, Daniel)
# Partner: asviray(Viray, Aljon)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import prompt
import goody

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    preferences = dict()
    for line in open_file.readlines():
        x = line.strip().split(';')
        preferences.update({x[0]: [None, [x[n] for n in range(1, len(x))]]})
    return preferences


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    string = ""
    for k in sorted(d.keys(), key=key, reverse=reverse):
        string += '  ' + str(k) + ' -> ' + str(d[k]) + '\n'
    return string        


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return [i for i in order if p1 == i or p2 == i][0]


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(k, men[k][0]) for k in men}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    import copy
    men_copy = men.copy()  
    
    unmatched = {}
    for man in men_copy:
        unmatched.add(man)
        
    proposal = unmatched.pop()
    return men[proposal]
  
  
  
    
if __name__ == '__main__':
    # Write script here
    men_file = input('Choose the file name representing preferences of the men: ')
    women_file = input('Choose the file name representing preferences of the women: ')
   
    men = read_match_preferences(open(men_file))
    women = read_match_preferences(open(women_file))
  
    men_str = dict_as_str(men)
    women_str = dict_as_str(women)
    print('Men Preferences\n' + men_str)
    print('Women Preferences\n' + women_str)
     
    trace = input('Choose whether to trace this algorithm[True]: ')
    
    print(make_match(men, women, trace))

    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
