import streamlit as st

from pages.calculadora_prazo import transforma_datas
from pages.ortn import ortn

from datetime import date, datetime


def converte_real(valor_causa):
    valor_causa_str = str(valor_causa)
    valor_causa_str = valor_causa_str.replace('.', ',')
    return valor_causa_str


st.title('Atualização ORTN - IPCA - Recurso')

# Insere os dados da dívida
valor_causa = st.number_input('Valor da causa (R$)', placeholder ='Insira o valor da parcela a ser atualizada')
valor_causa_str = converte_real(valor_causa)
data_fim = st.date_input('Data de ajuizamento', value=date.today(), format="DD.MM.YYYY")
data_ajuizamento_str = transforma_datas.date_para_str(data_fim)

#Botão para atualizar
if st.button("Calcular"):
    ortn_corrigido = ortn.atualiza_ortn(valor_causa, data_fim)
    ortn_corrigido_str = converte_real(ortn_corrigido)

    st.subheader('Data do ajuizamento')
    st.write(data_ajuizamento_str)
    
    st.subheader('Valor da causa')
    st.write(f'R$ {valor_causa_str}')

    st.subheader('50 ORTN - IPCA-E')
    st.write(f'R$ {ortn_corrigido_str}')

    st.subheader('Recurso cabível: ')
    if valor_causa < ortn_corrigido:      
        st.write(f'Embargos infringentes')
    else:
        st.write(f'Apelação')


