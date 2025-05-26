from scipy.stats import wilcoxon

def get_sample(name):
    print(f"Digite os valores da amostra {name}, um por linha. Quando terminar, pressione ENTER duas vezes:")
    data = []
    while True:
        try:
            row = input()
            if row == '':
                break
            data.append(int(row.strip()))
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
    return data

# Receber amostras
sample_A = get_sample('A')
sample_B = get_sample('B')

# Mostrar as amostras formatadas
print(f"\nAmostra A formatada: {sample_A}")
print(f"Amostra B formatada: {sample_B}")

# Teste de Wilcoxon
statistic, p_value = wilcoxon(sample_A, sample_B)

# Mostrar resultados
print(f"\nResultado do Teste de Wilcoxon:")
print(f"Estatística: {statistic}")
print(f"Valor-p: {p_value}")

# Interpretação
if p_value < 0.05:
    print("Diferença estatisticamente significativa.")
else:
    print("Diferença NÃO estatisticamente significativa.")
