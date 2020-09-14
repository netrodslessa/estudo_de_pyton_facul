# Desafio 06

# Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada

n = float(input('Digite um número: '))
q = n ** (1/2)
print('Dobro: {}\nTriplo: {}\nRaiz quadrada: {:.2f}'.format(n + n, n + n + n, q))
