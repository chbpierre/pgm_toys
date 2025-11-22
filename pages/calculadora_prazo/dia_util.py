from datetime import date, datetime

def verificador_dia_util(data):
    if data.weekday() > 4 or data in feriados:
        return False
    else:
        return True
    

def verificar_fds_feriado_relatorio(data):
    if data.weekday() == 5:
        return 'Sábado'
    if data.weekday() == 6:
        return 'Domingo'
    if data in feriados:
        return 'Feriado'

feriados = [
    date(2025, 2, 28),
    date(2025, 3, 3),
    date(2025, 3, 4),
    date(2025, 4, 17),
    date(2025, 4, 18),
    date(2025, 4, 21),
    date(2025, 5, 1),
    date(2025, 5, 2),
    date(2025, 5, 2),
    date(2025, 6, 19),
    date(2025, 6, 20),
    date(2025, 6, 27),
    date(2025, 7, 9),
    date(2025, 10, 28),
    date(2025, 11, 20),
    date(2025, 11, 21),
    date(2025, 12, 8),
    date(2025, 12, 20),
    date(2025, 12, 21),
    date(2025, 12, 22),
    date(2025, 12, 23),
    date(2025, 12, 24),
    date(2025, 12, 25),
    date(2025, 12, 26),
    date(2025, 12, 27),
    date(2025, 12, 28),
    date(2025, 12, 29),
    date(2025, 12, 30),
    date(2025, 12, 31),
    date(2026, 1, 1),
    date(2026, 1, 2),
    date(2026, 1, 3),
    date(2026, 1, 4),
    date(2026, 1, 5),
    date(2026, 1, 6),
    date(2026, 1, 7),
    date(2026, 1, 8),
    date(2026, 1, 9),
    date(2026, 1, 10),
    date(2026, 1, 11),
    date(2026, 1, 12),
    date(2026, 1, 13),
    date(2026, 1, 14),
    date(2026, 1, 15),
    date(2026, 1, 16),
    date(2026, 1, 17),
    date(2026, 1, 18),
    date(2026, 1, 19),
    date(2026, 1, 20),
         ]