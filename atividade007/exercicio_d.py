# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_d

'''
Faça um programa que imprima os números pares de 0 e 100.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('For Range, números pares [0-100]')
print('='*70)

for c in range(0, 102, 2):
    print(f'{c}', end=' ')
print('\n'+'-'*70)
print()
print()
print('-'*70)

# Exemplo com While
print('For Range, números pares [0-100]')
print('='*70)

contador = -2
while (contador <= 98):
    contador += 2
    print(f'{contador}', end=' ')
print('\n'+'-'*70)