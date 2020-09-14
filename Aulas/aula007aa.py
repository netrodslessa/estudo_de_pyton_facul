n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'. format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))
# Entrada: 4, 3
# Saída:
# A soma é 7, o produto é 12 e a divisão é 1.33
# Divisão inteira 1 e potência 64