import pandas as pd

# Função de Ativação (Degrau Bipolar)
def funcao_ativacao(y_in):
    return 1 if y_in >= 0 else -1

# Regra de Hebb (Treinamento)
def treinar_hebb(entradas, targets):
    pesos = [0, 0, 0]
    bias = 0
    
    # Passa por todas as linhas da tabela (Batch)
    for i in range(len(entradas)):
        x = entradas[i]
        t = targets[i]
        
        # Atualiza pesos: w_novo = w_atual + (x * target)
        # Como o peso inicial é 0, basta somar x*t
        pesos[0] += x[0] * t
        pesos[1] += x[1] * t
        pesos[2] += x[2] * t
        
        # Atualiza bias: b_novo = b_atual + target
        bias += t
        
    return pesos, bias

# Função para testar e exibir a tabela
def testar_rede(nome_caso, entradas, targets, pesos, bias):
    print(f"\n--- {nome_caso} ---")
    print(f"Pesos Finais: {pesos} | Bias Final: {bias}")
    print(f"{'A':^3} {'B':^3} {'C':^3} | {'Target':^6} | {'Soma (yin)':^10} | {'Saída (y)':^9} | {'Status':^8}")
    print("-" * 65)
    
    erros = 0
    for i in range(len(entradas)):
        x = entradas[i]
        t = targets[i]
        
        # Cálculo da saída: yin = bias + somatorio(xi * wi)
        y_in = bias + (x[0] * pesos[0]) + (x[1] * pesos[1]) + (x[2] * pesos[2])
        
        # Aplica função degrau
        y_calculado = funcao_ativacao(y_in)
        
        # Verifica se acertou
        status = "OK" if y_calculado == t else "ERRO"
        if status == "ERRO": erros += 1
        
        print(f"{x[0]:^3} {x[1]:^3} {x[2]:^3} | {t:^6} | {y_in:^10} | {y_calculado:^9} | {status:^8}")
    print("-" * 65)

# --- DADOS ---

# Tabela Verdade (Entradas A, B, C)
X = [
    [-1, -1, -1],
    [-1, -1,  1],
    [-1,  1, -1],
    [-1,  1,  1],
    [ 1, -1, -1],
    [ 1, -1,  1],
    [ 1,  1, -1],
    [ 1,  1,  1]
]

# Definindo os Targets para cada caso

# Caso 1: Y1 = A AND B AND C (Só é 1 se todos forem 1)
targets_Y1 = [-1, -1, -1, -1, -1, -1, -1, 1]

# Caso 2: Y2 = A OR B OR C (Só é -1 se todos forem -1)
targets_Y2 = [-1, 1, 1, 1, 1, 1, 1, 1]

# Caso 3: Y3 = (NOT(A AND B)) OR C
# Lógica: A.B é 1 apenas em (1,1). Logo NOT(A.B) é -1 apenas em (1,1).
# Resultado final é OR com C.
# Único caso -1 é quando (NOT(AB) é -1) E (C é -1) -> Entrada (1, 1, -1)
targets_Y3 = [1, 1, 1, 1, 1, 1, -1, 1]

# --- EXECUÇÃO ---

# 1. Executar Y1
w1, b1 = treinar_hebb(X, targets_Y1)
testar_rede("Caso 1: Y1 = ABC (AND)", X, targets_Y1, w1, b1)

# 2. Executar Y2
w2, b2 = treinar_hebb(X, targets_Y2)
testar_rede("Caso 2: Y2 = A+B+C (OR)", X, targets_Y2, w2, b2)

# 3. Executar Y3
w3, b3 = treinar_hebb(X, targets_Y3)
testar_rede("Caso 3: Y3 = Not(AB) + C", X, targets_Y3, w3, b3)