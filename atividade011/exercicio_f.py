# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
#Atividade011: exercício_f.py

'''
Crie uma função que receba 2 lista:
- lista 1: nome, peso, idade 
- lista 2: John, 40, 1.8
- Sua função deve criar um dicionário contendo chave e valor 
utilizando como base essas duas listas. Depois, seu programa 
deverá imprimir esse dicionário utilizando o laço for... items...
'''

import os
from traceback import print_tb


os.system('cls')


def monta_dicionario(lista1, lista2):
    # uso da função zip()
    # Esta função faz a junção das listas:
    # A 1ª lista se torna chave e a segunda o valor
    dicicionario = dict(zip(lista1, lista2))

    return dicicionario


lista_1 = ['nome', 'peso', 'idade']
lista_2 = ['John', 40, 1.80]

print('-'*70)
print('Juntando listas em dicionário')
print('='*70)

print(f'Lista 1:', end=' ')
for item in lista_1:
    print(f'{item}', end='\t')

print()
print(f'Lista 2:', end=' ')
for item in lista_2:
    print(f'{item}', end='\t')
print()
print('-'*70)

print()
print('Dicionário Montado com lista 1 e 2')
print('='*70)

resultado = monta_dicionario(lista_1, lista_2)

for chave, valor in resultado.items():
    print(f'{chave}: {valor}', end='\t')
print()
print('-'*70)
print()
