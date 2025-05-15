'''
Beecrowd 1065

Prof. Gregory ----- Aluno(a): Marianna Fernandes
15/05/2025
'''
#Pares entre 5 números

qtd_pares = 0

for i in range(5):
    valores = int(input(''))
    if valores % 2 == 0:
        qtd_pares = qtd_pares + 1

print(f'{qtd_pares} valores pares')
