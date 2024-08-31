def calcular_percentuais(faturamento):
    # Calcula o total de faturamento
    total_faturamento = sum(faturamento.values())
    
    # Calcula o percentual de cada estado em relação ao total
    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor / total_faturamento) * 100
        percentuais[estado] = percentual
    
    return percentuais, total_faturamento


# Dados de faturamento mensal por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
    
# Calcula os percentuais e o total de faturamento
percentuais, total_faturamento = calcular_percentuais(faturamento)

# Exibe o total de faturamento
print(f"Total de faturamento: R${total_faturamento:.2f}")

# Exibe o percentual de cada estado
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
