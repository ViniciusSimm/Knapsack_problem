import numpy as np

class Model():
    def __init__(self,weights,rest,capacities):
        self.weights = weights
        self.rest = rest
        self.capacities = capacities

    def check_constrains(self,used):
        mult = np.multiply(self.rest,used)
        sum = np.sum(mult,axis=1)
        diff = self.capacities - sum
        print(diff)
        if any(diff < 0):
            return False
        else:
            return True

    def evaluate(self,used):
        mult = np.multiply(self.weights,used)
        sum = np.sum(mult)
        print(sum)
        return sum
