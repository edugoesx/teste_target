# Dados de faturamento por estado
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

def calcular_percentuais(faturamento):
    # Calcula o valor total de faturamento
    total_faturamento = sum(faturamento.values())
    
    # Calcula o percentual de cada estado
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}
    
    return total_faturamento, percentuais

# Calcula os percentuais
total, percentuais = calcular_percentuais(faturamento_por_estado)

# Exibe os resultados
print(f"Valor total de faturamento: R$ {total:.2f}\n")
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")