import numpy as np

class Tools():
    def __init__(self,weights,rest,capacities):
        self.weights = weights
        self.rest = rest
        self.capacities = capacities

    def check_constrains(self,used):
        mult = np.multiply(self.rest,used)
        sum = np.sum(mult,axis=1)
        diff = self.capacities - sum
        if any(diff < 0):
            return False
        else:
            return True

    def evaluate(self,used):
        mult = np.multiply(self.weights,used)
        sum = np.sum(mult)
        return sum

    def transform_list(self,current_list,best):
        new_list = []
        for i in current_list:
            new_list.append((best-i)/best)
        return new_list