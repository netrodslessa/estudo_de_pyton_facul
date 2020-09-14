## Desafio 11

# Faça um programa que leia a altura e a largura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta, pinta uma área de 2m².

h = float(input("Digite a altura: "))
b = float(input("Digite a largura: "))
area = 2 * (h + b)
print('Você vai precisar de {:.1f} litros de tinta '.format(area / 2)) 