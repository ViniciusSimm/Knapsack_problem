import numpy as np

class Data():
    def convert_text_to_list_of_lists(self,text,size_each_list):
        print(len(text.split()))
        n = size_each_list
        megalist = []
        littlelist = []
        for i in text.split():
                littlelist.append(i)
                if len(littlelist) == n:
                        megalist.append(littlelist)
                        littlelist = []
        return megalist
    
    def convert_text_to_list(self,text):
        return text.split()

# class TEMPLATE(Data):
#     def __init__(self):
#         self.name_data = ""

#         self.weights = """"""
        
#         self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

#         self.capacities = """"""
        
#         self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

#         self.rest = """"""

#         self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

#         self.optimum = 0

class WEING1():
    name_data = "WEING1"

    weights = [1898, 440, 22507, 270, 14148, 3100, 4650, 30800, 615, 4975, 
            1160, 4225, 510, 11880, 479, 440, 490, 330, 110, 560, 
            24355, 2885, 11748, 4550, 750, 3720, 1950, 10500]

    weights = np.array(weights)

    capacities = [600,600]
    capacities = np.array(capacities)

    rest1 = [45, 0, 85, 150, 65, 95, 30, 0, 170, 0, 40, 25, 20, 0, 0, 25, 0, 0, 25, 0, 165, 0, 85, 0, 0, 0, 0, 100]
    rest2 = [30, 20, 125, 5, 80, 25, 35, 73, 12, 15, 15, 40, 5, 10, 10, 12, 10, 9, 0, 20, 60, 40, 50, 36, 49, 40, 19, 150]
    rest = np.array([rest1,rest2])

    optimum = 141278



class WEING2(Data):
    def __init__(self):
        self.name_data = "WEING2"

        self.weights = """1898 440 22507 270 14148 3100 4650 30800 615 4975
                        1160 4225 510 11880 479 440 490 330 110 560
                        24355 2885 11748 4550 750 3720 1950 10500"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """500 500"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """45 0 85 150 65 95 30 0 170 0
                        40 25 20 0 0 25 0 0 25 0
                        165 0 85 0 0 0 0 100
                        30 20 125 5 80 25 35 73 12 15
                        15 40 5 10 10 12 10 9 0 20
                        60 40 50 36 49 40 19 150"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 130883

class WEING3(Data):
    def __init__(self):
        self.name_data = "WEING3"

        self.weights = """1898 440 22507 270 14148 3100 4650 30800 615 4975
                        1160 4225 510 11880 479 440 490 330 110 560
                        24355 2885 11748 4550 750 3720 1950 10500"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """300 300"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """45 0 85 150 65 95 30 0 170 0
                        40 25 20 0 0 25 0 0 25 0
                        165 0 85 0 0 0 0 100
                        30 20 125 5 80 25 35 73 12 15
                        15 40 5 10 10 12 10 9 0 20
                        60 40 50 36 49 40 19 150"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 95677

class WEING4(Data):
    def __init__(self):
        self.name_data = "WEING4"

        self.weights = """1898 440 22507 270 14148 3100 4650 30800 615 4975
                        1160 4225 510 11880 479 440 490 330 110 560
                        24355 2885 11748 4550 750 3720 1950 10500"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """300 600"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """45 0 85 150 65 95 30 0 170 0
                        40 25 20 0 0 25 0 0 25 0
                        165 0 85 0 0 0 0 100
                        30 20 125 5 80 25 35 73 12 15
                        15 40 5 10 10 12 10 9 0 20
                        60 40 50 36 49 40 19 150"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 119337

class WEING5(Data):
    def __init__(self):
        self.name_data = "WEING5"

        self.weights = """1898 440 22507 270 14148 3100 4650 30800 615 4975
                        1160 4225 510 11880 479 440 490 330 110 560
                        24355 2885 11748 4550 750 3720 1950 10500"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """600 300"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """45 0 85 150 65 95 30 0 170 0
                        40 25 20 0 0 25 0 0 25 0
                        165 0 85 0 0 0 0 100
                        30 20 125 5 80 25 35 73 12 15
                        15 40 5 10 10 12 10 9 0 20
                        60 40 50 36 49 40 19 150"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 98796

class WEING6(Data):
    def __init__(self):
        self.name_data = "WEING6"

        self.weights = """1898 440 22507 270 14148 3100 4650 30800 615 4975
                        1160 4225 510 11880 479 440 490 330 110 560
                        24355 2885 11748 4550 750 3720 1950 10500"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """562 497"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """45 0 85 150 65 95 30 0 170 0
                        40 25 20 0 0 25 0 0 25 0
                        165 0 85 0 0 0 0 100
                        30 20 125 5 80 25 35 73 12 15
                        15 40 5 10 10 12 10 9 0 20
                        60 40 50 36 49 40 19 150"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 130623


class WEING7(Data):
    def __init__(self):
        self.name_data = "WEING7"

        self.weights = """41850 38261 23800 21697 7074 5587 5560 5500 3450 2391
                        761 460 367 24785 47910 30250 107200 4235 9835 9262
                        15000 6399 6155 10874 37100 27040 4117 32240 1600 4500
                        70610 6570 15290 23840 16500 7010 16020 8000 31026 2568
                        2365 4350 1972 4975 29400 7471 2700 3840 22400 3575
                        13500 1125 11950 12753 10568 15600 20652 13150 2900 1790
                        4970 5770 8180 2450 7140 12470 6010 16000 11100 11093
                        4685 2590 11500 5820 2842 5000 3300 2800 5420 900
                        13300 8450 5300 750 1435 2100 7215 2605 2422 5500
                        8550 2700 540 2550 2450 725 445 700 1720 2675
                        220 300 405 150 70"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """3000 3000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """75 40 365 95 25 17 125 20 22 84
                        75 50 15 0 0 12 0 10 0 50
                        0 0 10 0 0 50 60 150 0 0
                        75 0 102 0 0 40 60 0 165 0
                        0 0 45 0 0 0 25 0 150 0
                        0 0 158 0 85 95 0 89 20 0
                        0 0 0 0 0 80 0 110 0 15
                        0 60 5 135 0 0 25 0 300 35
                        100 0 0 25 0 0 225 25 0 0
                        0 0 0 0 0 5 0 60 0 100
                        0 0 0 0 0
                        0 0 0 0 0 0 0 0 0 0
                        0 0 0 5 10 10 50 2 5 5
                        10 5 6 11 41 30 5 40 2 6
                        100 10 25 39 30 13 30 15 60 5
                        5 10 5 15 91 24 10 15 90 15
                        60 5 55 60 50 75 100 65 15 10
                        30 35 50 15 45 80 40 110 80 80
                        36 20 90 50 25 50 35 30 60 10
                        150 110 70 10 20 30 104 40 40 94
                        150 50 10 50 50 16 10 20 50 90
                        10 15 39 20 20"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 1095445


class WEING8(Data):
    def __init__(self):
        self.name_data = "WEING8"

        self.weights = """41850 38261 23800 21697 7074 5587 5560 5500 3450 2391
                        761 460 367 24785 47910 30250 107200 4235 9835 9262
                        15000 6399 6155 10874 37100 27040 4117 32240 1600 4500
                        70610 6570 15290 23840 16500 7010 16020 8000 31026 2568
                        2365 4350 1972 4975 29400 7471 2700 3840 22400 3575
                        13500 1125 11950 12753 10568 15600 20652 13150 2900 1790
                        4970 5770 8180 2450 7140 12470 6010 16000 11100 11093
                        4685 2590 11500 5820 2842 5000 3300 2800 5420 900
                        13300 8450 5300 750 1435 2100 7215 2605 2422 5500
                        8550 2700 540 2550 2450 725 445 700 1720 2675
                        220 300 405 150 70"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """500 500"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """75 40 365 95 25 17 125 20 22 84
                        75 50 15 0 0 12 0 10 0 50
                        0 0 10 0 0 50 60 150 0 0
                        75 0 102 0 0 40 60 0 165 0
                        0 0 45 0 0 0 25 0 150 0
                        0 0 158 0 85 95 0 89 20 0
                        0 0 0 0 0 80 0 110 0 15
                        0 60 5 135 0 0 25 0 300 35
                        100 0 0 25 0 0 225 25 0 0
                        0 0 0 0 0 5 0 60 0 100
                        0 0 0 0 0
                        0 0 0 0 0 0 0 0 0 0
                        0 0 0 5 10 10 50 2 5 5
                        10 5 6 11 41 30 5 40 2 6
                        100 10 25 39 30 13 30 15 60 5
                        5 10 5 15 91 24 10 15 90 15
                        60 5 55 60 50 75 100 65 15 10
                        30 35 50 15 45 80 40 110 80 80
                        36 20 90 50 25 50 35 30 60 10
                        150 110 70 10 20 30 104 40 40 94
                        150 50 10 50 50 16 10 20 50 90
                        10 15 39 20 20"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 624319

