'''
💡 Beecrowd 1051 - Imposto de Renda
📝 Enunciado:
Em um país imaginário, os habitantes pagam imposto conforme seu salário de acordo com a seguinte tabela:

Faixa de Salário (R$)	Alíquota
de 0.00 até 2000.00	Isento
de 2000.01 até 3000.00	8%
de 3000.01 até 4500.00	18%
acima de 4500.00	28%

A taxação só é aplicada sobre o valor que ultrapassar cada faixa.

Exemplo: Se a pessoa ganha 2500.00, ela paga 8% sobre os 500.00 excedentes da faixa isenta.

🔡 Entrada:
Um valor com duas casas decimais, representando o salário.

📤 Saída:
Imprima o valor do imposto a ser pago, com duas casas decimais.

Se for isento, imprima: Isento

✅ Exemplo de Entrada e Saída:
Entrada: 3002.00
Saída: R$ 80.36'''


salario = float(input())

imposto = 0.0

if salario <= 2000.00:
    print("Isento")
elif salario <= 3000.00:
    imposto = (salario - 2000.00) * 0.08
    print(f"R$ {imposto:.2f}")
elif salario <= 4500.00:
    imposto = (1000.00 * 0.08) + ((salario - 3000.00) * 0.18)
    print(f"R$ {imposto:.2f}")
else:
    imposto = (1000.00 * 0.08) + (1500.00 * 0.18) + ((salario - 4500.00) * 0.28)
    print(f"R$ {imposto:.2f}")



#Primeiro a entrada( salario )
# Se faz a análise do salário informado com as faixas de imposto de renda e as compara
# Após comparar, faz - se o desconto, com a faixa salarial anterior e o sobre o valor restante é aplicado a taxa de IR
