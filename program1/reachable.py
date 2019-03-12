# Submitter: dmishkan(Mishkanian, Daniel)
# Partner: asviray(Viray, Aljon)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    graph = dict()
    for line in file.readlines():
        key = line.split(";")[0].strip()
        value = line.split(";")[1].strip()
        if key not in graph:
            graph.update({key: {value}})
        else:
            graph[key].add(value)
    return graph


def graph_as_str(graph : {str:{str}}) -> str:
    multiline = ""
    for key, value in sorted(graph.items()):
        multiline += "  " + str(key) + " -> " + str(list(sorted(value))) + "\n"
    return multiline

        
def reachable(graph : {str:{str}}, start : str, trace : bool=False) -> {str}:
        reached_set = set()
        exploring_list = [start]
        
        if start in graph:
            
            while len(exploring_list) > 0:
                
                if trace:
                    print(f"\nreached set = {reached_set}")
                    print(f"exploring list = {exploring_list}") 
                
                next_node = exploring_list.pop(0)
                reached_set.add(next_node)        
                
                if next_node in graph:
                    for reachable in graph[next_node]:
                        if reachable not in reached_set:
                            exploring_list.append(reachable)
                
                if trace:
                    print(f"removing node from exploring list and adding it to reached list: node = {next_node}")
                    print(f"after adding all nodes reachable directly from {next_node} but not already in reached, exploring = {exploring_list}\n") 
            
        return reached_set
        


if __name__ == '__main__':
    
    # For asking for input/running the program
    file = input('Choose the file name representing the graph: ')
    graph = read_graph(open(file))
    print(graph_as_str(graph))
         
    while True:
        start = input('Choose the start node (or choose quit): ')
         
        if start == 'quit':
            break
        
        elif (reachable(graph, start, False) == set()):
            print(f"  Entry Error: '{start}';  Illegal: not a source node.\n  Please enter a legal String\n")
            continue
        
        trace = prompt.for_bool('Choose whether to trace this algorithm[True]')
        print("From " + start + " the reachable nodes are", reachable(graph, start, trace), "\n")              
    
    
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