class WEISH01(Data):
    def __init__(self):
        self.name_data = "WEISH01"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """400 500 500 600 600"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                    59 18 0 36 3 8 15 42 9 0
                    42 47 52 32 26 48 55 6 29 84
                    8 66 98 50 0 30 0 88 15 37
                    26 72 61 57 17 27 83 3 9 66
                    97 42 2 44 71 11 25 74 90 20
                    3 74 88 50 55 19 0 6 30 62
                    17 81 25 46 67 28 36 8 1 52
                    19 37 27 62 39 84 16 14 21 5
                    21 40 0 6 82 91 43 30 62 91
                    10 41 12 4 80 77 98 50 78 35
                    7 1 96 67 85 4 23 38 2 57
                    94 86 80 92 31 17 65 51 46 66
                    44 3 26 0 39 20 11 6 55 70
                    11 75 82 35 47 99 5 14 23 38"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 4554


class WEISH02(Data):
    def __init__(self):
        self.name_data = "WEISH02"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """370 650 460 980 870"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                    59 18 0 36 3 8 15 42 9 0
                    42 47 52 32 26 48 55 6 29 84
                    8 66 98 50 0 30 0 88 15 37
                    26 72 61 57 17 27 83 3 9 66
                    97 42 2 44 71 11 25 74 90 20
                    3 74 88 50 55 19 0 6 30 62
                    17 81 25 46 67 28 36 8 1 52
                    19 37 27 62 39 84 16 14 21 5
                    21 40 0 6 82 91 43 30 62 91
                    10 41 12 4 80 77 98 50 78 35
                    7 1 96 67 85 4 23 38 2 57
                    94 86 80 92 31 17 65 51 46 66
                    44 3 26 0 39 20 11 6 55 70
                    11 75 82 35 47 99 5 14 23 38"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 4536


class WEISH03(Data):
    def __init__(self):
        self.name_data = "WEISH03"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """480 800 500 300 620"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 4115


class WEISH04(Data):
    def __init__(self):
        self.name_data = "WEISH04"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """540 270 500 500 750"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 4561


class WEISH05(Data):
    def __init__(self):
        self.name_data = "WEISH05"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """540 240 480 600 790"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 4514


class WEISH06(Data):
    def __init__(self):
        self.name_data = "WEISH06"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """480 760 800 1180 940"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 5557


class WEISH07(Data):
    def __init__(self):
        self.name_data = "WEISH07"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """480 600 700 1200 1200"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 5567


class WEISH08(Data):
    def __init__(self):
        self.name_data = "WEISH08"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """480 760 800 1185 1200"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 5605


class WEISH09(Data):
    def __init__(self):
        self.name_data = "WEISH09"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """750 870 360 800 940"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 5246


class WEISH10(Data):
    def __init__(self):
        self.name_data = "WEISH10"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """850 1400 1500 450 1100"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 6339


class WEISH11(Data):
    def __init__(self):
        self.name_data = "WEISH11"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """880 1340 1360 300 1000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 5643


class WEISH12(Data):
    def __init__(self):
        self.name_data = "WEISH12"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """850 1400 1500 440 1100"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 6339


class WEISH13(Data):
    def __init__(self):
        self.name_data = "WEISH13"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """850 1400 1500 400 1100"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 6159


class WEISH14(Data):
    def __init__(self):
        self.name_data = "WEISH14"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1024 1700 1850 510 1310"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 6954


class WEISH15(Data):
    def __init__(self):
        self.name_data = "WEISH15"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1130 420 1380 1000 1630"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 7486


class WEISH16(Data):
    def __init__(self):
        self.name_data = "WEISH16"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1200 1300 630 1100 1400"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 7289


class WEISH17(Data):
    def __init__(self):
        self.name_data = "WEISH17"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """2090 2200 1190 2460 2320"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 8633


class WEISH18(Data):
    def __init__(self):
        self.name_data = "WEISH18"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """970 1310 1730 2220 2580"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9580


class WEISH19(Data):
    def __init__(self):
        self.name_data = "WEISH19"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1200 1920 2330 620 1460"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 7698


class WEISH20(Data):
    def __init__(self):
        self.name_data = "WEISH20"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1320 700 1730 1954 1810"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9450


class WEISH21(Data):
    def __init__(self):
        self.name_data = "WEISH21"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1320 600 1730 1954 1810"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9074


class WEISH22(Data):
    def __init__(self):
        self.name_data = "WEISH22"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1347 2180 2683 838 1788"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 8947


class WEISH23(Data):
    def __init__(self):
        self.name_data = "WEISH23"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1360 2200 2700 700 1700"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 8344


class WEISH24(Data):
    def __init__(self):
        self.name_data = "WEISH24"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1100 1500 2000 2500 3000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 10220


class WEISH25(Data):
    def __init__(self):
        self.name_data = "WEISH25"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1500 800 2000 2200 2100"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9939


class WEISH26(Data):
    def __init__(self):
        self.name_data = "WEISH26"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74
                        100 72 31 29 316 244 70 82 90 52"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1600 2500 3000 850 2000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        20 8 4 43 17 25 36 60 84 40
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        74 26 10 85 63 31 22 9 92 18
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        3 32 82 20 2 51 18 42 4 26
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        7 86 48 2 1 15 74 80 57 16
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6
                        11 17 48 79 63 77 17 29 18 60"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9584


class WEISH27(Data):
    def __init__(self):
        self.name_data = "WEISH27"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74
                        100 72 31 29 316 244 70 82 90 52"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1600 2500 3000 900 2000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        20 8 4 43 17 25 36 60 84 40
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        74 26 10 85 63 31 22 9 92 18
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        3 32 82 20 2 51 18 42 4 26
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        7 86 48 2 1 15 74 80 57 16
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6
                        11 17 48 79 63 77 17 29 18 60"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9819


class WEISH28(Data):
    def __init__(self):
        self.name_data = "WEISH28"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74
                        100 72 31 29 316 244 70 82 90 52"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1500 2500 3000 820 2000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        20 8 4 43 17 25 36 60 84 40
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        74 26 10 85 63 31 22 9 92 18
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        3 32 82 20 2 51 18 42 4 26
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        7 86 48 2 1 15 74 80 57 16
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6
                        11 17 48 79 63 77 17 29 18 60"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9492


class WEISH29(Data):
    def __init__(self):
        self.name_data = "WEISH29"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74
                        100 72 31 29 316 244 70 82 90 52"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """1600 2500 3000 800 2000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        20 8 4 43 17 25 36 60 84 40
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        74 26 10 85 63 31 22 9 92 18
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        3 32 82 20 2 51 18 42 4 26
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        7 86 48 2 1 15 74 80 57 16
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6
                        11 17 48 79 63 77 17 29 18 60"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 9410


