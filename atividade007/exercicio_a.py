# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_a

'''
Faça um programa que imprima os números no intervalo entre 1 e 100.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('Imprimir os números de 0 a 100')
print('='*70)

# utilizando o For
for c in range(0, 101):
    print(c, end=' ')
print()
print('-'*70)


# Utilizando o While
contador = 0

while (contador <= 100):    
    print(contador, end=' ')
    contador += 1
    
print()
print('-'*70)