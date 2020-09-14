## Desafio 13

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo 
# salário, com 15% de aumento.

sal = float(input('Digite o valor do salário: '))
print('Com reajuste fica em R$ {:.2f}'.format(sal + sal * 0.15))