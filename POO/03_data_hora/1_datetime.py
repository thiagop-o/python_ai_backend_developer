from datetime import date, datetime, time

data = date(2023, 7, 10)
print(data)
print(date.today())


data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())

hora = time(10, 20, 0)
print(hora)

teste = datetime.today() - data_hora
print(type(teste))