class WEISH30(Data):
    def __init__(self):
        self.name_data = "WEISH30"

        self.weights = """360 83 59 130 431 67 230 52 93 125
                        670 892 600 38 48 147 78 256 63 17
                        120 164 432 35 92 110 22 42 50 323
                        514 28 87 73 78 15 26 78 210 36
                        85 189 274 43 33 10 19 389 276 312
                        94 68 73 192 41 163 16 40 195 138
                        73 152 400 26 14 170 205 57 369 435
                        123 25 94 88 90 146 55 29 82 74
                        100 72 31 29 316 244 70 82 90 52"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """2100 1100 3300 3700 3600"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """7 0 30 22 80 94 11 81 70 64
                        59 18 0 36 3 8 15 42 9 0
                        42 47 52 32 26 48 55 6 29 84
                        2 4 18 56 7 29 93 44 71 3
                        86 66 31 65 0 79 20 65 52 13
                        48 14 5 72 14 39 46 27 11 91
                        15 25 0 94 53 48 27 99 6 17
                        69 43 0 57 7 21 78 10 37 26
                        20 8 4 43 17 25 36 60 84 40
                        8 66 98 50 0 30 0 88 15 37
                        26 72 61 57 17 27 83 3 9 66
                        97 42 2 44 71 11 25 74 90 20
                        0 38 33 14 9 23 12 58 6 14
                        78 0 12 99 84 31 16 7 33 20
                        5 18 96 63 31 0 70 4 66 9
                        15 25 2 0 48 1 40 31 82 79
                        56 34 3 19 52 36 95 6 35 34
                        74 26 10 85 63 31 22 9 92 18
                        3 74 88 50 55 19 0 6 30 62
                        17 81 25 46 67 28 36 8 1 52
                        19 37 27 62 39 84 16 14 21 5
                        60 82 72 89 16 5 29 7 80 97
                        41 46 15 92 51 76 57 90 10 37
                        25 93 5 39 0 97 6 96 2 81
                        69 4 32 78 65 83 62 89 45 53
                        52 76 72 23 89 48 41 1 27 19
                        3 32 82 20 2 51 18 42 4 26
                        21 40 0 6 82 91 43 30 62 91
                        10 41 12 4 80 77 98 50 78 35
                        7 1 96 67 85 4 23 38 2 57
                        4 53 0 33 2 25 14 97 87 42
                        15 65 19 83 67 70 80 39 9 5
                        41 31 36 15 30 87 28 13 40 0
                        51 79 75 43 91 60 24 18 85 83
                        3 85 2 5 51 63 52 85 17 62
                        7 86 48 2 1 15 74 80 57 16
                        94 86 80 92 31 17 65 51 46 66
                        44 3 26 0 39 20 11 6 55 70
                        11 75 82 35 47 99 5 14 23 38
                        94 66 64 27 77 50 28 25 61 10
                        30 15 12 24 90 25 39 47 98 83
                        56 36 6 66 89 45 38 1 18 88
                        19 39 20 1 7 34 68 32 31 58
                        41 99 92 67 33 26 25 68 37 6
                        11 17 48 79 63 77 17 29 18 60"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 11191


