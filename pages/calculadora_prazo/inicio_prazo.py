from datetime import date, timedelta, datetime
from pages.calculadora_prazo import dia_util

def gerar_lista_date_inicio(data_usuario, prazo_inicial):
    lista_inicial = []
    while data_usuario < prazo_inicial:
        lista_inicial.append(data_usuario)
        data_usuario += timedelta(days=1)
    return lista_inicial


def disponibilizacao_dje(data_usuario):
    data_publicacao = data_usuario + timedelta(days=1)
    while not dia_util.verificador_dia_util(data_publicacao):
        data_publicacao += timedelta(days=1)
    data_inicio_prazo = data_publicacao + timedelta(days=1)
    while not dia_util.verificador_dia_util(data_inicio_prazo):
        data_inicio_prazo += timedelta(days=1)
    return data_inicio_prazo


def juntada(data_usuario):
    data_inicio_prazo = data_usuario
    data_inicio_prazo += timedelta(days=1)
    while not dia_util.verificador_dia_util(data_inicio_prazo):
        data_inicio_prazo += timedelta(days=1)
    return data_inicio_prazo


def portal(data_usuario):
    data_inicio_prazo = data_usuario
    data_inicio_prazo += timedelta(days=10)
    while not dia_util.verificador_dia_util(data_inicio_prazo):
        data_inicio_prazo += timedelta(days=1)
    return data_inicio_prazo
