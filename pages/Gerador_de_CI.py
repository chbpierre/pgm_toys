import streamlit as st
from docx import Document
from datetime import date
from pages.gerador_ci import ci
import os
from time import sleep


def obter_iniciais(servidor, ignorar_preposicoes=True):
    preposicoes = {'da', 'de', 'do', 'das', 'dos', 'e'}
    partes = servidor.strip().split()
    if ignorar_preposicoes:
        iniciais = ''.join([parte[0].upper() for parte in partes 
                          if parte.lower() not in preposicoes])
    else:
        iniciais = ''.join([parte[0].upper() for parte in partes])    
    return iniciais


def gerar_numero_ci(numero_ci, data_ci, servidor):
    numero_ci_str = str(numero_ci)
    numero_ci_str += '-'
    ano = data_ci.year
    ano_str = str(ano)
    iniciais_str = obter_iniciais(servidor)
    iniciais_str += '-'
    numero_ci_estilizado = numero_ci_str + iniciais_str + ano_str
    return numero_ci_estilizado



st.title('Gerador de Comunicação Interna - CI')


numero_ci = st.number_input('Número da CI', step=1, placeholder="Digite apenas números")

data_ci = st.date_input('Data da CI', value='today', format="DD.MM.YYYY")
data_ci_str = (data_ci.strftime("%d/%m/%Y"))

origem = st.text_input('Origem - Campo "De: "')

destino = st.text_input('Destino - Campo "Para: "')

assunto = st.text_input('Assunto da CI')

servidor = st.text_input('Nome do servidor')

cargo = st.text_input('Cargo do servidor')

matricula = st.text_input('Matrícula do servidor')

texto = st.text_area('Texto da CI')


if st.button("Gerar certidão"):
    
    numero_ci_estilizado = gerar_numero_ci(numero_ci, data_ci, servidor)

    ci = ci.gerar_ci(origem, destino, assunto, data_ci_str, numero_ci_estilizado, servidor, cargo, matricula, texto)
     
    with open(ci, "rb") as file:
        st.download_button(
            label="Dowload CI",
            data=file,
            file_name=ci,
        )
        sleep(2)
        os.remove(ci)





