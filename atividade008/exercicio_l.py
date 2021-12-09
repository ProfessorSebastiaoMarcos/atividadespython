# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_h.py

# Faça um programa que preencha uma lista com 50 números aleatórios. 
# Depois fatie essa lista em 5 listas de 10 elementos.


# Importando as bibliotecas
import os
from random import randint


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Lista de 50 números, ordem crescente')
print('='*70)

# Criando uma lista
numeros = []

# Acrescentando elementos a lista
for c in range(0, 10):
    n = randint(1, 10)
    numeros.append(n)

# Imprimindo as listas
print(f'Lista de Números: {numeros}')
l_ascendente = numeros.sort()
print(f'Lista ascendente: {numeros}')
l_descendente = numeros.sort(reverse = True)
print(f'Lista descendente: {numeros}')