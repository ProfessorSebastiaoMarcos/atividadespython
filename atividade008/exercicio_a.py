# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_a.py

# Crie a lista [1, 2, 3, 5, 6] e depois insira o 
# valor que está faltando na posição correta.

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Inserção de elemento')
print('='*70)

# Criando a lista
numeros = [1, 2, 3, 5, 6]

# Imprimindo a Lista
print(f'Números: {numeros}')

# Inserindo o valor 4 na posição 3
numeros.insert(3, 4)

# Imprimindo a lista
print(f'Números: {numeros}')