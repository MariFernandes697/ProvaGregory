'''
Beecrowd 1060

Prof. Gregory ----- Aluno(a): Marianna Fernandes
15/05/2025
'''
# Pares, Impares, Positivos e Negativos

qtd_pares = 0
qtd_impares = 0
qtd_positivos = 0
qtd_negativos = 0

for i in range(5):
    valores = int(input(''))
    if valores % 2 == 0:
        qtd_pares = qtd_pares + 1
    else: 
        qtd_impares = qtd_impares + 1
    if valores > 0:
        qtd_positivos = qtd_positivos + 1
    elif valores < 0:
        qtd_negativos = qtd_negativos + 1

print(f'{qtd_pares} valor(es) par(es)')
print(f'{qtd_impares} valor(es) impar(es)')
print(f'{qtd_positivos} valor(es) positivo(s)')
print(f'{qtd_negativos} valor(es) negativo(s)')
