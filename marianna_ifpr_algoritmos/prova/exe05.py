'''
Beecrowd 1060

Prof. Gregory ----- Aluno(a): Marianna Fernandes
15/05/2025
'''
#Soma de Impares Consecutivos I

x = int(input(''))
y = int(input(''))

soma = 0
for i in range(min(x,y)+ 1, max(x,y)):
    if i % 2 != 0:
        soma = soma + i
print(soma)

# Duas entradas + uma variável soma
# for i in range ( percorrer os números)
# min(x,y) procura o menor número
# max(x,y) procura o maior número
# if i != 0: soma = soma + i (Verifica se o número é impar para continuar e se for impar adicionar o valor de entrada a variavél soma)
        