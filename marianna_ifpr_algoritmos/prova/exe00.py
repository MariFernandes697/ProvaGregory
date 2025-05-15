# Números positivos Beecrowd 1060
'''
Beecrowd 1060

Prof. Gregory ----- Aluno(a): Marianna Fernandes
15/05/2025
'''

qtd_valores = 0

for i in range(6):
    valores = float(input(''))
    if valores > 0:
        qtd_valores = qtd_valores + 1

print(f'{qtd_valores} valores positivos')

'''
Declara duas variáveis: uma para os números serem recebidos, outra para contar os números que forem positivos
A variavél qtd_valores adiciona um valor a si mesma apenas quando o valor da entrada for maior que 0.

'''