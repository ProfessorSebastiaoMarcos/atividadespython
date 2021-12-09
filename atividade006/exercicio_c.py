# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_c

# Importando as bibliotecas
import os
import math


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('PROGRAMA PARA ENCONTRAR NOME')
print('='*50)

nome = str(input('Digite o nome: '))
print()

if ('Oliveira' in nome):
    print('Nome Encontrado!')
else:
    print('Nome não Encontrado!')
print('-'*50)
print()