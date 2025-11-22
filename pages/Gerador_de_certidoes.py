import streamlit as st
from docx import Document
from datetime import date
from pages.gerador_certidao import tipos_de_certidao
import os
from time import sleep

st.title('Gerador de certidões')

processos = []
autores = []

opcao_tipo_certidao = st.selectbox(
    'Tipo de certidão',
    ('PCCV Magistério - Recurso Inominado', "PCCV Geral - Recurso Inominado", 'ATS Hora extra', 'PCCV Geral - Apelação'),
    index=None,
    placeholder='Selecione qual tipo de certidão será emitida'
)

data_certidão = st.date_input('Especifique a data da certidão', value='today', format="DD.MM.YYYY")
data_certidão = (data_certidão.strftime("%d/%m/%Y")) + "."

#cadastro procurador
procurador = st.text_input('Nome do procurador')
oab = st.text_input('OAB do procurador', placeholder='Digite no seguinte formato "111.111"')

#cadastro processos
processo = st.text_input('Número do processo judicial: ')
parte_contraria = st.text_input('Nome do autor: ')

if st.button("Gerar certidão"):
    certidao = tipos_de_certidao.gerar_certidão(opcao_tipo_certidao, procurador, oab, processo, data_certidão, parte_contraria)
     
    with open(certidao, "rb") as file:
        st.download_button(
            label="Dowload Certidão",
            data=file,
            file_name=certidao,
        )
        sleep(2)
        os.remove(certidao)





