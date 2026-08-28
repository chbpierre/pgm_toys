def atualiza_ortn(valor_causa, data_fim):
    from bcb import sgs

    DATA_INICIO = '2001-01-01'
    ORTN = 328.27
    
    ipcae = sgs.get({'IPCA-E' : 10764}, start=DATA_INICIO, end=data_fim)

    ipcae['IPCA-E'] = (ipcae['IPCA-E'] / 100) + 1
    ortn_corrigido = round((ORTN * ipcae['IPCA-E'].prod()), 2)

    return ortn_corrigido
   