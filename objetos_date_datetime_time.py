from datetime import date, datetime, time

#Como marcar um dia especifico em python
d = date(2024, 7, 19)
print(d) #2024-07-19
print(date.today()) #Data do dia atual

#Adicionando horas nas data
data_hora = datetime(2023, 7, 10)
print(data_hora) #2023-07-10 00:00:00
print(datetime.today()) #Data e horario atual do dia atual

#Adicionando horario especifico
hora = time(10, 20, 0) 
print(hora) #10:20:00 