class SENTO1(Data):
    def __init__(self):
        self.name_data = "SENTO1"

        self.weights = [2, 77, 6, 67, 930, 3, 6, 270, 33, 13,
                110, 21, 56, 974, 47, 734, 238, 75, 200, 51,
                47, 63, 7, 6, 468, 72, 95, 82, 91, 83,
                27, 13, 6, 76, 55, 72, 300, 6, 65, 39,
                63, 61, 52, 85, 29, 640, 558, 53, 47, 25,
                3, 6, 568, 6, 2, 780, 69, 31, 774, 22]
        
        self.weights = np.array(self.weights)

        self.capacities = [6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 4000,
                        6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 4000,
                        6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 6000, 4000]
        
        self.capacities = np.array(self.capacities)

        self.rest = """47 774 76 56 59 22 42 1 21 760
                        818 62 42 36 785 29 662 49 608 116
                        834 57 42 39 994 690 27 524 23 96
                        667 490 805 46 19 26 97 71 699 465
                        53 26 123 20 25 450 22 979 75 96
                        27 41 21 81 15 76 97 646 898 37
                        73 67 27 99 35 794 53 378 234 32
                        792 97 64 19 435 712 837 22 504 332
                        13 65 86 29 894 266 75 16 86 91
                        67 445 118 73 97 370 88 85 165 268
                        758 21 255 81 5 774 39 377 18 370
                        96 61 57 23 13 164 908 834 960 87
                        36 42 56 96 438 49 57 16 978 9
                        644 584 82 550 283 340 596 788 33 350
                        55 59 348 66 468 983 6 33 42 96
                        464 175 33 97 15 22 9 554 358 587
                        71 23 931 931 94 798 73 873 22 39
                        71 864 59 82 16 444 37 475 65 5
                        47 114 26 668 82 43 55 55 56 27
                        716 7 77 26 950 320 350 95 714 789
                        430 97 590 32 69 264 19 51 97 33
                        571 388 602 140 15 85 42 66 778 936
                        61 23 449 973 828 33 53 297 75 3
                        54 27 918 11 620 13 28 80 79 3
                        61 720 7 31 22 82 688 19 82 654
                        809 99 81 97 830 826 775 72 9 719
                        740 860 72 30 82 112 66 638 150 13
                        586 590 519 2 320 13 964 754 70 241
                        72 12 996 868 36 91 79 221 49 690
                        23 18 748 408 688 97 85 777 294 17
                        698 53 290 3 62 37 704 810 42 17
                        983 11 45 56 234 389 712 664 59 15
                        22 91 57 784 75 719 294 978 75 86
                        105 227 760 2 190 3 71 32 210 678
                        41 93 47 581 37 977 62 503 32 85
                        31 36 30 328 74 31 56 891 62 97
                        71 37 978 93 9 23 47 71 744 9
                        619 32 214 31 796 103 593 16 468 700
                        884 67 36 3 93 71 734 504 81 53
                        509 114 293 31 75 59 99 11 67 306
                        96 218 845 303 3 319 86 724 22 838
                        82 5 330 58 55 66 53 916 89 56
                        33 27 13 57 6 87 21 12 15 290
                        206 420 32 880 854 417 770 4 12 952
                        604 13 96 910 34 460 76 16 140 100
                        876 622 559 39 640 59 6 244 232 513
                        644 7 813 624 990 274 808 372 2 694
                        804 39 5 644 914 484 1 8 43 92
                        16 36 538 210 844 520 33 73 100 284
                        650 85 894 2 206 637 324 318 7 566
                        46 818 92 65 520 721 90 53 174 43
                        320 812 382 16 878 678 29 92 755 827
                        27 218 143 12 57 480 154 944 7 730
                        12 65 67 39 390 32 39 318 47 86
                        45 51 59 21 53 43 25 7 42 27
                        310 45 72 53 798 304 354 79 45 44
                        52 76 45 26 27 968 86 16 62 85
                        790 208 390 36 62 83 93 16 574 150
                        99 7 920 860 12 404 31 560 37 32
                        9 62 7 43 17 77 73 368 66 82
                        11 51 97 26 83 426 92 39 66 2
                        23 93 85 660 85 774 77 77 927 868
                        7 554 760 104 48 202 45 75 51 55
                        716 752 37 95 267 91 5 956 444 529
                        96 99 17 99 62 7 394 580 604 89
                        678 476 97 234 1 608 19 69 676 51
                        410 89 414 81 130 491 6 238 79 43
                        5 288 910 204 948 19 644 21 295 11
                        6 595 904 67 51 703 430 95 408 89
                        11 495 844 13 417 570 9 429 16 939
                        430 270 49 72 65 66 338 994 167 76
                        47 211 87 39 1 570 85 134 967 12
                        553 63 35 63 98 402 664 85 458 834
                        3 62 508 7 1 72 88 45 496 43
                        750 222 96 31 278 184 36 7 210 55
                        653 51 35 37 393 2 49 884 418 379
                        75 338 51 21 29 95 790 846 720 71
                        728 930 95 1 910 5 804 5 284 128
                        423 6 58 36 37 321 22 26 16 27
                        218 530 93 55 89 71 828 75 628 67
                        66 622 440 91 73 790 710 59 83 968
                        129 632 170 67 613 608 43 71 730 910
                        36 92 950 138 23 95 460 62 189 73
                        65 943 62 554 46 318 13 540 90 53
                        967 654 46 69 26 769 82 89 15 87
                        46 59 22 840 66 35 684 57 254 230
                        21 586 51 19 984 156 23 748 760 65
                        339 892 13 13 327 65 35 246 71 178
                        83 3 34 624 788 200 980 882 343 550
                        708 542 53 72 86 51 700 524 577 948
                        132 900 72 51 91 150 22 110 154 148
                        99 75 21 544 110 11 52 840 201 2
                        6 663 22 20 89 10 93 964 924 73
                        501 398 3 2 279 5 288 80 91 132
                        620 628 57 79 2 874 36 497 846 22
                        350 866 57 86 83 178 968 52 399 628
                        869 26 710 37 81 89 6 82 82 56
                        96 66 46 13 934 49 394 72 194 408
                        5 541 88 93 36 398 508 89 66 16
                        71 466 7 95 464 41 69 130 488 695
                        82 39 95 53 37 200 87 56 268 71
                        304 855 22 564 47 26 26 370 569 2
                        494 2 25 61 674 638 61 59 62 690
                        630 86 198 24 15 650 75 25 571 338
                        268 958 95 898 56 585 99 83 21 600
                        462 940 96 464 228 93 72 734 89 287
                        174 62 51 73 42 838 82 515 232 91
                        25 47 12 56 65 734 70 48 209 71
                        267 290 31 844 12 570 13 69 65 848
                        72 780 27 96 97 17 69 274 616 36
                        554 236 47 7 47 134 76 62 824 55
                        374 471 478 504 496 754 604 923 330 22
                        97 6 2 16 14 958 53 480 482 93
                        57 641 72 75 51 96 83 47 403 32
                        624 7 96 45 97 148 91 3 69 26
                        22 45 42 2 75 76 96 67 688 2
                        2 224 83 69 41 660 81 89 93 27
                        214 458 66 72 384 59 76 538 15 840
                        65 63 77 33 92 32 35 832 970 49
                        13 8 77 75 51 95 56 63 578 47
                        33 62 928 292 2 340 278 911 818 770
                        464 53 888 55 76 31 389 40 864 36
                        35 37 69 95 22 648 334 14 198 42
                        73 594 95 32 814 45 45 515 634 254
                        42 29 15 83 55 176 35 46 60 296
                        262 598 67 644 80 999 3 727 79 374
                        19 780 400 588 37 86 23 583 518 42
                        56 1 108 83 43 720 570 81 674 25
                        96 218 6 69 107 534 158 56 5 938
                        9 938 274 76 298 9 518 571 47 175
                        63 93 49 94 42 26 79 50 718 926
                        419 810 23 363 519 339 86 751 7 86
                        47 75 55 554 3 800 6 13 85 65
                        99 45 69 73 864 95 199 924 19 948
                        214 3 718 56 278 1 363 86 1 22
                        56 114 13 53 56 19 82 88 99 543
                        674 704 418 670 554 282 5 67 63 466
                        491 49 67 154 956 911 77 635 2 49
                        53 12 79 481 218 26 624 954 13 580
                        130 608 3 37 91 78 743 1 950 45
                        41 718 36 30 534 418 452 359 759 88
                        29 499 55 974 93 56 108 257 93 171
                        13 92 63 714 9 84 890 16 930 967
                        748 5 7 6 327 894 33 629 448 21
                        9 19 7 535 75 3 27 928 21 7
                        864 27 73 61 25 75 876 16 92 22
                        248 11 86 944 872 996 252 2 800 334
                        93 107 254 441 930 744 97 177 498 931
                        694 800 9 36 6 539 35 79 130 860
                        710 7 630 475 903 552 2 45 97 974
                        17 36 77 843 328 22 76 368 39 71
                        35 850 96 93 87 56 972 96 594 864
                        344 76 17 17 576 629 780 640 56 65
                        43 196 520 86 92 31 6 593 174 569
                        89 718 83 8 790 285 780 62 378 313
                        519 2 85 845 931 731 42 365 32 33
                        65 59 2 671 26 364 854 526 570 630
                        33 654 95 41 42 27 584 17 724 59
                        42 26 918 6 242 356 75 644 818 168
                        964 12 97 178 634 21 3 586 47 382
                        804 89 194 21 610 168 79 96 87 266
                        482 46 96 969 629 128 924 812 19 2
                        468 13 9 120 73 7 92 99 93 418
                        224 22 7 29 57 33 949 65 92 898
                        200 57 12 31 296 185 272 91 77 37
                        734 911 27 310 59 33 87 872 73 79
                        920 85 59 72 888 49 12 79 538 947
                        462 444 828 935 518 894 13 591 22 920
                        23 93 87 490 32 63 870 393 52 23
                        63 634 39 83 12 72 131 69 984 87
                        86 99 52 110 183 704 232 674 384 47
                        804 99 83 81 174 99 77 708 7 623
                        114 1 750 49 284 492 11 61 6 449
                        429 52 62 482 826 147 338 911 30 984
                        35 55 21 264 5 35 92 128 65 27
                        9 52 66 51 7 47 670 83 76 7
                        79 37 2 46 480 608 990 53 47 19
                        35 518 71 59 32 87 96 240 52 310
                        86 73 52 31 83 544 16 15 21 774
                        224 7 83 680 554 310 96 844 29 61"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 7772


class SENTO2(Data):
    def __init__(self):
        self.name_data = "SENTO2"

        self.weights = """2 77 6 67 930 3 6 270 33 13
                        110 21 56 974 47 734 238 75 200 51
                        47 63 7 6 468 72 95 82 91 83
                        27 13 6 76 55 72 300 6 65 39
                        63 61 52 85 29 640 558 53 47 25
                        3 6 568 6 2 780 69 31 774 22"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """10000 10000 10000 10000 10000 10000 10000 10000 10000 7000
                        10000 10000 10000 10000 10000 10000 10000 10000 10000 7000
                        10000 10000 10000 10000 10000 10000 10000 10000 10000 7000"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """47 774 76 56 59 22 42 1 21 760
                        818 62 42 36 785 29 662 49 608 116
                        834 57 42 39 994 690 27 524 23 96
                        667 490 805 46 19 26 97 71 699 465
                        53 26 123 20 25 450 22 979 75 96
                        27 41 21 81 15 76 97 646 898 37
                        73 67 27 99 35 794 53 378 234 32
                        792 97 64 19 435 712 837 22 504 332
                        13 65 86 29 894 266 75 16 86 91
                        67 445 118 73 97 370 88 85 165 268
                        758 21 255 81 5 774 39 377 18 370
                        96 61 57 23 13 164 908 834 960 87
                        36 42 56 96 438 49 57 16 978 9
                        644 584 82 550 283 340 596 788 33 350
                        55 59 348 66 468 983 6 33 42 96
                        464 175 33 97 15 22 9 554 358 587
                        71 23 931 931 94 798 73 873 22 39
                        71 864 59 82 16 444 37 475 65 5
                        47 114 26 668 82 43 55 55 56 27
                        716 7 77 26 950 320 350 95 714 789
                        430 97 590 32 69 264 19 51 97 33
                        571 388 602 140 15 85 42 66 778 936
                        61 23 449 973 828 33 53 297 75 3
                        54 27 918 11 620 13 28 80 79 3
                        61 720 7 31 22 82 688 19 82 654
                        809 99 81 97 830 826 775 72 9 719
                        740 860 72 30 82 112 66 638 150 13
                        586 590 519 2 320 13 964 754 70 241
                        72 12 996 868 36 91 79 221 49 690
                        23 18 748 408 688 97 85 777 294 17
                        698 53 290 3 62 37 704 810 42 17
                        983 11 45 56 234 389 712 664 59 15
                        22 91 57 784 75 719 294 978 75 86
                        105 227 760 2 190 3 71 32 210 678
                        41 93 47 581 37 977 62 503 32 85
                        31 36 30 328 74 31 56 891 62 97
                        71 37 978 93 9 23 47 71 744 9
                        619 32 214 31 796 103 593 16 468 700
                        884 67 36 3 93 71 734 504 81 53
                        509 114 293 31 75 59 99 11 67 306
                        96 218 845 303 3 319 86 724 22 838
                        82 5 330 58 55 66 53 916 89 56
                        33 27 13 57 6 87 21 12 15 290
                        206 420 32 880 854 417 770 4 12 952
                        604 13 96 910 34 460 76 16 140 100
                        876 622 559 39 640 59 6 244 232 513
                        644 7 813 624 990 274 808 372 2 694
                        804 39 5 644 914 484 1 8 43 92
                        16 36 538 210 844 520 33 73 100 284
                        650 85 894 2 206 637 324 318 7 566
                        46 818 92 65 520 721 90 53 174 43
                        320 812 382 16 878 678 29 92 755 827
                        27 218 143 12 57 480 154 944 7 730
                        12 65 67 39 390 32 39 318 47 86
                        45 51 59 21 53 43 25 7 42 27
                        310 45 72 53 798 304 354 79 45 44
                        52 76 45 26 27 968 86 16 62 85
                        790 208 390 36 62 83 93 16 574 150
                        99 7 920 860 12 404 31 560 37 32
                        9 62 7 43 17 77 73 368 66 82
                        11 51 97 26 83 426 92 39 66 2
                        23 93 85 660 85 774 77 77 927 868
                        7 554 760 104 48 202 45 75 51 55
                        716 752 37 95 267 91 5 956 444 529
                        96 99 17 99 62 7 394 580 604 89
                        678 476 97 234 1 608 19 69 676 51
                        410 89 414 81 130 491 6 238 79 43
                        5 288 910 204 948 19 644 21 295 11
                        6 595 904 67 51 703 430 95 408 89
                        11 495 844 13 417 570 9 429 16 939
                        430 270 49 72 65 66 338 994 167 76
                        47 211 87 39 1 570 85 134 967 12
                        553 63 35 63 98 402 664 85 458 834
                        3 62 508 7 1 72 88 45 496 43
                        750 222 96 31 278 184 36 7 210 55
                        653 51 35 37 393 2 49 884 418 379
                        75 338 51 21 29 95 790 846 720 71
                        728 930 95 1 910 5 804 5 284 128
                        423 6 58 36 37 321 22 26 16 27
                        218 530 93 55 89 71 828 75 628 67
                        66 622 440 91 73 790 710 59 83 968
                        129 632 170 67 613 608 43 71 730 910
                        36 92 950 138 23 95 460 62 189 73
                        65 943 62 554 46 318 13 540 90 53
                        967 654 46 69 26 769 82 89 15 87
                        46 59 22 840 66 35 684 57 254 230
                        21 586 51 19 984 156 23 748 760 65
                        339 892 13 13 327 65 35 246 71 178
                        83 3 34 624 788 200 980 882 343 550
                        708 542 53 72 86 51 700 524 577 948
                        132 900 72 51 91 150 22 110 154 148
                        99 75 21 544 110 11 52 840 201 2
                        6 663 22 20 89 10 93 964 924 73
                        501 398 3 2 279 5 288 80 91 132
                        620 628 57 79 2 874 36 497 846 22
                        350 866 57 86 83 178 968 52 399 628
                        869 26 710 37 81 89 6 82 82 56
                        96 66 46 13 934 49 394 72 194 408
                        5 541 88 93 36 398 508 89 66 16
                        71 466 7 95 464 41 69 130 488 695
                        82 39 95 53 37 200 87 56 268 71
                        304 855 22 564 47 26 26 370 569 2
                        494 2 25 61 674 638 61 59 62 690
                        630 86 198 24 15 650 75 25 571 338
                        268 958 95 898 56 585 99 83 21 600
                        462 940 96 464 228 93 72 734 89 287
                        174 62 51 73 42 838 82 515 232 91
                        25 47 12 56 65 734 70 48 209 71
                        267 290 31 844 12 570 13 69 65 848
                        72 780 27 96 97 17 69 274 616 36
                        554 236 47 7 47 134 76 62 824 55
                        374 471 478 504 496 754 604 923 330 22
                        97 6 2 16 14 958 53 480 482 93
                        57 641 72 75 51 96 83 47 403 32
                        624 7 96 45 97 148 91 3 69 26
                        22 45 42 2 75 76 96 67 688 2
                        2 224 83 69 41 660 81 89 93 27
                        214 458 66 72 384 59 76 538 15 840
                        65 63 77 33 92 32 35 832 970 49
                        13 8 77 75 51 95 56 63 578 47
                        33 62 928 292 2 340 278 911 818 770
                        464 53 888 55 76 31 389 40 864 36
                        35 37 69 95 22 648 334 14 198 42
                        73 594 95 32 814 45 45 515 634 254
                        42 29 15 83 55 176 35 46 60 296
                        262 598 67 644 80 999 3 727 79 374
                        19 780 400 588 37 86 23 583 518 42
                        56 1 108 83 43 720 570 81 674 25
                        96 218 6 69 107 534 158 56 5 938
                        9 938 274 76 298 9 518 571 47 175
                        63 93 49 94 42 26 79 50 718 926
                        419 810 23 363 519 339 86 751 7 86
                        47 75 55 554 3 800 6 13 85 65
                        99 45 69 73 864 95 199 924 19 948
                        214 3 718 56 278 1 363 86 1 22
                        56 114 13 53 56 19 82 88 99 543
                        674 704 418 670 554 282 5 67 63 466
                        491 49 67 154 956 911 77 635 2 49
                        53 12 79 481 218 26 624 954 13 580
                        130 608 3 37 91 78 743 1 950 45
                        41 718 36 30 534 418 452 359 759 88
                        29 499 55 974 93 56 108 257 93 171
                        13 92 63 714 9 84 890 16 930 967
                        748 5 7 6 327 894 33 629 448 21
                        9 19 7 535 75 3 27 928 21 7
                        864 27 73 61 25 75 876 16 92 22
                        248 11 86 944 872 996 252 2 800 334
                        93 107 254 441 930 744 97 177 498 931
                        694 800 9 36 6 539 35 79 130 860
                        710 7 630 475 903 552 2 45 97 974
                        17 36 77 843 328 22 76 368 39 71
                        35 850 96 93 87 56 972 96 594 864
                        344 76 17 17 576 629 780 640 56 65
                        43 196 520 86 92 31 6 593 174 569
                        89 718 83 8 790 285 780 62 378 313
                        519 2 85 845 931 731 42 365 32 33
                        65 59 2 671 26 364 854 526 570 630
                        33 654 95 41 42 27 584 17 724 59
                        42 26 918 6 242 356 75 644 818 168
                        964 12 97 178 634 21 3 586 47 382
                        804 89 194 21 610 168 79 96 87 266
                        482 46 96 969 629 128 924 812 19 2
                        468 13 9 120 73 7 92 99 93 418
                        224 22 7 29 57 33 949 65 92 898
                        200 57 12 31 296 185 272 91 77 37
                        734 911 27 310 59 33 87 872 73 79
                        920 85 59 72 888 49 12 79 538 947
                        462 444 828 935 518 894 13 591 22 920
                        23 93 87 490 32 63 870 393 52 23
                        63 634 39 83 12 72 131 69 984 87
                        86 99 52 110 183 704 232 674 384 47
                        804 99 83 81 174 99 77 708 7 623
                        114 1 750 49 284 492 11 61 6 449
                        429 52 62 482 826 147 338 911 30 984
                        35 55 21 264 5 35 92 128 65 27
                        9 52 66 51 7 47 670 83 76 7
                        79 37 2 46 480 608 990 53 47 19
                        35 518 71 59 32 87 96 240 52 310
                        86 73 52 31 83 544 16 15 21 774
                        224 7 83 680 554 310 96 844 29 61"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 8722


