import streamlit as st
import pandas as pd
from datetime import date
from pages.prescricao.prescricao_back import calculadora_prescrição


def converter_download(df):
    from weasyprint import HTML, CSS

    html = """
    <style>
        @page { size: A4 landscape; margin: 10mm; }
        table { width: 100%; table-layout: fixed; }
        th, td {
            text-align: left;
            padding: 4px;
            font-size: 8pt;
            overflow-wrap: break-word;
        }
    </style>
    """ + df_final.to_html(index=False, justify="left", border=0)

    HTML(string=html).write_pdf(
        'planilha_prescricao.pdf',
        stylesheets=[CSS(string="@page { size: A4 landscape; margin: 1cm; }")]
    )

    with open('planilha_prescricao.pdf', 'rb') as f:
        pdf_bytes = f.read()

    # html = df.style.set_table_attributes('style="border-collapse: collapse; width: 100%; font-family: Arial; font-size: 10px;"').to_html(justify='center', index=False)


    return df.to_csv(index=False), pdf_bytes #df.to_html(index=False)


st.set_page_config(layout="wide")

st.title('Calculadora de prescrição', text_alignment='center', icon=':material/calculate:')

st.write('')
st.write('')

# Usar uma LISTA para acumular múltiplos débitos
if "lista_debitos" not in st.session_state:
    st.session_state["lista_debitos"] = []

with st.container():

    with st.form('form', clear_on_submit=True):

        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

        with col1:
            cda = st.text_input("CDA")
            
        with col2:
            lançamento = st.text_input("GUIA")
            
        with col3:
            natureza_débito = st.selectbox(
                "Tipo",  # Retornado para Tipo
                ("TRIBUTÁRIO", "NÃO TRIBUTÁRIO"),
                index=None,
                placeholder='Selecione'
            )

        with col4:
            fase = st.selectbox(
                "Fase",
                ('EM COBRANÇA', 'DÍVIDA ATIVA', 'EXECUÇÃO FISCAL'),
                index=None,
                placeholder='Selecione'
            )

        with col5:
            dt_vencimento = st.date_input(
                'Vencimento',
                min_value=date(2010, 1, 1),
                max_value='today',
                format="DD.MM.YYYY",
                value=None
                )
            
        with col6:
            dt_inscricao = st.date_input(
                'Inscrição',
                min_value=date(2010, 1, 1),
                max_value='today',
                format="DD.MM.YYYY",
                value=None
                )

        with col7:
            dt_parcelamento = st.date_input(
                'Parcelamento',
                min_value=date(2010, 1, 1),
                max_value='today',
                format="DD.MM.YYYY",
                value=None
                )

        with col8:
            dt_despacho = st.date_input(
                'Despacho',
                min_value=date(2010, 1, 1),
                max_value='today',
                format="DD.MM.YYYY",
                value=None
                )

        with col9:
            dt_protesto = st.date_input(
                'Protesto',
                min_value=date(2010, 1, 1),
                max_value='today',
                format="DD.MM.YYYY",
                value=None
                )

        # st.write('')
        st.divider()

        btn1, btn2, btn3 = st.columns(3, gap='large')
        
        with btn1:
            btn_add = st.form_submit_button('Adicionar', icon=':material/add:', use_container_width=True)
        with btn2:
            btn_apagar = st.form_submit_button('Remover último', icon=':material/remove:', use_container_width=True)
        with btn3:
            btn_limpar = st.form_submit_button('Limpar', icon=':material/refresh:', use_container_width=True)


# AÇÕES DOS BOTÕES
if btn_add:
    if dt_vencimento is None:
        st.warning("O preencihimento do vencimento é obrigatório para o cálculo!")
    elif natureza_débito is None:
        st.warning("O preenchimento do tipo é obrigatório para o cálculo!")
    elif fase is None:
        st.warning("O preenchimento da fase do débito é obrigatório para o cálculo!")
    else:
        dic_add = {
            'GUIA'         : lançamento,
            'CDA'          : cda,
            'Tipo'         : natureza_débito, 
            'Fase'         : fase,
            'Vencimento'   : dt_vencimento,
            'Inscrição'    : dt_inscricao,
            'Parcelamento' : dt_parcelamento,
            'Despacho'     : dt_despacho,
            'Protesto'     : dt_protesto
        }
        st.session_state["lista_debitos"].append(dic_add)
        
if btn_apagar:
    if st.session_state["lista_debitos"]:
        st.session_state["lista_debitos"].pop()
    else:
        st.warning("A lista já está vazia.")

if btn_limpar:
    st.session_state["lista_debitos"].clear()


# RENDERIZAÇÃO DA TABELA 
st.write("---")

if st.session_state["lista_debitos"]:
    lista_dfs = []
    
    for debito in st.session_state["lista_debitos"]:
        df_resultado = calculadora_prescrição(debito.copy())
        lista_dfs.append(df_resultado)
    
    df_final = pd.concat(lista_dfs, ignore_index=True)
    
    st.dataframe(df_final, hide_index=True, use_container_width=True)
else:
    st.info("Nenhum débito cadastrado ainda.")

st.write("---")

fin1, fin2 = st.columns(2, gap='xxlarge')

if st.session_state["lista_debitos"]:
    csv, pdf_bytes = converter_download(df_final)

    st.session_state['df_final'] = df_final

    with fin1:
        btn_csv = st.download_button('Exportar CSV', 
        data=csv,
        file_name="planilha_prescricao.csv", 
        icon=":material/download:",
        width="stretch"
        )

    with fin2:
        btn_pdf = st.download_button('Exportar PDF', 
        data=pdf_bytes,
        file_name="planilha_prescricao.pdf", 
        icon=":material/download:",
        width="stretch"
        )

    # with fin2:
    #     btn_html = st.download_button('Exportar HTML', 
    #     data=html,
    #     file_name="planilha_prescricao.html", 
    #     icon=":material/download:"
    #     )
