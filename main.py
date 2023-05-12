import random
from csv import writer

from constructor import InitialConstructor
from heuristic import Heuristic
from model import Model
from data import WEING1,WEING2,WEING3,WEING4,WEING5,WEING6,WEING7,WEING8
from data import WEISH01,WEISH02,WEISH03,WEISH04,WEISH05,WEISH06,WEISH07,WEISH08,WEISH09,WEISH10,WEISH11,WEISH12,WEISH13,WEISH14,WEISH15,WEISH16,WEISH17,WEISH18,WEISH19,WEISH20,WEISH21,WEISH22,WEISH23,WEISH24,WEISH25,WEISH26,WEISH27,WEISH28,WEISH29,WEISH30
from data import SENTO1,SENTO2
from data import PB1,PB2,PB4,PB5,PB6,PB7
from data import HP1,HP2

data = WEING1()
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
print(data.optimum)

with open('GRASP.csv', 'a') as f_object:
    writer_object = writer(f_object)
    List = [data.name_data,N_SOLUTIONS,ALPHA,lista_ordenada[0][0],lista_ordenada[0][1],(data.optimum-lista_ordenada[0][1])/data.optimum]
    writer_object.writerow(List)
    f_object.close()
