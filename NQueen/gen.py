import numpy as np
import random


class Indevediual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    def mutate(self):
        l = len(self.chromosome)

        x = random.randint(0, l//2)
        y = random.randint((l//2)+1, l-1)
        self.chromosome[x], self.chromosome[y] = self.chromosome[y], self.chromosome[x]
        self.fitness = self.cal_fitness()

    def cal_fitness(self):
        res = 0
        row = len(self.chromosome) - len(np.unique(self.chromosome))
        res += row
        for i in range(len(self.chromosome)):
            for j in range(len(self.chromosome)):
                if i != j:
                    dx = abs(i-j)
                    dy = abs(self.chromosome[i]-self.chromosome[j])

                    if dx == dy:
                        res += 1
        return res

    def draw_chromosome(self):
        length = len(self.chromosome)
        for i in range(length):
            st = ""
            for j in range(length):
                if self.chromosome[j] == i:
                    st += ' * '
                else:
                    st += ' - '
            print(st)

    def get_fitness(self):
        return self.fitness

    def get_chromosome(self):
        return self.chromosome

    def set_chromosome(self,chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
