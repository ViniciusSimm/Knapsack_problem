import random
from csv import writer

from constructor import InitialConstructor
from heuristic import Heuristic
from model import Model
from data import WEING1,SENTO1,SENTO2,WEING2,WEING3

data = WEING3()
model = Model(weights=data.weights,rest=data.rest,capacities=data.capacities)
constructor = InitialConstructor(weights=data.weights,rest=data.rest,capacities=data.capacities)
heuristic = Heuristic()

N_SOLUTIONS = 5 # number of vectors
ALPHA = 0.8 # proportion of 0s

print(data.name_data)

solution_list = constructor.random_constructor(n_solutions=N_SOLUTIONS,alpha=ALPHA)

local_optimas = []

for sol in solution_list:

    used = sol.copy()
    s_current = model.evaluate(used)
    neighbors = heuristic.create_neighbors_2t(used)
    random.shuffle(neighbors)

    print("Random Start Solution: {} \nCost: {}".format(used,s_current))

    for i in range(len(neighbors)):
        n = neighbors[i]
        if model.check_constrains(n):
            s_proposed = model.evaluate(n)
            if s_proposed > s_current:
                used = n
                s_current = s_proposed

                neighbors = heuristic.create_neighbors_2t(used)
                random.shuffle(neighbors)
                i = 0
            
    print("Random Start Solution: {} \nCost: {}".format(used,s_current))

    local_optimas.append((used,s_current))


lista_ordenada = sorted(local_optimas, key=lambda x: x[1], reverse=True)
print(lista_ordenada)

with open('GRASP.csv', 'a') as f_object:
    writer_object = writer(f_object)
    List = [data.name_data,N_SOLUTIONS,ALPHA,lista_ordenada[0][0],lista_ordenada[0][1]]
    writer_object.writerow(List)
    f_object.close()