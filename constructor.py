import random
import numpy as np
from model import Model

class InitialConstructor(Model):

    def index_ordering(self):
        lista = self.weights
        indices_ordenados = sorted(range(len(lista)), key=lambda i: lista[i], reverse=True)
        lista_ordenada = [lista[i] for i in indices_ordenados]
        return lista_ordenada, indices_ordenados

    def greedy_constructor(self):
        used = np.array([0]*len(self.weights))
        cap = self.capacities.copy()
        sum_weight = 0

        _,ind_weights = self.index_ordering()
        for i in ind_weights:
            diff = cap - self.rest[:,i]
            if any(diff < 0):
                pass
            else:
                cap = cap - self.rest[:,i]
                used[i] = 1
                sum_weight = sum_weight + self.weights[i]

        return used

    def random_list(self,alpha):
        used = [1 if random.random() > alpha else 0 for i in self.weights]
        return used

    def random_constructor(self,n_solutions,alpha):
        solution_list = []
        while len(solution_list) < n_solutions:
            prop_sol = np.array(self.random_list(alpha=alpha))
            if self.check_constrains(prop_sol):
                solution_list.append(prop_sol)

        return solution_list

# weights = [1898, 440, 22507, 270, 14148, 3100, 4650, 30800, 615, 4975, 
#         1160, 4225, 510, 11880, 479, 440, 490, 330, 110, 560, 
#         24355, 2885, 11748, 4550, 750, 3720, 1950, 10500]

# weights = np.array(weights)

# capacities = [600,600]
# capacities = np.array(capacities)

# rest1 = [45, 0, 85, 150, 65, 95, 30, 0, 170, 0, 40, 25, 20, 0, 0, 25, 0, 0, 25, 0, 165, 0, 85, 0, 0, 0, 0, 100]
# rest2 = [30, 20, 125, 5, 80, 25, 35, 73, 12, 15, 15, 40, 5, 10, 10, 12, 10, 9, 0, 20, 60, 40, 50, 36, 49, 40, 19, 150]
# rest = np.array([rest1,rest2])

# creator = InitialConstructor(weights,rest,capacities)
# print(creator.random_constructor(10,0.7))