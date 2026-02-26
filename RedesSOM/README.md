# Experimentos com Self-Organizing Maps (SOM)

Este projeto realiza experimentos com Redes SOM (Self-Organizing Maps), avaliando:

1. Diferentes taxas de aprendizagem (eta) e vizinhança (sigma)
2. Utilização de diferentes datasets

---

## 🔹 1. Avaliação de Taxa de Aprendizagem (eta) e Vizinhança (sigma)

Foram realizados experimentos variando os hiperparâmetros:

- **eta (learning_rate)** → controla o quanto os pesos são ajustados a cada iteração
- **sigma** → define o raio da vizinhança afetada ao redor do neurônio vencedor (BMU)

### Configurações testadas

| Experimento | eta | sigma |
|------------|------|--------|
| A | 0.1 | 1 |
| B | 0.5 | 3 |
| C | 0.8 | 5 |
| D | 0.05 | 10 |

### Resultados obtidos (Iris Dataset)

Rectangular → QE: 0.3285 | TE: 0.0067  
Hexagonal → QE: 0.3467 | TE: 0.0533  

Experimentos com variação de eta e sigma:

- eta=0.1 | sigma=1 → QE=0.3250 | TE=0.6000  
- eta=0.5 | sigma=3 → QE=0.3467 | TE=0.0533  
- eta=0.8 | sigma=5 → QE=0.4795 | TE=0.0733  
- eta=0.05 | sigma=10 → QE=0.7967 | TE=0.1600  

### Análise

- Valores muito altos de **sigma** tornam o mapa excessivamente suavizado, aumentando o erro de quantização.
- Valores muito altos de **eta** podem gerar instabilidade.
- A melhor configuração observada foi **eta=0.5 e sigma=3**, pois apresentou bom equilíbrio entre QE e TE.
- Sigma muito pequeno pode gerar fragmentação no mapa.
- Sigma muito grande reduz a capacidade de separação dos clusters.

---

## 🔹 2. Teste com Outros Datasets

Além do dataset Iris, foi utilizado o dataset **Wine**, que possui maior dimensionalidade (13 atributos).

### Resultado - Wine Dataset

Wine Dataset → QE: 1.6916 | TE: 0.0337  

### Análise

- O dataset Wine apresentou maior erro de quantização quando comparado ao Iris.
- Isso ocorre devido à maior complexidade e dimensionalidade dos dados.
- Datasets mais complexos exigem mapas maiores ou mais iterações para melhor organização.

---

## 📊 Visualização

Foi utilizada a U-Matrix para visualizar a organização dos neurônios.

- Cores claras indicam maiores distâncias (fronteiras entre clusters).
- Cores escuras indicam regiões internas de cluster.

A visualização confirma a capacidade da SOM em organizar os dados preservando relações topológicas.

---

## 🏁 Conclusão

Os experimentos demonstram que:

- A escolha adequada de eta e sigma é fundamental para o desempenho da SOM.
- Valores intermediários tendem a produzir melhores resultados.
- Datasets com maior dimensionalidade exigem maior capacidade de representação da rede.
- A SOM é eficaz na organização não supervisionada de dados multidimensionais.
