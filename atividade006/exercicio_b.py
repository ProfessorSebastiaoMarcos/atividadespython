# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_b

# Importando as bibliotecas
import os
import math


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('PROGRAMA QUE TROCA NOME')
print('='*50)
nome = str(input('Digite um nome: '))

nomeNovo = nome.replace('Silva', 'Oliveira')

print(f'Nome antigo: {nome}')
print(f'Nome novo: {nomeNovo}')
print('-'*50)