# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_f

'''
Faça um programa que imprima os números primos entre 0 e 100.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('For Range, número primo')
print('='*70)

# Declaração
#limite = 100
inicio = 0
fim = 20
for c in range(inicio, fim + 1):
    divisores = 0

    for j in range(1, c+1):
        if(c % j == 0):
            divisores = divisores + 1
    
    if (divisores == 2):
        print(c, end=' ')
print()
print('='*70)