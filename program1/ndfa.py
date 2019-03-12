# Submitter: dmishkan(Mishkanian, Daniel)
# Partner: asviray(Viray, Aljon)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
from tkinter.constants import CURRENT


def read_ndfa(file : open) -> {str:{str:{str}}}:
    fa = dict()
    for line in file.readlines():
        x = line.strip().split(';')

        k = []
        v = []
        for i in range(1, len(x), 2):
            k.append(x[i])
            v.append(x[i+1])

        n_dict = dict()
        for j in list(zip(k,v)):
            if j[0] not in n_dict:
                n_dict.update({j[0]: {j[1]}})
            else:
                n_dict[j[0]].add(j[1])
        fa.update({x[0]: n_dict})

    return fa



def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    string = ""
    for key, value in sorted(ndfa.items()):
        l = []
        for k , v in sorted(value.items()):
            l.append((k,sorted(list(v))))
        string += '  ' + str(key) + ' transitions: ' + str(l) + '\n'
    return string

def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    fa_result = [state]
    positions = [state]
    answer_set = set()
    for i in inputs:
        for pos in positions[:]:
            if (i in ndfa[pos]):
                for l in ndfa[pos][i]:
                    answer_set.add(l)
                    positions.append(l)    
            positions.remove(pos)

        fa_result.append((i, answer_set))
        if len(answer_set) == 0:
            return fa_result
        answer_set = set()
    return fa_result

def interpret(result : [None]) -> str:
    string = f"Start state = {result[0]}\n"
    
    for i in range(1, len(result)):
        string += f'  Input = {result[i][0]}; '
        
        if result[i][1] == None:
            string += (f'illegal input: simulation terminated\nStop state = None\n')
            return string
        
        string += f'new possible states = {sorted(list(result[i][1]))}\n'

    string += (f'Stop state(s) = {sorted(list(result[i][-1]))}\n')
    return string





if __name__ == '__main__':
    # Write script here
    
    file = input('Choose the file name representing the finite automaton: ')
    fa = read_ndfa(open(file))
    file2 = input('Choose the file name representing the start-states and their inputs: ')
    fa2 = read_ndfa(open(file2))
    

    print("\nThe Description of the chosen Finite Automaton")
    print(ndfa_as_str(fa))
    for line in open(file2).readlines():
        print("Begin tracing the next FA simulation")
        x = line.strip().split(';')
        print(interpret(process(fa, x[0], x[1:])))
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
