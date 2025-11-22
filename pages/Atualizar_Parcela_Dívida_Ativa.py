import streamlit as st
from datetime import date, datetime, timedelta
from pages.calculadora_prazo import transforma_datas
from pages.atualiza_divida_ativa import calculos

st.title('Atualização Dívida Ativa')

# Insere os dados da dívida
valor_original = st.number_input('Valor da parcela', placeholder ='Insira o valor da parcela a ser atualizada')
data_vencimento = st.date_input('Data do vencimento', value=None, format="DD.MM.YYYY")
data_final = st.date_input('Data final para atualização', value=None, format="DD.MM.YYYY")


#Botão para atualizar
if st.button("Calcular"):
    
    # Transforma as datas
    data_vencimento_str = transforma_datas.date_para_str(data_vencimento)
    data_final_str = transforma_datas.date_para_str(data_final)

    # Pega o ano das variáveis
    exercicio_divida = data_vencimento_str[6:]
    exercicio_final = data_final_str[6:]

    # Cálculo para dívidas anteriores a 2023
    if data_vencimento.year < 2023:

    # Calcula o indíce de correção monetária e aplica ao valor original da dívida de forma composta
        valor_corrigido = calculos.correcao_monetaria(valor_original, exercicio_divida, exercicio_final)
        
    # Calcula o valor dos juros de 1% ao mês considerando sobre o valor corrigido
        taxa_juros = calculos.juros_1(data_vencimento)
        valor_juros = valor_corrigido * taxa_juros

    # Calcula a Taxa Selic que será aplicada, conforme parâmetros - Calculaddda de forma smples, sem capitalização
        taxa_selic = calculos.calculo_selic(valor_corrigido, date(2022, 11, 1), data_final) 

    # Aplica a correção pela Taxa Selic apurada e depois acresce 1% (mês de pagamento)
        valor_atualizado_selic = valor_corrigido * (1 + ((1+taxa_selic)/100))

    # Calcula a multa de 20% + principal + juros
        multa = calculos.calculo_multa(valor_atualizado_selic)
        valor_atualizado_selic_multa = valor_atualizado_selic + multa + valor_juros

    # Calcula HA de 10% sobre o valor total
        ha = calculos.calculo_ha(valor_atualizado_selic_multa)
        valor_atualizado_selic_multa_ha = valor_atualizado_selic_multa + ha

    # Reporta os valores

        st.subheader('Valor corrigido monetariamente')
        st.write(f'R$ {valor_corrigido:.2f}')

        st.subheader('Taxa de juros 1%')
        st.write(f'{taxa_juros*100:.0f}%')

        st.subheader('Valor dos juros')
        st.write(f'R$ {valor_juros:.2f}')

        st.subheader('Taxa Selic acumulada no período')
        st.write(f'{taxa_selic:.2f}%')

        st.subheader('Taxa Selic + 1% na data do pagamento')
        st.write(f'{taxa_selic + 1.01:.2f}%')

        st.subheader('Valor atualizado (Taxa Selic + 1% no pagamento)')
        st.write(f'R$ {valor_atualizado_selic:.2f}')

        st.subheader('Valor da multa')
        st.write(f'R$ {multa:.2f}')

        st.subheader('Valor total')
        st.write(f'R$ {valor_atualizado_selic_multa:.2f}')

        st.subheader('Valor HA')
        st.write(f'R$ {ha:.2f}')

        st.subheader('Valor total + HA')
        st.write(f'R$ {valor_atualizado_selic_multa_ha:.2f}')

    else:

    # Calcula a Taxa Selic que será aplicada, conforme parâmetros - Calculaddda de forma smples, sem capitalização    
        taxa_selic = calculos.calculo_selic(valor_original, data_vencimento, data_final) 

    # Aplica a correção pela Taxa Selic apurada e depois acresce 1% (mês de pagamento)
        valor_atualizado_selic = valor_original * (1 + ((1+taxa_selic)/100))

    # Calcula a multa de 20% e soma ao principal
        multa = calculos.calculo_multa(valor_atualizado_selic)
        valor_atualizado_selic_multa = valor_atualizado_selic + multa

    # Calcula HA de 10% sobre o valor total
        ha = calculos.calculo_ha(valor_atualizado_selic_multa)
        valor_atualizado_selic_multa_ha = valor_atualizado_selic_multa + ha

    # Reporta

        st.subheader('Taxa Selic acumulada no período')
        st.write(f'{taxa_selic:.2f}%')

        st.subheader('Taxa Selic + 1% na data do pagamento')
        st.write(f'{taxa_selic + 1.01:.2f}%')

        st.subheader('Valor atualizado (Taxa Selic + 1% no pagamento)')
        st.write(f'R$ {valor_atualizado_selic:.2f}')

        st.subheader('Valor da multa')
        st.write(f'R$ {multa:.2f}')

        st.subheader('Valor total')
        st.write(f'R$ {valor_atualizado_selic_multa:.2f}')

        st.subheader('Valor HA')
        st.write(f'R$ {ha:.2f}')

        st.subheader('Valor total + HA')
        st.write(f'R$ {valor_atualizado_selic_multa_ha:.2f}')