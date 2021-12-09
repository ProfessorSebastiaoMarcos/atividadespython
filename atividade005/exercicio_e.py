# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 10/11/2021
# Exercício_a: Raíz quadrada

# Importando as bibliotecas
import os
from random import randint


# Limpando o terminal
os.system('cls')

# Título
print('-' * 50)
print('PROGRAMA PARA SORTEAR UM NÚMERO')
print('=' * 50)

#Cálculo
numeroSorteado = randint(1, 20)

#Saída
print(f'O número sorteado foi: {numeroSorteado}')
print('-' * 50)
print()