class PB1(Data):
    def __init__(self):
        self.name_data = "PB1"

        self.weights = """560 1125 68 47 122 196 41 25 115 82 22 631 132
                        420 86 42 103 81 26 49 316 72 71 49 108 116 90"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """207 185 168 160"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """40 91 3 3 18 25 1 1 8 1 1 49 8
                        21 6 1 5 8 1 0 42 6 4 8 0 10 1
                        16 92 4 6 0 8 2 1 6 2 1 70 9
                        22 4 1 5 6 0 4 8 4 3 0 10 0 6
                        38 39 5 8 12 15 0 1 20 3 0 40 6
                        8 0 6 4 4 1 5 8 2 8 0 20 0 0
                        38 52 7 0 3 4 1 2 4 6 1 18 15
                        38 10 4 8 0 3 0 6 1 3 0 3 5 4"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 3090

class PB2(Data):
    def __init__(self):
        self.name_data = "PB2"

        self.weights = """560 620 68 328 47 122 196 41 25 115
                        82 22 631 132 420 86 42 103 215 81
                        91 26 49 316 72 71 49 108 116 90
                        215 58 47 81"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """163 165 239 168"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """40 30 3 12 3 18
                        25 1 1 8 1 1 49 8 21 6
                        1 5 10 8 2 1 0 42 6 4
                        8 0 10 1 8 3 2 4
                        16 16
                        4 18 6 0 8 2 1 6 2 1
                        70 9 22 4 1 5 10 6 4 0
                        4 8 4 3 0 10 0 6 22 0
                        2 2
                        38 71 5 40 8 12 15 0
                        1 20 3 0 40 6 8 0 6 4
                        22 4 6 1 5 8 2 8 0 20
                        0 0 13 6 1 2
                        38 42 7 20
                        0 3 4 1 2 4 6 1 18 15
                        38 10 4 8 6 0 0 3 0 6
                        1 3 0 3 5 4 18 3 4 0"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 3186


