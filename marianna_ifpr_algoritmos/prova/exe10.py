'''
Beecrowd 1072

Prof. Gregory ----- Aluno(a): Marianna Fernandes
15/05/2025
'''

'''Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).
'''
#Minha versão

n = int(input(''))
qtd_xintervalo = 0
qtd_foraintervalo = 0

for x in range(n):
  x = int(input(''))
  if(x>=10 and x<=20):
    qtd_xintervalo = qtd_xintervalo + 1 

  else:
    qtd_foraintervalo = qtd_foraintervalo + 1


print(f'{qtd_xintervalo} in')
print(f'{qtd_xintervalo} out')


#Versão do Chat
n = int(input())
qtd_xintervalo = 0
qtd_foraintervalo = 0

for _ in range(n):
    x = int(input())
    if 10 <= x <= 20:
        qtd_xintervalo += 1
    else:
        qtd_foraintervalo += 1

print(f'{qtd_xintervalo} in')
print(f'{qtd_foraintervalo} out')