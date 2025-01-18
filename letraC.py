def calcular_faturamento(faturamento_diario):
    # Verifica se a lista está vazia
    if not faturamento_diario:
        return None, None, 0

    # Calcula o menor e o maior valor de faturamento
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)

    # Calcula a média mensal
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)

    # Conta os dias com faturamento acima da média
    dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_media

# Exemplo de uso
faturamento_diario = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
menor, maior, dias_acima_media = calcular_faturamento(faturamento_diario)

print(f'Menor faturamento: R$ {menor}')
print(f'Maior faturamento: R$ {maior}')
print(f'Dias com faturamento acima da média: {dias_acima_media}')