class PB4(Data):
    def __init__(self):
        self.name_data = "PB4"

        self.weights = """7074 5587 5500 3450 367 4235 9262 6155 32240 1600
                        4500 6570 7010 16020 8000 2568 2365 4350 4975 29400
                        7471 3840 3575 1125 1790 2450 540 445 220"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """153 154"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """25
                        17 20 22 15 10 50 10 150 0 0
                        0 40 60 0 0 0 0 0 0 0
                        0 0 0 0 0 0 0 0
                        0 0
                        0 0 0 2 5 6 40 2 6 10
                        13 30 15 5 5 10 15 91 24 15
                        15 5 10 15 10 10 10"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 95168


class PB5(Data):
    def __init__(self):
        self.name_data = "PB5"

        self.weights = """245 177 291 237 114 237 194 211 231 211
                        97 168 174 134 308 271 131 211 97 282"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """463 451 623 493 551 647 624 511 595 526"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """77 12 57 7 21 20 85 52 72 90
                        62 71 93 8 79 68 68 44 13 52
                        21 85 87 82 26 61 36 1 14 19
                        74 26 85 24 56 63 0 12 1 39
                        72 58 72 93 3 93 17 54 92 79
                        12 20 24 30 99 79 15 11 8 89
                        76 14 86 37 12 48 54 58 32 15
                        6 54 32 32 71 61 29 92 20 73
                        11 62 93 56 80 52 93 38 89 33
                        17 32 35 76 51 31 40 73 42 78
                        28 85 3 31 93 44 93 73 35 28
                        11 37 99 73 91 67 7 95 15 97
                        32 42 54 90 59 98 94 88 59 86
                        10 0 59 15 76 97 55 87 70 1
                        77 18 87 61 64 37 41 39 3 18
                        20 55 50 30 51 92 88 55 60 86
                        53 83 68 50 86 20 19 58 48 99
                        57 67 21 36 41 13 34 94 50 50
                        41 68 47 16 5 9 35 62 88 73
                        64 96 9 62 79 27 16 24 30 60"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 2139


