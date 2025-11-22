from datetime import date, timedelta, datetime
from pages.calculadora_prazo import dia_util

def contador_prazo(data, prazo):
    contador_prazo = 0
    while contador_prazo < prazo - 1:
        data += timedelta(days=1)
        if dia_util.verificador_dia_util(data):
            contador_prazo += 1
    return data