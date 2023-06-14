import random
from csv import writer
import time
import numpy as np

from constructor import InitialConstructor
from heuristic import Heuristic
from tools import Tools
from data import WEING1,WEING2,WEING3,WEING4,WEING5,WEING6,WEING7,WEING8
from data import WEISH01,WEISH02,WEISH03,WEISH04,WEISH05,WEISH06,WEISH07,WEISH08,WEISH09,WEISH10,WEISH11,WEISH12,WEISH13,WEISH14,WEISH15,WEISH16,WEISH17,WEISH18,WEISH19,WEISH20,WEISH21,WEISH22,WEISH23,WEISH24,WEISH25,WEISH26,WEISH27,WEISH28,WEISH29,WEISH30
from data import SENTO1,SENTO2
from data import PB1,PB2,PB4,PB5,PB6,PB7
from data import HP1,HP2

class Model():
    def __init__(self,data):
        self.data = data
        self.tools = Tools(weights=self.data.weights,rest=self.data.rest,capacities=self.data.capacities)
        self.constructor = InitialConstructor(weights=self.data.weights,rest=self.data.rest,capacities=self.data.capacities)
        self.heuristic = Heuristic()

    def GRASP(self,n_solutions,alpha):
        start_time = time.time()

        list_of_best_evaluations = [0]

        print(self.data.name_data)
        solution_list = self.constructor.random_constructor(n_solutions=n_solutions,alpha=alpha)
        local_optimas = []
        for sol in solution_list:

            list_of_sol_evaluation = []

            used = sol.copy()
            s_current = self.tools.evaluate(used)
            neighbors = self.heuristic.create_neighbors_3t(used)
            random.shuffle(neighbors)

        
            while neighbors:
            # for i in range(len(neighbors)):
                print(len(neighbors))
                n = neighbors.pop(0)
                if self.tools.check_constrains(n):
                    s_proposed = self.tools.evaluate(n)
                    if s_proposed > s_current:
                        used = n
                        s_current = s_proposed

                        neighbors = self.heuristic.create_neighbors_3t(used)
                        random.shuffle(neighbors)
                        print('RESTART -----------------------------------')

                list_of_sol_evaluation.append((s_current))
            

            if list_of_sol_evaluation[-1] > list_of_best_evaluations[-1]:
                list_of_best_evaluations = list_of_sol_evaluation


            print("Random Start Solution: {} \nCost: {}".format(used,s_current))
            local_optimas.append((used,s_current))


        lista_ordenada = sorted(local_optimas, key=lambda x: x[1], reverse=True)
        # print(lista_ordenada)
        # print(self.data.optimum)

        final_time = time.time()

        with open('GRASP.csv', 'a') as f_object:
            writer_object = writer(f_object)
            List = [self.data.name_data,n_solutions,alpha,lista_ordenada[0][0],lista_ordenada[0][1],(self.data.optimum-lista_ordenada[0][1])/self.data.optimum,final_time-start_time,'3t',len(self.data.weights),len(self.data.capacities),self.tools.transform_list(list_of_best_evaluations,self.data.optimum)]
            writer_object.writerow(List)
            f_object.close()    

    def genetic(self,n_solutions,alpha,parts,n_genetic_output,chance_of_mutation):
        start_time = time.time()

        genetic_solutions = []
        print(self.data.name_data)
        solution_list = self.constructor.random_constructor(n_solutions=n_solutions,alpha=alpha)

        end_indicator = True
        while end_indicator:
            # print(solution_list)
            solution_list_results = [(i,self.tools.evaluate(i)) for i in solution_list]
            best_current_solution = self.constructor.tuple_ordering(solution_list_results)[-1]
            # print(best_current_solution)
            genetic_solutions = self.heuristic.create_neighbors_genetic(n_solutions=n_solutions,solution_list=solution_list,parts=parts,tool=self.tools)
            genetic_solutions = [self.heuristic.prob_mutation(vec=i,tool=self.tools,chance_of_mutation=chance_of_mutation) for i in genetic_solutions]
            genetic_solutions_results = [(i,self.tools.evaluate(i)) for i in genetic_solutions]
            genetic_solutions_results = self.constructor.tuple_ordering(genetic_solutions_results)
            # print(genetic_solutions_results)
            
            if genetic_solutions_results[-1][1] <= best_current_solution[1]:
                end_indicator = False
                best_vector = best_current_solution[0]
                best_score = best_current_solution[1]
            else:
                results = genetic_solutions_results[-1*n_genetic_output:]
                results = [np.array(i[0]) for i in results]
                rand = random.choices(solution_list,k=n_solutions-n_genetic_output)
                for cel in rand:
                    results.append(cel)
                solution_list = results.copy()

        final_time = time.time()

        with open('genetic.csv', 'a') as f_object:
            writer_object = writer(f_object)
            List = [self.data.name_data,n_solutions,alpha,best_vector,best_score,(self.data.optimum-best_score)/self.data.optimum,final_time-start_time,parts,n_genetic_output,chance_of_mutation]
            writer_object.writerow(List)
            f_object.close()

if __name__ == "__main__":
    weing = [WEING1(),WEING2(),WEING3(),WEING4(),WEING5(),WEING6(),WEING7(),WEING8()]
    weish = [WEISH01(),WEISH02(),WEISH03(),WEISH04(),WEISH05(),WEISH06(),WEISH07(),WEISH08(),WEISH09(),WEISH10(),
             WEISH11(),WEISH12(),WEISH13(),WEISH14(),WEISH15(),WEISH16(),WEISH17(),WEISH18(),WEISH19(),WEISH20(),
             WEISH21(),WEISH22(),WEISH23(),WEISH24(),WEISH25(),WEISH26(),WEISH27(),WEISH28(),WEISH29(),WEISH30()]
    sento = [SENTO1(),SENTO2()]
    pb = [PB1(),PB2(),PB4(),PB5(),PB6(),PB7()]
    hp = [HP1(),HP2()]

    for data in hp:
        for i in range(3):
            data = data
            N_SOLUTIONS = 1 # number of vectors
            ALPHA = 0.8 # proportion of 0s

            model = Model(data)
            model.GRASP(n_solutions=N_SOLUTIONS,alpha=ALPHA)


    # model = Model(WEING1())
    # model.genetic(n_solutions=10,alpha=0.6,parts=2,n_genetic_output=5,chance_of_mutation=0.5)

    # for data in hp:
    #     for i in range(5):
    #         data = data
    #         N_SOLUTIONS = 30 # number of vectors
    #         ALPHA = 0.8 # proportion of 0s
    #         PARTS = 2 # split gene
    #         N_GENETIC_OUTPUT = 15 # many vectors kept from genetic approach
    #         CHANCE_OF_MUTATION = 0.8 # probability of mutating a vector

    #         model = Model(data)
    #         model.genetic(n_solutions=N_SOLUTIONS,alpha=ALPHA,parts=PARTS,n_genetic_output=N_GENETIC_OUTPUT,chance_of_mutation=CHANCE_OF_MUTATION)