class PB6(Data):
    def __init__(self):
        self.name_data = "PB6"

        self.weights = """82 77 110 67 61 3 6 85 2 22
                        238 33 56 63 69 47 63 75 6 83
                        47 47 7 6 53 76 200 29 91 6
                        27 52 6 51 55 72 13 6 65 95"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """3317 1880 2740 4310 2681 3375 4704 3031 3115 2878
                        2609 3321 4142 4670 2130 3323 4766 2590 3573 2888
                        3578 3478 4189 1748 2039 2660 4645 3578 4418 2211"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """524 774 818 56 26 22 42 20 47 37
                        662 21 42 57 97 75 53 49 76 96
                        834 785 42 39 979 46 608 25 23 41
                        667 123 805 116 19 26 760 81 699 27
                        16 67 792 99 21 794 53 81 73 87
                        837 234 64 65 908 18 758 22 27 91
                        13 435 86 29 377 73 504 5 86 61
                        67 255 118 332 97 370 32 23 165 75
                        33 42 644 96 23 49 57 931 36 5
                        596 978 82 59 37 22 71 788 56 96
                        55 283 348 66 873 97 33 94 42 864
                        464 931 33 350 15 22 9 82 358 6
                        51 114 716 668 23 43 55 973 47 3
                        350 56 77 97 28 75 61 95 26 33
                        430 950 590 32 297 140 714 828 97 27
                        571 449 602 789 15 85 27 11 778 19
                        638 720 809 31 12 82 688 868 61 17
                        775 82 81 860 85 49 72 72 7 13
                        740 830 72 30 221 2 9 36 150 18
                        586 996 519 719 320 13 654 408 70 66
                        978 53 983 3 93 37 704 581 698 97
                        712 42 45 91 56 32 41 664 290 86
                        22 234 57 784 503 2 59 37 75 36
                        105 47 760 15 190 3 17 328 210 294
                        504 37 619 93 218 23 47 303 71 56
                        593 744 214 67 53 22 96 16 978 53
                        884 796 36 3 724 31 468 3 81 5
                        509 845 293 700 75 59 9 58 67 734
                        16 27 206 57 7 87 21 624 33 92
                        770 15 32 13 1 2 644 4 13 100
                        604 854 96 910 372 39 12 990 140 39
                        876 813 559 952 640 59 290 644 232 76
                        53 36 650 210 218 520 33 12 16 86
                        324 100 894 818 39 7 27 318 538 43
                        46 206 92 65 944 16 7 57 174 65
                        320 143 382 566 878 678 284 39 755 90
                        16 51 310 21 7 43 25 860 45 82
                        354 42 72 76 73 37 99 79 59 85
                        52 798 45 26 560 36 45 12 62 62
                        790 920 390 44 62 83 27 43 574 86
                        75 51 23 26 99 426 92 99 11 51
                        77 66 85 554 19 604 96 77 97 55
                        7 85 760 104 580 95 927 62 51 476
                        716 17 37 868 267 91 2 234 444 45
                        95 89 5 81 270 491 6 72 410 12
                        644 79 910 595 85 167 430 21 414 89
                        6 948 904 67 994 13 295 65 408 211
                        11 49 844 11 417 570 43 39 16 430
                        7 63 3 63 338 402 664 21 553 128
                        88 458 508 222 804 720 75 45 35 55
                        750 1 96 31 846 37 496 29 210 930
                        653 51 35 43 393 2 834 1 418 36
                        59 6 218 36 92 321 22 138 423 53
                        828 16 93 622 13 189 36 75 58 968
                        66 89 440 91 62 67 628 23 83 943
                        129 950 170 67 613 608 27 554 730 710
                        748 654 46 69 3 769 82 624 967 948
                        684 15 22 586 700 343 83 57 46 65
                        21 66 51 19 882 13 254 788 760 542
                        339 34 13 230 327 65 87 72 71 23
                        964 900 99 51 628 150 22 79 132 628
                        52 154 21 663 968 846 620 840 72 73
                        6 110 22 20 497 2 201 2 924 866
                        501 57 3 2 279 5 148 86 91 93
                        89 26 96 37 39 89 6 53 869 2
                        394 82 46 541 26 268 82 72 710 16
                        5 934 88 93 56 95 194 37 66 855
                        71 95 7 408 464 41 56 564 488 508
                        83 2 630 61 62 638 61 73 494 71
                        75 62 198 958 70 232 174 25 25 600
                        268 15 95 898 515 464 571 42 21 47
                        462 51 96 338 228 93 690 56 89 99
                        62 290 72 844 6 570 13 16 267 32
                        69 65 27 236 83 482 97 274 31 55
                        554 97 47 7 480 504 616 14 824 641
                        374 2 478 36 496 754 848 75 330 76
                        89 7 22 45 63 148 91 33 624 47
                        96 69 42 224 56 970 65 67 96 27
                        2 75 83 69 832 72 688 92 93 8
                        214 77 66 2 384 59 26 75 15 81
                        14 62 464 292 29 340 278 83 33 374
                        389 818 888 37 3 60 42 40 928 42
                        35 76 69 95 46 32 864 55 198 598
                        73 15 95 36 814 45 770 644 634 334
                        56 780 56 588 93 86 23 94 19 86
                        570 518 108 218 86 718 63 81 400 938
                        96 43 6 69 50 76 674 42 5 810
                        9 49 274 25 298 9 42 363 47 158
                        86 75 99 554 704 800 6 670 47 49
                        199 85 69 3 77 63 674 924 55 22
                        214 864 718 56 67 53 19 554 1 49
                        56 418 13 948 56 19 65 154 99 363
                        359 12 130 481 92 26 624 714 53 21
                        743 13 3 718 33 930 13 1 79 88
                        41 91 36 30 16 974 950 9 759 5
                        29 63 55 45 93 56 580 6 93 452
                        2 19 864 535 800 3 27 36 9 974
                        876 21 73 11 2 130 694 16 7 334
                        248 25 86 944 79 441 92 6 800 7
                        93 9 254 22 930 744 7 475 498 252
                        640 36 35 843 718 22 76 8 17 33
                        972 39 96 76 42 378 89 96 77 65
                        344 87 17 17 62 86 594 790 56 2
                        43 83 520 864 92 31 71 845 174 780
                        644 59 33 671 89 364 854 21 65 2
                        584 570 95 26 924 87 804 17 2 168
                        42 42 918 6 96 178 724 610 818 46
                        964 194 97 59 634 21 630 969 47 75
                        91 13 224 120 85 7 92 72 468 920
                        949 93 7 57 13 538 920 65 9 37
                        200 57 12 31 79 310 92 888 77 444
                        734 59 27 898 59 33 418 935 73 272
                        674 93 63 490 1 63 870 49 23 984
                        131 52 39 99 338 6 114 69 87 47
                        86 12 52 110 61 81 984 284 384 52
                        804 750 83 87 174 99 23 482 7 232
                        53 55 9 264 73 35 92 31 35 61
                        670 65 66 37 96 21 86 83 21 19
                        79 7 2 46 15 59 76 83 47 7
                        35 52 71 7 32 87 27 680 52 990"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 776


