nome = input('Qual seu nome? ')
print('Prazer em te conhecer: {:20}!'.format(nome))
# Saída: Prazer em te conhecer:  Ana                 !
print('Prazer em te conhecer: {:>20}!'.format(nome))
# Saída: Prazer em te conhecer:                   ana!
print('Prazer em te conhecer: {:=>20}!'.format(nome))
# Saída: Prazer em te conhecer: =================ana!
print('Prazer em te conhecer: {:=<20}!'.format(nome))
# Saída: Prazer em te conhecer: ana=================!
print('Prazer em te conhecer: {:=^20}!'.format(nome))
# Saída: Prazer em te conhecer: ========ana=========!
