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