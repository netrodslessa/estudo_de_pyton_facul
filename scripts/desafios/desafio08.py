## Desafio 08

# Escreva um programa que leia um valor em metros e o exiba convertido em 
# centímetros e milímetros.

cent = float(input('Digite o número em metros: '))
print('São {}cm e {}mm'.format(cent * 100, cent * 1000))