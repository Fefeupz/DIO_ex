from datetime import datetime, timedelta, date

tipo_carro = 'M'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes = tempo_pequeno)
    print(f'O carro chegou {data_atual} e ficará pronto às {data_estimada}')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes = tempo_medio)
    print(f'O carro chegou {data_atual} e ficará pronto às {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes = tempo_grande)
    print(f'O carro chegou {data_atual} e ficará pronto às {data_estimada}')

#Diminui a data em 1 dia e só retorna os valores de data, sem hora
print(date.today() - timedelta(days=1))

#Configurando manualmente dia e hora para conseguir diminuir de timedelta
resultado = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

