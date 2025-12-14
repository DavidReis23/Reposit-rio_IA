import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from decimal import Decimal
import locale
import warnings
warnings.filterwarnings("ignore")

# --- Variáveis fuzzy ---
tamanho = ctrl.Antecedent(np.arange(20, 351, 1), 'tamanho')      # m²
qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')   # 0 a 10
valor = ctrl.Consequent(np.arange(50, 1001, 1), 'valor')        # em milhares

# --- Funções de pertinência ---
qualidade['baixa'] = fuzz.trapmf(qualidade.universe, [0, 0, 2.5, 5])
qualidade['media'] = fuzz.trimf(qualidade.universe, [2.5, 5, 7.5])
qualidade['alta']  = fuzz.trapmf(qualidade.universe, [5, 7.5, 10, 10])

tamanho['kitnet']  = fuzz.trapmf(tamanho.universe, [20, 20, 35, 45])
tamanho['pequeno'] = fuzz.trapmf(tamanho.universe, [35, 45, 75, 85])
tamanho['medio']   = fuzz.trapmf(tamanho.universe, [75, 85, 140, 150])
tamanho['grande']  = fuzz.trapmf(tamanho.universe, [140, 150, 350, 350])

valor['baixo']      = fuzz.trapmf(valor.universe, [50, 50, 105, 125])
valor['medio_baixo']= fuzz.trapmf(valor.universe, [105, 125, 180, 200])
valor['medio']      = fuzz.trapmf(valor.universe, [180, 200, 350, 380])
valor['alto']       = fuzz.trapmf(valor.universe, [350, 380, 700, 800])
valor['muito_alto'] = fuzz.trapmf(valor.universe, [700, 800, 1000, 1000])

# --- Regras ---
regras = [
    ctrl.Rule(tamanho['kitnet'] & qualidade['baixa'], valor['baixo']),
    ctrl.Rule(tamanho['kitnet'] & qualidade['media'], valor['medio_baixo']),
    ctrl.Rule(tamanho['kitnet'] & qualidade['alta'],  valor['medio']),

    ctrl.Rule(tamanho['pequeno'] & qualidade['baixa'], valor['medio_baixo']),
    ctrl.Rule(tamanho['pequeno'] & qualidade['media'], valor['medio']),
    ctrl.Rule(tamanho['pequeno'] & qualidade['alta'],  valor['alto']),

    ctrl.Rule(tamanho['medio'] & qualidade['baixa'], valor['medio']),
    ctrl.Rule(tamanho['medio'] & qualidade['media'], valor['alto']),
    ctrl.Rule(tamanho['medio'] & qualidade['alta'],  valor['muito_alto']),

    ctrl.Rule(tamanho['grande'] & qualidade['baixa'], valor['alto']),
    ctrl.Rule(tamanho['grande'] & qualidade['media'], valor['muito_alto']),
    ctrl.Rule(tamanho['grande'] & qualidade['alta'],  valor['muito_alto']),
]

sistema = ctrl.ControlSystem(regras)
sim = ctrl.ControlSystemSimulation(sistema)

# --- Entrada ---
t = float(input("Informe o tamanho do imóvel (20-350 m²): "))
q = float(input("Informe a qualidade (0-10): "))

sim.input['tamanho'] = max(20, min(350, t))
sim.input['qualidade'] = max(0, min(10, q))

sim.compute()

if 'valor' not in sim.output:
    print("Não foi possível estimar o valor para essa combinação.")
    exit()

valor_k = sim.output['valor']
valor_total = Decimal(valor_k * 1000).quantize(Decimal('0.01'))
aluguel = (valor_total * Decimal('0.004')).quantize(Decimal('0.01'))

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

print("\n--- RESULTADO ---")
print(f"Valor estimado: {locale.currency(valor_total, grouping=True)}")
print(f"Aluguel estimado (~0,4%): {locale.currency(aluguel, grouping=True)}")

valor.view(sim=sim)
plt.tight_layout()
plt.savefig("imovel_fuzzy.png", dpi=150)
print("Gráfico salvo: imovel_fuzzy.png")
