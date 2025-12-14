import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import warnings
warnings.filterwarnings("ignore")

# Universos
x_dinheiro = np.arange(0, 101, 1)
x_pessoas = np.arange(0, 101, 1)
x_risco = np.arange(0, 101, 1)

# Funções de pertinência
din_inadequado = fuzz.trapmf(x_dinheiro, [0, 0, 30, 50])
din_medio      = fuzz.trimf(x_dinheiro, [30, 50, 70])
din_adequado   = fuzz.trapmf(x_dinheiro, [50, 70, 100, 100])

pess_pequeno = fuzz.trapmf(x_pessoas, [0, 0, 40, 60])
pess_alto    = fuzz.trapmf(x_pessoas, [40, 60, 100, 100])

risco_pequeno = fuzz.trapmf(x_risco, [0, 0, 30, 50])
risco_normal  = fuzz.trimf(x_risco, [30, 50, 70])
risco_alto    = fuzz.trapmf(x_risco, [50, 70, 100, 100])

# Variáveis fuzzy
dinheiro = ctrl.Antecedent(x_dinheiro, 'dinheiro')
pessoas  = ctrl.Antecedent(x_pessoas, 'pessoas')
risco    = ctrl.Consequent(x_risco, 'risco')

dinheiro['inadequado'] = din_inadequado
dinheiro['medio'] = din_medio
dinheiro['adequado'] = din_adequado

pessoas['pequeno'] = pess_pequeno
pessoas['alto'] = pess_alto

risco['pequeno'] = risco_pequeno
risco['normal'] = risco_normal
risco['alto'] = risco_alto

# Regras
r1 = ctrl.Rule(dinheiro['adequado'] | pessoas['pequeno'], risco['pequeno'])
r2 = ctrl.Rule(dinheiro['medio'] & pessoas['alto'], risco['normal'])
r3 = ctrl.Rule(dinheiro['inadequado'], risco['alto'])

sistema = ctrl.ControlSystem([r1, r2, r3])
sim = ctrl.ControlSystemSimulation(sistema)

# Entrada
d = float(input("Nível de dinheiro (0-100): "))
p = float(input("Quantidade de pessoas (0-100): "))

sim.input['dinheiro'] = max(0, min(100, d))
sim.input['pessoas'] = max(0, min(100, p))

sim.compute()

print("\n--- RESULTADO ---")
print(f"Risco do projeto: {sim.output['risco']:.2f}")

if sim.output['risco'] < 33:
    print("Classificação: RISCO PEQUENO")
elif sim.output['risco'] < 66:
    print("Classificação: RISCO NORMAL")
else:
    print("Classificação: RISCO ALTO")

risco.view(sim=sim)
plt.tight_layout()
plt.savefig("risco_fuzzy.png", dpi=150)
print("Gráfico salvo: risco_fuzzy.png")
