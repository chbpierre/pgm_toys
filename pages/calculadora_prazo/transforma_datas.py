from datetime import date, datetime

def str_para_date(data):
    data = datetime.strptime(data, "%d/%m/%Y").date()
    return data

def date_para_str(data):
    data = datetime.strftime(data, "%d/%m/%Y")
    return data