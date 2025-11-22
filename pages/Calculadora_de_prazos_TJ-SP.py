import streamlit as st
from datetime import date, datetime, timedelta
from pages.calculadora_prazo import menu_app, inicio_prazo, contador_prazo, transforma_datas, relatorio_app
from time import sleep
import os


st.title('Contador de prazos judiciais - TJ-SP')

data_usuario = st.date_input('Data do evento', value="today", format="DD.MM.YYYY")
prazo_usuario = st.number_input('Prazo', value=15, step=1, placeholder ='Insira o prazo aqui')

prazo_inicial = menu_app.menu_principal_radio(data_usuario)
prazo_final = contador_prazo.contador_prazo(prazo_inicial, prazo_usuario)

lista_inicio = inicio_prazo.gerar_lista_date_inicio(data_usuario, prazo_inicial)

prazo_inicial_str = transforma_datas.date_para_str(prazo_inicial)
prazo_final_str = transforma_datas.date_para_str(prazo_final)

st.subheader('Prazo Inicial')
st.write(prazo_inicial_str)
st.subheader('Prazo Final')
st.write(prazo_final_str)

relatorio_app.gerar_relatorio_prazo(prazo_inicial_str, prazo_final_str, lista_inicio)

with open("Relatório.docx", "rb") as file:
    st.download_button(
        label="Baixar Relatório Docx",
        data=file,
        file_name="Relatório.docx",
    )
    sleep(2)
    os.remove("Relatório.docx")


st.caption("Criado por Cesar Henrique Bruhn Pierre. Uso livre e gratuito. O autor não se responsabiliza por eventuais erros na contagem dos prazos, cabendo ao usuário adotar as devidas precauções.")

