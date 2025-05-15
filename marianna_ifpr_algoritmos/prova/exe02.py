#Números Impares
'''
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

Entrada
O arquivo de entrada contém 1 valor inteiro qualquer.

Saída
Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.
'''
'''
Beecrowd 1067

Prof. Gregory ----- Aluno(a): Marianna Fernandes
24/04/2025
'''

x = int(input(''))

for x in range(1,x + 1,2):
    print(x)

'''
range (inicio, fim, passo a passo)
range (
    começa no 1, 
    termina no número que foi informado, no caso adiciona um caso o número informado seja impar também,
    diz para o código de quanto em quanto ele deve contar, nno caso de 2 em 2
      )
'''