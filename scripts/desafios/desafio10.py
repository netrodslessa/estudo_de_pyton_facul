## Desafio 10

# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#  quantos Dólares ela pode comprar. Considerando USS 1,00 = R$ 3,27

r = float(input('Digite o valor em Reais: '))
print('US$ {:.2f}'.format(r * 3.27))