class PB7(Data):
    def __init__(self):
        self.name_data = "PB7"

        self.weights = """47 77 110 67 65 3 6 39 33 63
                        6 21 56 29 69 61
                        85 6 47 76 47 51 7 53 6 2
                        52 82 91 63 27 13 6 72 55 72 31"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """5875 4351 5221 7099 5746 5560 6840 6069 6333 5229
                        5428 5824 7422 5461 5047 6064 7582 5220 6483 4929
                        5909 5057 6662 3514 4469 4153 7077 6163 6955 3373"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """785 774 818 56 699 22 42 465 21
                        57 76 62 42 25 97 26 20 41 75
                        46 834 116 42 979 81 47 123 524 23
                        53 667 760 805 690 19 26 646
                        435 67
                        792 99 165 794 53 268 234 65 27 97
                        64 5 908 21 81 61 18 73 13 332
                        86 377 23 73 255 16 86 758 67 32
                        118 266 97 370 834
                        283 42 644 96 358
                        49 57 587 978 59 56 584 82 94 37
                        23 931 864 22 97 55 350 348 873 82
                        36 931 33 42 71 464 9 33 983 15
                        22 475
                        950 114 716 668 778 43 55 936 56
                        97 26 7 77 828 28 23 973 27 75
                        140 430 789 590 297 11 47 449 51 97
                        61 571 27 602 264 15 85 80
                        830 720
                        809 31 70 82 688 241 82 860 7 99
                        81 36 85 12 868 18 49 2 740 719
                        72 221 408 61 996 638 150 72 586 654
                        519 112 320 13 777
                        234 53 983 3 210
                        37 704 678 42 91 290 11 45 37 56
                        93 581 36 32 2 22 15 57 503 328
                        698 47 978 75 41 105 17 760 719 190
                        3 891
                        796 37 619 93 67 23 47 306
                        744 67 978 32 214 3 53 218 303 5
                        22 31 884 700 36 724 58 71 845 504
                        81 96 509 9 293 71 75 59 916
                        854
                        27 206 57 232 87 21 513 15 13 13
                        420 32 990 1 7 624 39 2 39 604
                        952 96 372 644 33 813 16 140 644 876
                        290 559 460 640 59 8
                        206 36 650 210
                        755 520 33 827 100 818 538 85 894 57
                        39 218 12 65 7 16 46 566 92 944
                        39 16 143 53 174 27 320 284 382 721
                        878 678 318
                        798 51 310 21 574 43 25
                        150 42 76 59 45 72 12 73 7 860
                        62 37 36 52 44 45 560 43 45 920
                        16 62 99 790 27 390 968 62 83 368
                        85 51 23 26 444 426 92 529 66 554
                        97 93 85 62 19 99 99 476 604 95
                        7 868 760 580 234 11 17 75 51 96
                        716 2 37 202 267 91 69
                        948 89 5
                        81 16 491 6 939 79 595 414 288 910
                        65 85 270 72 211 167 13 6 11 904
                        994 39 410 49 95 408 430 11 43 844
                        703 417 570 134
                        1 63 3 63 418 402
                        664 379 458 222 35 62 508 29 804 338
                        21 930 720 37 750 43 96 846 1 553
                        51 7 210 75 653 834 35 184 393 2
                        5
                        89 6 218 36 730 321 22 910 16
                        622 58 530 93 23 13 92 138 943 189
                        67 66 67 440 62 554 423 950 59 83
                        36 129 27 170 790 613 608 540
                        66 654
                        46 69 71 769 82 178 15 586 46 59
                        22 788 700 3 624 542 343 13 21 230
                        51 882 72 967 34 748 760 83 339 87
                        13 156 327 65 524
                        110 900 99 51 91
                        150 22 132 154 663 72 75 21 2 968
                        628 79 866 846 2 6 2 22 497 86
                        132 57 964 924 620 501 148 3 10 279
                        5 52
                        934 26 96 37 488 89 6 695
                        82 541 710 66 46 37 26 39 53 855
                        268 95 5 408 88 56 564 869 95 89
                        66 82 71 56 7 398 464 41 370
                        15
                        2 630 61 89 638 61 287 62 958 25
                        86 198 42 70 62 73 47 232 464 268
                        338 95 515 56 494 51 83 21 174 462
                        690 96 585 228 93 48
                        97 290 72 844
                        330 570 13 22 65 236 31 780 27 14
                        83 6 16 641 482 504 554 36 47 480
                        75 267 2 62 824 97 374 848 478 134
                        496 754 47
                        75 7 22 45 15 148 91
                        840 69 224 96 45 42 92 56 63 33
                        8 970 72 2 2 83 832 75 624 77
                        89 93 65 214 26 66 660 384 59 63
                        76 62 464 292 634 340 278 254 818 37
                        928 53 888 55 3 29 83 598 60 32
                        35 36 69 46 644 33 15 14 198 42
                        73 770 95 648 814 45 727
                        43 780 56
                        588 47 86 23 175 518 218 400 1 108
                        42 86 93 94 810 718 76 96 25 6
                        50 363 19 49 56 5 63 9 42 274
                        534 298 9 751
                        864 75 99 554 99 800
                        6 543 85 3 55 45 69 554 77 704
                        670 49 63 53 214 948 718 67 154 47
                        418 86 1 674 56 65 13 1 56 19
                        635
                        91 12 130 481 93 26 624 171 13
                        718 79 608 3 9 33 92 714 5 930
                        974 41 45 36 16 6 53 63 359 759
                        13 29 580 55 418 93 56 629
                        25 19
                        864 535 498 3 27 931 21 11 7 27
                        73 6 2 800 36 7 130 441 248 22
                        86 79 475 9 9 2 800 694 93 7
                        254 996 930 744 45
                        87 36 35 843 174
                        22 76 569 39 76 77 850 96 790 42
                        718 8 2 378 86 344 864 17 62 845
                        17 83 640 56 89 43 71 520 629 92
                        31 365
                        42 59 33 671 47 364 854 382
                        570 26 2 654 95 610 924 89 21 46
                        87 178 42 59 918 96 969 65 194 644
                        818 804 964 630 97 356 634 21 812
                        57
                        13 224 120 73 7 92 79 93 57 9
                        22 7 888 13 85 72 444 538 310 200
                        898 12 79 935 468 59 91 77 920 734
                        418 27 185 59 33 591
                        12 93 63 490
                        7 63 870 623 52 99 87 634 39 284
                        338 1 49 52 6 81 86 87 52 61
                        482 23 750 674 384 114 804 23 83 704
                        174 99 911
                        7 55 9 264 52 35 92
                        310 65 37 21 52 66 83 96 73 31
                        7 21 59 79 7 2 15 680 35 52
                        53 47 86 35 27 71 608 32 87 844"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 1035


class HP1(Data):
    def __init__(self):
        self.name_data = "HP1"

        self.weights = """560 1125 68 328 47 122 196 41 25 115
                        82 22 631 132 420 86 42 103 81 26
                        49 316 72 71 49 108 116 90"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """219 203 208 180"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """40 91 3 12 3 18 25 1 1 8
                        1 1 49 8 21 6 1 5 8 1
                        0 42 6 4 8 0 10 1
                        16 92 4 18 6 0 8 2 1 6
                        2 1 70 9 22 4 1 5 6 0
                        4 8 4 3 0 10 0 6
                        38 39 5 40 8 12 15 0 1 20
                        3 0 40 6 8 0 6 4 4 1
                        5 8 2 8 0 20 0 0
                        38 52 7 20 0 3 4 1 2 4
                        6 1 18 15 38 10 4 8 0 3
                        0 6 1 3 0 3 5 4"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 3418


class HP2(Data):
    def __init__(self):
        self.name_data = "HP2"

        self.weights = """560 1125 620 68 328 47 122 196 41 25
                        115 82 22 631 132 420 86 42 103 215
                        81 91 26 49 316 72 71 49 108 116
                        90 215 58 47 81"""
        
        self.weights = np.array(self.convert_text_to_list(self.weights)).astype(int)

        self.capacities = """163 165 239 168"""
        
        self.capacities = np.array(self.convert_text_to_list(self.capacities)).astype(int)

        self.rest = """40 91 30 3 12 3 18 25 1 1
                        8 1 1 49 8 21 6 1 5 10
                        8 2 1 0 42 6 4 8 0 10
                        1 8 3 2 4
                        16 92 16 4 18 6 0 8 2 1
                        6 2 1 70 9 22 4 1 5 10
                        6 4 0 4 8 4 3 0 10 0
                        6 22 0 2 2
                        38 39 71 5 40 8 12 15 0 1
                        20 3 0 40 6 8 0 6 4 22
                        4 6 1 5 8 2 8 0 20 0
                        0 13 6 1 2
                        38 52 42 7 20 0 3 4 1 2
                        4 6 1 18 15 38 10 4 8 6
                        0 0 3 0 6 1 3 0 3 5
                        4 18 3 4 0"""

        self.rest = np.array(self.convert_text_to_list_of_lists(self.rest,len(self.weights))).astype(int)

        self.optimum = 3186
