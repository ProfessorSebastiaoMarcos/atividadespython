# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_i

'''
Faça um programa que imprima os números no intervalo 
entre 1 e 10 em ordem inversa.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('For Range, ordem inversa')
print('='*70)

for c in range(10, 0, -1):
    print(c, end=' ')
print()
print('-'*70)