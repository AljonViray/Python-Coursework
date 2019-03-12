from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder

def create_random(n, callable):
    return random_graph(n, callable)

n = 1000
while n < 128001: #Until n reaches 128000
    graph = create_random(n, lambda n: 10*n)

    p = Performance(lambda: spanning_tree(graph), lambda: None, 5, f'Testing spanning_tree using {n} nodes')
    p.evaluate(5)
    p.analyze()
    
    n = n*2 #Double n

        