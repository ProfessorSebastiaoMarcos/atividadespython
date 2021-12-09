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
print('Lista de 50 números')
print('='*70)


# Criar variável
numeros = []

# iniciar o laço
for c in range(0, 50+1):
    numeros.append(randint(1, 50))

print(numeros[0:10])
print(numeros[11:21])
print(numeros[21:31])
print(numeros[31:41])
print(numeros[41:51])

print('-'*70)
print('Fim do Programa!')
print()