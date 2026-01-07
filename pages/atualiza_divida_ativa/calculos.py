from datetime import date, datetime


def correcao_monetaria(valor_original, exercicio_divida, exercicio_final):
    
    valor_corrigido = valor_original
    
    exercicio_divida = int(exercicio_divida)
    exercicio_divida += 1

    exercicio_final = int(exercicio_final)
    
    while exercicio_divida <= exercicio_final:
        if exercicio_divida < 2024:
            valor_corrigido *= (1 + (correcao_tabela[exercicio_divida]/100))
        exercicio_divida += 1
    
    return valor_corrigido


def juros_1(data_vencimento):
    data_final = date(2022, 11, 30)
    total_meses = ((data_final.year - data_vencimento.year) * 12)
    total_meses += data_final.month - data_vencimento.month
    taxa_juros = total_meses * 0.01
    print(taxa_juros)
    return taxa_juros
    

def calculo_selic(valor_original, data, data_final):

    valor_acumulado = valor_original
    selic_acumulada = 0
   
    data_final = data_final.replace(day=1)
    data = data.replace(day=1)

    primeira_taxa = selic_mensal[data]

    while data < data_final:

        selic_acumulada += selic_mensal[data]

        mes_atual = data.month
        mes_atual = int(mes_atual)
        ano_atual = data.year
        ano_atual = int(ano_atual)
        if mes_atual < 12:
            data = data.replace(month=mes_atual+1)
        elif mes_atual == 12:
            ano_atual += 1 
            data = data.replace(year=ano_atual)
            data = data.replace(month=1)

    return selic_acumulada - primeira_taxa

def calculo_multa(valor):
    return valor * 0.20


def calculo_ha(valor):
    return valor * 0.10
        
    
correcao_tabela = {
    2018 : 1.944,
    2019 : 3.558,
    2020 : 3.367,
    2021 : 5.198,
    2022 : 10.960,
    2023 : 5.975,
    2024: 4.685
    }

selic_mensal = {
    
    #Taxas de 2022
    date(2022, 11, 1): 1.02, # Novembro de 2022
    date(2022, 12, 1): 1.12, # Dezembro de 2022
    
    # Taxas de 2023
    date(2023, 1, 1): 1.12, # Janeiro de 2023 [1]
    date(2023, 2, 1): 0.92, # Fevereiro de 2023 [1]
    date(2023, 3, 1): 1.17, # Março de 2023 [1]
    date(2023, 4, 1): 0.92, # Abril de 2023 [1]
    date(2023, 5, 1): 1.12, # Maio de 2023 [1]
    date(2023, 6, 1): 1.07, # Junho de 2023 [1]
    date(2023, 7, 1): 1.07, # Julho de 2023 [1]
    date(2023, 8, 1): 1.14, # Agosto de 2023 [1]
    date(2023, 9, 1): 0.97, # Setembro de 2023 [1]
    date(2023, 10, 1): 1.00, # Outubro de 2023 [1]
    date(2023, 11, 1): 0.92, # Novembro de 2023 [1]
    date(2023, 12, 1): 0.89, # Dezembro de 2023 [1]
    
    # Taxas de 2024
    date(2024, 1, 1): 0.97, # Janeiro de 2024 [1]
    date(2024, 2, 1): 0.80, # Fevereiro de 2024 [1]
    date(2024, 3, 1): 0.83, # Março de 2024 [1]
    date(2024, 4, 1): 0.89, # Abril de 2024 [1]
    date(2024, 5, 1): 0.83, # Maio de 2024 [1]
    date(2024, 6, 1): 0.79, # Junho de 2024 [1]
    date(2024, 7, 1): 0.91, # Julho de 2024 [1]
    date(2024, 8, 1): 0.87, # Agosto de 2024 [1]
    date(2024, 9, 1): 0.84, # Setembro de 2024 [1]
    date(2024, 10, 1): 0.93, # Outubro de 2024 [1]
    date(2024, 11, 1): 0.79, # Novembro de 2024 [1]
    date(2024, 12, 1): 0.93, # Dezembro de 2024 [1]
    
    # Taxas de 2025
    date(2025, 1, 1): 1.01, # Janeiro de 2025 [1]
    date(2025, 2, 1): 0.99, # Fevereiro de 2025 [1]
    date(2025, 3, 1): 0.96, # Março de 2025 [1]
    date(2025, 4, 1): 1.06, # Abril de 2025 [1]
    date(2025, 5, 1): 1.14, # Maio de 2025 [1]
    date(2025, 6, 1): 1.10, # Junho de 2025 [1]
    date(2025, 7, 1): 1.28, # Julho de 2025 [1]
    date(2025, 8, 1): 1.16, # Agosto de 2025 [1]
    date(2025, 9, 1): 1.22, # Setembro de 2025 [1]
    date(2025, 10, 1): 1.28, # Outubro de 2025 [1]
    date(2025, 11, 1): 1.05, # Novembro de 2025
    date(2025, 12, 1): 1.22} # Dezembro de 20205
