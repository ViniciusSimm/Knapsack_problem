import numpy as np
from tools import Tools
import random

class Heuristic():

    def create_neighbors_1t(self,used):
        neighbors = []
        for i in range(len(used)):
            neighbor = used.copy()
            neighbor[i] = 1 - neighbor[i]
            neighbors.append(neighbor)
        return neighbors

    def create_neighbors_2t(self,used):
        first_neighbors = self.create_neighbors_1t(used)
        neighbors = []
        for sol in first_neighbors:
            second_neighbors = self.create_neighbors_1t(used=sol)
            neighbors.extend(second_neighbors)
        return neighbors

    def create_neighbors_3t(self,used):
        second_neighbors = self.create_neighbors_2t(used)
        neighbors = []
        for sol in second_neighbors:
            second_neighbors = self.create_neighbors_1t(used=sol)
            neighbors.extend(second_neighbors)
        return neighbors
    
    def divide_vector(self,vec,n):
        k, m = divmod(len(vec), n)
        return list(vec[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

    def combine_two_vectors(self,vec1,vec2,parts):
        vec1 = self.divide_vector(vec1,parts)
        vec2 = self.divide_vector(vec2,parts)

        subv1 = []
        subv2 = []

        for i in range(len(vec1)):
            if i%2 != 0:
                subv1.extend(vec1[i])
                subv2.extend(vec2[i])
            else:
                subv1.extend(vec2[i])
                subv2.extend(vec1[i])
        
        return subv1,subv2

    def create_neighbors_genetic(self,n_solutions,solution_list,parts,tool):
        genetic_solutions = []
        a = 0
        while a < n_solutions:
            b = a+1
            while b < n_solutions:
                subv1,subv2 = self.combine_two_vectors(vec1=solution_list[a],vec2=solution_list[b],parts=parts)

                if tool.check_constrains(subv1):
                    genetic_solutions.append(subv1)
                
                if tool.check_constrains(subv2):
                    genetic_solutions.append(subv2)

                b = b + 1
            a = a + 1
        
        return genetic_solutions

    def mutation_genetic(self,vec,tool):
        position_to_change = random.randint(0, len(vec)-1)
        vec_alt = vec.copy()
        vec_alt[position_to_change] = 1 - vec_alt[position_to_change]
        if tool.check_constrains(used=vec_alt):
            return vec_alt
        else:
            return vec

    def prob_mutation(self,vec,tool,chance_of_mutation):
        if random.random() < chance_of_mutation:
            vec = self.mutation_genetic(vec=vec,tool=tool)
        return vec

# h = Heuristic()


# h.mutation_genetic([1,0,1,0,1,0,1])
