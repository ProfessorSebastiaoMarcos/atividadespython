# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_i

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('Programa que procura o primeiro e o último nome')
print('-'*70)

nome = str(input('Digite o seu completo: '))

nomeQuebrado = nome.split()

print(f'{nome}')
print(f'{nomeQuebrado}')
print(f'Primeiro Nome: {nomeQuebrado[0]}')
print(f'Último NOme: {nomeQuebrado[-1]}')

print('-'*70)