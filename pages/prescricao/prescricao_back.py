import pandas as pd
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from pages.calculadora_prazo import transforma_datas

def calculadora_prescrição(dic_base):

    def verificacao_prescricao(dt_presc):
        if dt_presc <= dt_hoje:
            resultado = 'PRESCRITO'
        else:
            resultado = 'NÃO PRESCRITO'
        return resultado
            
    def soma_cinco(data):
        return data + relativedelta(years=5)

    def prescrição():
        # AQUI FOI CORRIGIDO: de global para nonlocal
        # nonlocal avisa ao Python que essas variáveis pertencem à calculadora_prescrição()
        nonlocal dt_base, dt_prescricao 
        
        # Uso de .get() para evitar erro caso não tenha data de Inscrição na interface
        if dic_base.get('Inscrição') and dic_base['Inscrição'] <= dt_prescricao:
            continua_inscricao = True
            
            if natureza_débito == 'NÃO TRIBUTÁRIO':
                dt_base += timedelta(days=180)
                dt_prescricao = soma_cinco(dt_base)

        elif dic_base.get('Inscrição') and dic_base['Inscrição'] > dt_prescricao:
            continua_inscricao = False
            resultado = verificacao_prescricao(dt_prescricao)
            return dt_prescricao, resultado
            
        else:
            # Caso a inscrição venha vazia do Front-end
            continua_inscricao = True

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


    # --- Varáveis da função principal ---
    
    natureza_débito = dic_base.get('Tipo', 'TRIBUTÁRIO')

    dic_dts = {
        'dt_protesto'     : dic_base.get('Protesto'),
        'dt_despacho'     : dic_base.get('Despacho'),
        'dt_parcelamento' : dic_base.get('Parcelamento')
    }

    dt_hoje = date.today()
    dt_base = dic_base['Vencimento']
    dt_prescricao = soma_cinco(dt_base)

    if dic_base.get('Fase') in ['DÍVIDA ATIVA', 'EM COBRANÇA']:
        dt_prescricao_final, resultado = prescrição()

        dic_comp = {
            'Prescrição' : dt_prescricao_final,
            'Resultado'       : resultado
        }

        dic_base.update(dic_comp)

    else:    
        dic_comp = {
            'Prescrição' : '',
            'Resultado'  : 'ANÁLISE PELO PROCURADOR DA EF'
        }
        
        dic_base.update(dic_comp)

    for chave, valor in dic_base.items():
        if isinstance(valor, date):
            dic_base[chave] = transforma_datas.date_para_str(valor)
        elif not valor:
            dic_base[chave] = ''    
    lista_dic = [dic_base]

    df = pd.DataFrame(lista_dic)

    return df