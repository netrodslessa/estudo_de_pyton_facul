## Desafio 12

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.

preco = float(input('Digite o valor: '))
print('O valor com 5% de desconto fica em R$ {}'.format(preco - preco * 0.05))