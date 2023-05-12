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
