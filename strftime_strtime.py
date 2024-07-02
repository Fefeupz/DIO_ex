from datetime import datetime 

data_hora_atual = datetime.now() #Atribuindo a variavel o valor de datetime
data_hora_str = "2024-07-02 10:20" #Atribuindo data e horario a variavel
mascara_ptbr = '%d/%m/%Y %a' #Atribuindo a variavel o formato brasileiro de horario
mascara_en = '%Y-%m-%d %H:%M' #Atribuindo a variavel o formato ingles de horario

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
print(type(data_convertida))