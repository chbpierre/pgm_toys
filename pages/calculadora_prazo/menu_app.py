from datetime import date, datetime, timedelta
from pages.calculadora_prazo import inicio_prazo
import streamlit as st

def menu_principal_radio(data):
    opcao_usuario_menu = st.radio(
        "Selecione o marco para início da contagem do prazo",
        ["Data da disponibilização DJE", "Data da juntada mandado", "Data do encaminhamento ao Portal da Fazenda Pública"]                          
    )
    if opcao_usuario_menu == "Data da disponibilização DJE":
        prazo_inicial = inicio_prazo.disponibilizacao_dje(data)
        return prazo_inicial
    if opcao_usuario_menu == "Data da juntada mandado":
        prazo_inicial = inicio_prazo.juntada(data)
        return prazo_inicial
    if opcao_usuario_menu == "Data do encaminhamento ao Portal da Fazenda Pública":
        prazo_inicial = inicio_prazo.portal(data)
        return prazo_inicial
        