from random import shuffle, randint, random

def euc_dis(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def get_list_dis(i1, i2):

    driving_dis = [[2297, 773, 2188, 1674, 3129, 3837, 4055, 4265, 4625, 3846, 4317, 4362, 5099, 6668, 6497, 6381, 6163, 5908, 5706, 5450, 4932, 5024, 4670, 4847, 5595, 5147], [3059, 4474, 3960, 3044, 3362, 2522, 2505, 1774, 539, 1116, 1450, 2112, 2619, 2771, 2564, 2563, 2595, 2670, 3635, 
3217, 3668, 3467, 3847, 4581, 4133], [1415, 901, 2356, 3064, 3282, 3492, 3852, 3073, 3544, 3589, 4326, 5895, 5724, 5608, 5390, 5135, 4933, 4677, 4159, 4251, 3897, 4074, 4822, 4374], [515, 1969, 2677, 2896, 3105, 3465, 3088, 4242, 4160, 4743, 5508, 5337, 5221, 5003, 4748, 
4546, 4290, 3772, 3864, 3511, 3687, 4435, 3988], [1457, 2164, 2383, 2593, 2952, 2575, 3729, 3647, 4230, 4995, 4824, 4708, 4490, 4235, 4033, 3777, 3259, 3351, 2998, 3174, 3922, 3475], [713, 932, 1142, 1501, 2512, 2749, 2555, 3253, 3544, 3374, 3257, 3039, 2784, 2582, 2326, 
1808, 1900, 1547, 1723, 2471, 2024], [841, 1051, 1661, 2824, 2858, 2715, 3162, 3883, 3713, 3597, 3378, 3123, 2922, 1919, 1553, 1378, 981, 1023, 1771, 1323], [210, 821, 1984, 2018, 1875, 2321, 2613, 2442, 2326, 2108, 1853, 1651, 1395, 877, 1316, 952, 1331, 2065, 1618], [806, 1969, 2002, 1689, 2119, 2410, 2240, 2124, 1905, 1650, 1448, 1249, 731, 1182, 1011, 1391, 2124, 1677], [1237, 1270, 1127, 1711, 2399, 
2229, 2113, 1894, 1639, 1437, 2035, 1517, 1967, 1767, 2146, 2880, 2433], [579, 912, 1574, 2081, 2233, 2026, 2025, 2057, 2132, 3097, 2679, 3130, 2929, 3309, 4043, 3595], [439, 902, 1408, 1561, 1666, 1552, 1584, 1659, 2624, 2715, 3074, 2965, 3345, 4078, 3631], [593, 1101, 1165, 1128, 1127, 1159, 1233, 2199, 2371, 2649, 2665, 3045, 3779, 3331], [515, 668, 773, 1021, 1130, 1205, 2170, 2343, 2620, 2987, 3396, 
4129, 3682], [182, 286, 535, 793, 1096, 2129, 2333, 2611, 2977, 3386, 4120, 3672], [117, 366, 624, 927, 1960, 2164, 2442, 2808, 3217, 3951, 3503], [251, 510, 812, 1845, 2050, 2327, 2694, 3103, 3836, 3389], [291, 593, 1626, 1831, 2108, 2475, 2884, 3617, 3170], [338, 1371, 
1575, 1853, 2220, 2628, 3362, 2915], [1056, 1373, 1650, 2017, 2426, 3159, 2712], [521, 564, 945, 1354, 2087, 1640], [459, 589, 984, 1717, 1270], [405, 814, 1547, 1100], [404, 1137, 690], [751, 304], [467], []]

    straight_dis = [[1118, 654, 1627, 1335, 2109, 2676, 2505, 2506, 2002, 1441, 1923, 2177, 2572, 2991, 3078, 3108, 3094, 3034, 3024, 3400, 3122, 3419, 3307, 3378, 3799, 3626], [1047, 2163, 1724, 1822, 2316, 1868, 1795, 1188, 330, 806, 1079, 1453, 1874, 1967, 2002, 2005, 1972, 2008, 2545, 2349, 2681, 2668, 2842, 3351, 3084], [1162, 771, 1460, 2027, 1915, 1941, 1518, 1288, 1744, 1920, 2381, 2762, 2819, 2828, 2775, 2676, 2615, 2869, 2560, 2837, 2697, 2745, 3151, 2991], [454, 1414, 1831, 2135, 2252, 2131, 2338, 2729, 2812, 3304, 3619, 3636, 3618, 3514, 3361, 3219, 3159, 2786, 2957, 2705, 2604, 2824, 2811], [1134, 1636, 1, 1902, 1710, 1887, 2275, 2363, 2854, 3176, 3199, 3184, 3089, 2944, 2816, 
2834, 2473, 2681, 2462, 2413, 2714, 2640], [567, 736, 877, 1024, 1779, 1945, 1866, 2328, 2524, 2495, 2449, 2306, 2119, 1926, 1747, 1372, 1552, 1328, 1307, 1690, 1546], [705, 882, 1318, 2220, 2292, 2142, 2551, 2657, 2595, 2531, 2361, 2153, 1918, 1492, 1117, 1181, 891, 779, 1123, 1003], [178, 716, 1695, 1666, 1474, 1857, 1952, 1892, 1831, 1665, 1462, 1240, 1028, 669, 922, 814, 976, 1504, 1216], [613, 1597, 
1528, 1319, 1687, 1774, 1714, 1653, 1488, 1286, 1068, 943, 618, 916, 873, 1083, 1624, 1312], [984, 974, 845, 1304, 1529, 1522, 1494, 1383, 1233, 1120, 1404, 1168, 1495, 1486, 1688, 2221, 1923], [483, 748, 1134, 1549, 1638, 1672, 1675, 1646, 1693, 2275, 2111, 2448, 2467, 2671, 3198, 2907], [325, 651, 1068, 1163, 1204, 1227, 1231, 1327, 2021, 1933, 2270, 2353, 2605, 3150, 2824], [493, 841, 907, 930, 926, 911, 1001, 1716, 1657, 1990, 2100, 2372, 2920, 2579], [433, 557, 624, 720, 822, 1025, 1851, 1892, 2200, 2371, 2673, 3218, 2857], [155, 252, 424, 611, 870, 1703, 1831, 2102, 2324, 2648, 3176, 2802], [99, 287, 490, 754, 1575, 1724, 1983, 2217, 2546, 3067, 2691], [192, 403, 666, 1480, 1638, 1892, 2131, 2461, 2979, 2602], [214, 475, 1288, 1448, 1699, 1940, 2271, 2787, 2410], [263, 1091, 1235, 1493, 1728, 2058, 
2576, 2200], [840, 972, 1232, 1464, 1795, 2313, 1937], [381, 441, 747, 1081, 1540, 1163], [338, 493, 823, 1345, 972], [329, 648, 1101, 723], [337, 852, 485], [548, 248], [378], []]
    
    if i1 > i2:
        i1, i2 = i2, i1
    i2 -= 1
    dis = straight_dis[i1][i2-i1]
    return dis


class Individual:
    def __init__(self, genome_length):
        self.geno_len = genome_length
        self.genome = [n for n in range(genome_length)]
        shuffle(self.genome)
        self.fit = 0
        self.total_dis = 0

    def get_fit(self, points):
        total_dis = 0 
        for i in range(len(points)):
            p1 = self.genome[i]
            p2 = self.genome[i-1]
            total_dis += get_list_dis(p1, p2)
        self.total_dis = total_dis
        fit = 1/total_dis*10000000
        self.fit = fit
        return fit

class Population:
    def __init__(self, n_ind, genome_length):
        self.n_ind = n_ind
        self.individuals = [Individual(genome_length) for _ in range(n_ind)]
        self.mean_fit = 0

    def fit_pop(self, pts):
        # get mean fit of population
        for ind in self.individuals:
            self.mean_fit += ind.get_fit(pts)
        self.mean_fit /= self.n_ind

        # sorting the population by fitness
        changed = True
        while changed:
            changed = False
            for c in range(1, self.n_ind):
                if self.individuals[c].fit > self.individuals[c-1].fit:
                    self.individuals[c], self.individuals[c-1] = self.individuals[c-1], self.individuals[c]
                    changed = True

    def new_population(self, elite_tax=0.15):
        def crossover(fathers):
            son = Individual(fathers[0].geno_len)
            cut_num = randint(0, fathers[0].geno_len)

            new_genome00 = fathers[0].genome[0:cut_num]
            new_genome01 = fathers[0].genome[cut_num:fathers[0].geno_len]
            new_genome11 = fathers[1].genome[cut_num:fathers[0].geno_len]

            repeated_index = []
            for c in range(len(new_genome11)):
                if new_genome11[c] in new_genome00:
                    repeated_index.append(c)

            non_repeated = []
            for c in range(len(new_genome01)):
                if new_genome01[c] not in new_genome11:
                    non_repeated.append(new_genome01[c])
                        
            for c in range(len(repeated_index)):
                new_genome11[repeated_index[c]] = non_repeated[c]

            son_genome = new_genome00 + new_genome11
            son.genome = son_genome

            return son

        def mutation(ind, mut_tax=0.7):
            mut = random()
            if mut <= mut_tax:
                s_genes = [randint(0, ind.geno_len-1) for _ in range(randint(2, 10))]
                for c in range(1, len(s_genes)):
                    ind.genome[s_genes[c]], ind.genome[s_genes[c-1]] = ind.genome[s_genes[c-1]], ind.genome[s_genes[c]]
        
        def choose_father():
            ag_fit = 0
            ag_fit_list = []
            for ind in self.individuals:
                ag_fit += ind.fit
                ag_fit_list.append(ag_fit)
            self.mean_fit = ag_fit/self.n_ind
            
            chosen_num = randint(0, int(ag_fit))
            for c in range(self.n_ind-1):
                if ag_fit_list[c] < chosen_num < ag_fit_list[c+1]:
                    return self.individuals[c]
            return self.individuals[0]


        elite_num = int(len(self.individuals)*elite_tax)
        new_inds = [] +self.individuals[:elite_num]
        for _ in range(self.n_ind-elite_num):
            father01, father02 = choose_father(), choose_father()
            son = crossover([father01, father02])
            mutation(son)
            new_inds.append(son)

        self.individuals = new_inds

        
if __name__ == '__main__':
    for c in range(10):
        cut_num = 5
        new_genome0 = [n for n in range(10)]
        shuffle(new_genome0)
        new_genome1 = [n for n in range(10)]
        shuffle(new_genome0)

        new_genome00 = new_genome0[0:cut_num]
        new_genome01 = new_genome0[cut_num:10]
        new_genome11 = new_genome1[cut_num:10]

        repeated_index = []
        for c in range(len(new_genome11)):
            if new_genome11[c] in new_genome00:
                repeated_index.append(c)

        non_repeated = []
        for c in range(len(new_genome01)):
            if new_genome01[c] not in new_genome11:
                non_repeated.append(new_genome01[c])
                    
        for c in range(len(repeated_index)):
            new_genome11[repeated_index[c]] = non_repeated[c]

        son_genome = new_genome00 + new_genome11

        # print(cut_num)
        # print(new_genome0)
        # print(son_genome)
        # print(new_genome1)
        