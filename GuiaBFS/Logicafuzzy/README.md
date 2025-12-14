# Projeto — Lógica Fuzzy (Avaliação de Imóvel e Risco de Projeto)

Este repositório contém duas aplicações desenvolvidas em **Python** utilizando **Lógica Fuzzy (Mamdani)** com a biblioteca **scikit-fuzzy**. O objetivo é demonstrar, de forma prática e didática, a modelagem de problemas do mundo real por meio de variáveis linguísticas, funções de pertinência, base de regras e defuzzificação.

Os sistemas implementados são:

* 🏠 **Avaliação Fuzzy de Valor de Imóvel**
* ⚠️ **Avaliador Fuzzy de Risco de Projeto**

---

## 📦 Tecnologias Utilizadas

* Python 3.11+
* NumPy
* Matplotlib
* SciPy
* NetworkX
* Scikit-Fuzzy

---

## 🔧 Instalação das Dependências

Antes de executar os códigos, instale as bibliotecas necessárias:

```bash
pip install numpy matplotlib scipy networkx scikit-fuzzy
```

---

## 🏠 Sistema 1 — Avaliação Fuzzy de Valor de Imóvel

### 📌 Descrição

Este sistema estima o **valor de um imóvel** e o **aluguel aproximado** com base em duas variáveis de entrada:

* **Tamanho do imóvel (m²)**: 20 a 350
* **Qualidade do imóvel**: escala de 0 a 10

A saída do sistema é:

* **Valor estimado do imóvel (em milhares)**
* **Aluguel estimado (~0,4% do valor)**

### 🔍 Variáveis Fuzzy

**Entradas (Antecedents):**

* Tamanho: kitnet, pequeno, médio, grande
* Qualidade: baixa, média, alta

**Saída (Consequent):**

* Valor: baixo, médio-baixo, médio, alto, muito alto

### 📐 Método Utilizado

* Inferência fuzzy do tipo **Mamdani**
* Operadores lógicos: AND (mínimo)
* Defuzzificação: **Centroide**

### ▶️ Execução

```bash
python imovelfuzzy.py
```

Ao executar, o sistema solicitará os valores de entrada e gerará o arquivo:

* `imovel_fuzzy.png`

---

## ⚠️ Sistema 2 — Avaliador Fuzzy de Risco de Projeto

### 📌 Descrição

Este sistema avalia o **nível de risco de um projeto**, considerando:

* **Nível de adequação financeira (0–100)**
* **Quantidade relativa de pessoas envolvidas (0–100)**

A saída é um valor numérico de risco e sua classificação qualitativa:

* Risco Pequeno
* Risco Normal
* Risco Alto

### 🔍 Variáveis Fuzzy

**Entradas (Antecedents):**

* Dinheiro: inadequado, médio, adequado
* Pessoas: pequeno, alto

**Saída (Consequent):**

* Risco: pequeno, normal, alto

### 📐 Método Utilizado

* Inferência fuzzy do tipo **Mamdani**
* Operadores lógicos: AND (mínimo) e OR (máximo)
* Defuzzificação: **Centroide**

### ▶️ Execução

```bash
python risco.py
```

O sistema gera o arquivo:

* `risco_fuzzy.png`

---

## 📊 Visualizações

Os gráficos gerados apresentam:

* Funções de pertinência das variáveis
* Área agregada das regras ativadas
* Linha vertical indicando o valor final (crisp)

Essas visualizações auxiliam na interpretação e validação dos resultados fuzzy.

---

## 🎓 Objetivo Acadêmico

Este projeto foi desenvolvido com fins **didáticos**, para a disciplina de **Inteligência Artificial**, demonstrando a aplicação prática da lógica fuzzy em problemas reais, conforme os conceitos de:

* Fuzzificação
* Base de regras
* Inferência fuzzy
* Defuzzificação

---

## ✅ Conclusão

Os sistemas apresentados demonstram que a lógica fuzzy é uma abordagem eficiente para lidar com incertezas e variáveis subjetivas, fornecendo resultados coerentes e interpretáveis para problemas complexos do cotidiano.

---

📌 **Autor:** David da Silva dos Reis
📚 **Curso:** Sistemas de Informação / ADS
📅 **Disciplina:** Inteligência Artificial