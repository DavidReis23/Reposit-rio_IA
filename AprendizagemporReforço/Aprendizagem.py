import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, confusion_matrix

# =========================
# Parâmetros
# =========================
alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 1000
runs = 30

# =========================
# Carregar dados
# =========================
iris = load_iris()
X = iris.data
y = iris.target

# Normalização
scaler = MinMaxScaler()
X = scaler.fit_transform(X)

# =========================
# Discretização
# =========================
def discretize(state):
    return tuple((state * 10).astype(int))

# =========================
# Treinamento Q-learning
# =========================
def train_q_learning(X_train, y_train):
    Q = {}
    rewards_per_episode = []

    for _ in range(episodes):
        total_reward = 0

        for state, label in zip(X_train, y_train):
            s = discretize(state)

            if s not in Q:
                Q[s] = np.zeros(3)

            # ε-greedy
            if np.random.rand() < epsilon:
                action = np.random.randint(3)
            else:
                action = np.argmax(Q[s])

            reward = 1 if action == label else -1
            total_reward += reward

            Q[s][action] += alpha * (
                reward + gamma * np.max(Q[s]) - Q[s][action]
            )

        rewards_per_episode.append(total_reward)

    return Q, rewards_per_episode

# =========================
# Teste
# =========================
def test_model(Q, X_test):
    predictions = []

    for state in X_test:
        s = discretize(state)

        if s in Q:
            action = np.argmax(Q[s])
        else:
            action = np.random.randint(3)

        predictions.append(action)

    return predictions

# =========================
# Execuções
# =========================
accuracies = []
all_rewards = []

for run in range(runs):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3
    )

    Q, rewards = train_q_learning(X_train, y_train)
    all_rewards.append(rewards)

    y_pred = test_model(Q, X_test)

    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)

# =========================
# Resultados
# =========================
print("Acurácia média:", np.mean(accuracies))
print("Desvio padrão:", np.std(accuracies))

print("\nMatriz de confusão (última rodada):")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# =========================
# GRÁFICOS
# =========================

# Média das recompensas
mean_rewards = np.mean(all_rewards, axis=0)

plt.figure(figsize=(15, 4))

# 1. Curva de aprendizado
plt.subplot(1, 3, 1)
plt.plot(mean_rewards)
plt.title("Curva de Aprendizado")
plt.xlabel("Episódios")
plt.ylabel("Recompensa")

# 2. Histograma de acurácia
plt.subplot(1, 3, 2)
plt.hist(accuracies)
plt.title("Distribuição de Acurácia")
plt.xlabel("Acurácia")
plt.ylabel("Frequência")

# 3. Matriz de confusão
plt.subplot(1, 3, 3)
plt.imshow(cm)
plt.title("Matriz de Confusão")
plt.xlabel("Predito")
plt.ylabel("Real")

# Adiciona números dentro da matriz
for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, cm[i][j], ha='center', va='center')

plt.tight_layout()
plt.savefig("graficos.png")

print("\nGráfico salvo como graficos.png")