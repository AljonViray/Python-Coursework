# Submitter: dmishkan(Mishkanian, Daniel)
# Partner: asviray(Viray, Aljon)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody


def read_fa(file : open) -> {str:{str:str}}:
    fa = dict()
    for line in file.readlines():
        x = line.strip().split(';')
        
        k = []
        v = []
        for i in range(1, len(x), 2):
            k.append(x[i])
            v.append(x[i+1])
             
        zipped = zip(k,v)
        fa.update({x[0]: dict([tup for tup in zipped])})
        
    return fa


def fa_as_str(fa : {str:{str:str}}) -> str:
    string = ""
    for key in sorted(fa.keys()):
        values = []
        for k in sorted(fa[key].keys()):
            tup = (k, fa[key][k])
            values.append(tup)
            
        string += '  ' + str(key) + ' transitions: ' + str(values) + '\n'
    return string        


def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    
    def alternator(states: list(fa.keys()), current_state: str):
        if current_state == states[0]:
            return states[1]
        elif current_state == states[1]:
            return states[0]
    
    fa_result = [state]
    for i in inputs:
        if i == '0':
            fa_result.append((i, state))
  
        elif i == '1':
            state = alternator(list(fa.keys()), state)
            fa_result.append((i, state))

        else:
            fa_result.append((i, None))
            
    return fa_result
    

def interpret(fa_result : [None]) -> str:
    string = f"Start state = {fa_result[0]}\n"
    
    for i in range(1, len(fa_result)):
        string += f'  Input = {fa_result[i][0]}; '
        
        if fa_result[i][0] not in ['0','1']:
            string += (f'illegal input: simulation terminated\nStop state = None\n')
            return string
        
        string += f'new state = {fa_result[i][1]}\n'

    string += (f'Stop state = {fa_result[i][-1]}\n')
    return string




if __name__ == '__main__':
    # Write script here
    file = input('Choose the file name representing the finite automaton: ')  
    fa = read_fa(open(file))
       
    print('\nThe Description of the chosen Finite Automaton')
    print(fa_as_str(fa))
      
    file_input = input('Choose the file name representing the start-states and their inputs: ')   
      
    fa_input = (open(file_input))
    for line in fa_input.readlines():
        input_list = line.strip().split(';')
         
        fa_results = process(fa, input_list[0], list(input_list[1: len(input_list)]))
        print(interpret(fa_results))
              
              
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
