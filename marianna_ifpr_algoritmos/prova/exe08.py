#Beecrowd 1019 – Conversão de Tempo
N = int(input())

horas = N // 3600
N = N % 3600

minutos = N // 60
segundos = N % 60

print(f"{horas}:{minutos}:{segundos}")

'''
Divida o número de segundos por 3600 → horas

Pegue o resto disso e divida por 60 → minutos

O que sobrar → segundos

'''