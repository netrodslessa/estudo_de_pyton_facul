# Desafio 04
# Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas
# as informações possíveis sobre ele.

inp = input('Digite algo: ')
print(inp)
print('O tipo primitivo desse valor é: ', type(inp))
print('Só tem espaços? ', inp.isspace())
print('É um número? ', inp.isnumeric())
print('É alfabético? ', inp.isalpha())
print('É alfanumérico? ', inp.isalnum())
print('Está em maiúsculo? ',inp.isupper())
print('Está em minúsculo? ',inp.islower())
print('Está capitalizada? ', inp.istitle())