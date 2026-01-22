import numpy as np
import random
import time

class NQueensGA:
    def __init__(self, n=8, pop_size=100, mut_rate=0.1, generations=500):
        self.n = n
        self.pop_size = pop_size
        self.mut_rate = mut_rate
        self.generations = generations
        self.population = [np.random.permutation(n) for _ in range(pop_size)]

    def fitness(self, individual):
        clashes = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if abs(i - j) == abs(individual[i] - individual[j]):
                    clashes += 1
        return clashes

    def crossover(self, p1, p2):
        point = random.randint(1, self.n - 1)
        child1 = np.concatenate([p1[:point], p2[point:]])
        child2 = np.concatenate([p2[:point], p1[point:]])
        return child1, child2

    def mutate(self, individual):
        if random.random() < self.mut_rate:
            i, j = random.sample(range(self.n), 2)
            individual[i], individual[j] = individual[j], individual[i]
        return individual

    def solve(self):
        start_time = time.time()
        for gen in range(self.generations):
            self.population = sorted(self.population, key=self.fitness)
            current_best = self.population[0]
            best_fit = self.fitness(current_best)

            if best_fit == 0:
                return current_best, gen, time.time() - start_time

            new_gen = self.population[:int(self.pop_size * 0.1)]
            
            while len(new_gen) < self.pop_size:
                p1, p2 = random.sample(self.population[:50], 2)
                c1, c2 = self.crossover(p1, p2)
                new_gen.extend([self.mutate(c1), self.mutate(c2)])
            
            self.population = new_gen[:self.pop_size]

        return self.population[0], self.generations, time.time() - start_time

n_rainhas = 8
ag = NQueensGA(n=n_rainhas, pop_size=100, mut_rate=0.2)
solucao, geracoes, tempo = ag.solve()

print(f"--- Resultado para {n_rainhas} Rainhas ---")
print(f"Melhor Configuração: {solucao}")
print(f"Conflitos Finais: {ag.fitness(solucao)}")
print(f"Gerações decorridas: {geracoes}")
print(f"Tempo de execução: {tempo:.4f}s")