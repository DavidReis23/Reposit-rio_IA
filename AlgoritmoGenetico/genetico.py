import numpy as np
import matplotlib.pyplot as plt

# --- PARÂMETROS GERAIS ---
POP_SIZE = 100
CHROM_LENGTH = 16
GENERATIONS = 50
MIN_X, MAX_X = -10, 10
RUNS = 5

# --- FUNÇÕES BASE ---
def decode(individual):
    # Converte binário para decimal e mapeia para [-10, 10]
    decimal = int("".join(str(b) for b in individual), 2)
    return MIN_X + decimal * (MAX_X - MIN_X) / ((2**CHROM_LENGTH) - 1)

def fitness_function(individual):
    x = decode(individual)
    return 2 * (x**2) + 5 * x

def hamming_distance(pop):
    # Calcula a distância média de Hamming da população
    dist = 0
    comparisons = 0
    for i in range(len(pop)):
        for j in range(i + 1, len(pop)):
            dist += np.sum(pop[i] != pop[j])
            comparisons += 1
    return dist / comparisons if comparisons > 0 else 0

def tournament_selection(pop, fitnesses, k=3):
    selected_indices = np.random.choice(len(pop), k, replace=False)
    best_idx = selected_indices[np.argmin(fitnesses[selected_indices])]
    return pop[best_idx].copy()

def crossover(p1, p2):
    if np.random.rand() < 0.8: # 80% de chance de crossover
        pt = np.random.randint(1, CHROM_LENGTH - 1)
        c1 = np.concatenate([p1[:pt], p2[pt:]])
        c2 = np.concatenate([p2[:pt], p1[pt:]])
        return c1, c2
    return p1.copy(), p2.copy()

def mutate(ind, mut_rate):
    for i in range(CHROM_LENGTH):
        if np.random.rand() < mut_rate:
            ind[i] = 1 - ind[i]
    return ind

# --- ALGORITMO GENÉTICO ---
def run_ga(elitism_pct, mut_rate_base, adaptive=False):
    pop = [np.random.randint(2, size=CHROM_LENGTH) for _ in range(POP_SIZE)]
    elite_count = int(POP_SIZE * (elitism_pct / 100))
    
    history_best = []
    history_avg = []
    history_div = []

    for gen in range(GENERATIONS):
        fitnesses = np.array([fitness_function(ind) for ind in pop])
        
        # Registros
        history_best.append(np.min(fitnesses))
        history_avg.append(np.mean(fitnesses))
        div = hamming_distance(pop)
        history_div.append(div)
        
        # Mutação Adaptativa (Mitigação)
        current_mut_rate = mut_rate_base
        if adaptive and div < (CHROM_LENGTH * 0.2): 
            current_mut_rate = mut_rate_base * 5 
            
        # Elitismo
        next_pop = []
        if elite_count > 0:
            elite_indices = np.argsort(fitnesses)[:elite_count]
            next_pop = [pop[i].copy() for i in elite_indices]
            
        # Reprodução
        while len(next_pop) < POP_SIZE:
            p1 = tournament_selection(pop, fitnesses)
            p2 = tournament_selection(pop, fitnesses)
            c1, c2 = crossover(p1, p2)
            next_pop.append(mutate(c1, current_mut_rate))
            if len(next_pop) < POP_SIZE:
                next_pop.append(mutate(c2, current_mut_rate))
                
        pop = next_pop

    return history_best, history_avg, history_div

# --- EXPERIMENTOS ---
configs = {
    'A (0% Elitismo)': {'elite': 0, 'mut': 0.01, 'adapt': False},
    'B (2% Elitismo)': {'elite': 2, 'mut': 0.01, 'adapt': False},
    'C (20% Elitismo)': {'elite': 20, 'mut': 0.01, 'adapt': False},
    'C_Mitigado (20% Elite + Adaptativo)': {'elite': 20, 'mut': 0.01, 'adapt': True}
}

results = {key: {'best': [], 'avg': [], 'div': []} for key in configs}

print("Executando experimentos...")
for name, conf in configs.items():
    for _ in range(RUNS):
        b, a, d = run_ga(conf['elite'], conf['mut'], conf['adapt'])
        results[name]['best'].append(b)
        results[name]['avg'].append(a)
        results[name]['div'].append(d)
        
    results[name]['best'] = np.mean(results[name]['best'], axis=0)
    results[name]['avg'] = np.mean(results[name]['avg'], axis=0)
    results[name]['div'] = np.mean(results[name]['div'], axis=0)

# --- PLOTAGEM DOS GRÁFICOS ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

for name in configs:
    ax1.plot(results[name]['best'], label=name)
    ax2.plot(results[name]['div'], label=name)

ax1.set_title("Evolução do Melhor Fitness Médio")
ax1.set_xlabel("Gerações")
ax1.set_ylabel("Fitness (menor é melhor)")
ax1.legend()

ax2.set_title("Evolução da Diversidade (Distância de Hamming)")
ax2.set_xlabel("Gerações")
ax2.set_ylabel("Distância Média")
ax2.legend()

plt.savefig("graficos_experimentos_ag.png", dpi=300, bbox_inches='tight')

plt.show()