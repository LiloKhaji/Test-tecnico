import json

def processar_faturamento(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    
    faturamento_diario = dados

    
    # Filtra valores não zero
    valores = [item['valor'] for item in faturamento_diario if item['valor'] > 0]
    
    if not valores:
        return 'Não há dados de faturamento válidos para processar.'
    
    menor_valor = min(valores)
    maior_valor = max(valores)
    
    # Calcula a média mensal
    media_mensal = sum(valores) / len(valores)
    
    # Calcula o número de dias com faturamento superior à média
    dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])
    
    return {
        'media_mensal': media_mensal,
        'menor_valor': menor_valor,
        'maior_valor': maior_valor,
        'dias_acima_da_media': dias_acima_da_media
    }

resultado = processar_faturamento('faturamento.json')

print(f'Media de faturamento no mês: R${resultado['media_mensal']:.2f}')
print(f'Menor valor de faturamento: R${resultado['menor_valor']:.2f}')
print(f'Maior valor de faturamento: R${resultado['maior_valor']:.2f}')
print(f'Numero de dias com faturamento acima da média: {resultado['dias_acima_da_media']}')

