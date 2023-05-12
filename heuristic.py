import numpy as np
from model import Model

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
