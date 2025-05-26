from scipy.stats import wilcoxon

def receber_amostra(nome):
    print(f"Digite os valores da amostra {nome}, um por linha. Quando terminar, pressione ENTER duas vezes:")
    dados = []
    while True:
        try:
            linha = input()
            if linha == '':
                break
            dados.append(int(linha.strip()))
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
    return dados

# Receber amostras
amostra_A = receber_amostra('A')
amostra_B = receber_amostra('B')

# Mostrar as amostras formatadas
print(f"\nAmostra A formatada: {amostra_A}")
print(f"Amostra B formatada: {amostra_B}")

# Teste de Wilcoxon
estatistica, p_valor = wilcoxon(amostra_A, amostra_B)

# Mostrar resultados
print(f"\nResultado do Teste de Wilcoxon:")
print(f"Estatística: {estatistica}")
print(f"Valor-p: {p_valor}")

# Interpretação
if p_valor < 0.05:
    print("Diferença estatisticamente significativa.")
else:
    print("Diferença NÃO estatisticamente significativa.")
