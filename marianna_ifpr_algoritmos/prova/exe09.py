'''
💡 Beecrowd 1050 - DDD
📝 Enunciado:
Leia um número inteiro que representa um código de DDD (discagem direta à distância). Em seguida, informe à qual cidade o DDD pertence.

Se o DDD não estiver na lista, imprima:
'''

ddd = int(input())

cidades = {
    61: "Brasília",
    71: "Salvador",
    11: "São Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitória",
    31: "Belo Horizonte"
}

if ddd in cidades:
    print(cidades[ddd])
else:
    print("DDD não cadastrado")


#Cadastrar uma lista
#Mostrar o dd e sua cidade respectiva
#Caso não houver ddd, informar que não está cadastrado9