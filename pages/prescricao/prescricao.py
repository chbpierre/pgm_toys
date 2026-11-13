import pandas as pd
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from rich import print
from pages.calculadora_prazo import transforma_datas

def verificacao_prescricao(dt_prescricao):
    print(f'Data prescrição : {transforma_datas.date_para_str(dt_prescricao)}')
    print(f'Data hoje       : {transforma_datas.date_para_str(dt_hoje)}')
    if dt_prescricao <= dt_hoje:
        resultado = 'PRESCRITO'
        print(f'[red]{resultado}[/red]')
    else:
        resultado = 'NÃO PRESCRITO'
        print(f'[green]{resultado}[/green]')
    return resultado
        

def soma_cinco(data):
    return data + relativedelta(years=5)


def prescrição():
    global dt_base, dt_prescricao
    
    if dt_inscricao <= dt_prescricao:
        continua_inscricao = True
        
        if natureza_débito == 'NÃO TRIBUTÁRIO':
            dt_base += timedelta(days=180)
            dt_prescricao = soma_cinco(dt_base)

    elif dt_inscricao > dt_prescricao:
        continua_inscricao = False
        resultado = verificacao_prescricao(dt_prescricao)
        return dt_prescricao, resultado

    lista_data = [dt_prescricao]

    if continua_inscricao:
        
        for nome_dt, dt in dic_dts.items():
            
            if dt is None:
                continue

            if nome_dt == 'dt_protesto':
                if natureza_débito == 'TRIBUTÁRIO' and dt >= date(2024, 6, 3):
                    lista_data.append(soma_cinco(dt))
            else:
                lista_data.append(soma_cinco(dt))

        dt_prescricao_final = max(lista_data)

        resultado = verificacao_prescricao(dt_prescricao_final)

        return dt_prescricao_final, resultado


# Varáveis
dt_vencimento   = date(2020,9, 1)
dt_inscricao    = date(2021, 2, 3)
dt_protesto     = date(2022, 1, 1)
dt_despacho     = date(2021, 1, 2)
dt_parcelamento = date(2021, 2, 5)

dt_hoje = date.today()
dt_base = dt_vencimento
dt_prescricao = soma_cinco(dt_base)

natureza_débito = 'NÃO TRIBUTÁRIO'
fase = 'DÍVIDA ATIVA'


# Dicionários
dic_dts = {
    'dt_protesto'     : dt_protesto,
    'dt_despacho'     : dt_despacho,
    'dt_parcelamento' : dt_parcelamento
}

dic = {
    'Tipo'              : natureza_débito,   
    'Vencimento'        : dt_vencimento,
    'Data inscrição'    : dt_inscricao,
    'Data despacho'     : dt_despacho,
    'Data parcelamento' : dt_parcelamento,
    'Data protesto'     : dt_protesto 
}

if fase == 'DÍVIDA ATIVA':
    dt_prescricao_final, resultado = prescrição()

    dic_comp = {
    'Data prescrição' : dt_prescricao_final,
    'Resultado'       : resultado
 }

    dic.update(dic_comp)


else:    
    dic_comp = {
    'Data prescrição' : None,
    'Resultado'       : 'ANÁLISE PELO PROCURADOR DA EF'
 }

    dic.update(dic_comp)


for chave, valor in dic.items():
    if isinstance(valor, date):
        dic[chave] = transforma_datas.date_para_str(valor)

lista_dic = [dic]

df = pd.DataFrame(lista_dic)

print(f'[blue]{df}[/blue]')
