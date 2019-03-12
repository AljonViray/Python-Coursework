import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder

def create_random(n, callable):
    return random_graph(n, callable)

n = 15000
graph = create_random(n, lambda n: 10*n)

file = 'results.txt'
cProfile.run('spanning_tree(graph)', file)

p = pstats.Stats(file)
# p.strip_dirs().sort_stats(-1).print_stats()

p.strip_dirs().sort_stats('calls').print_stats(10)
# p.strip_dirs().sort_stats('cumulative').print_stats(10)
p.strip_dirs().sort_stats('time').print_stats(10)


