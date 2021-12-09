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

nomes = ['João', 'Maria', 'José', 'Pedro', 'John']
print(f'Minha Tupla: {nomes}')

if 'Pedro' in nomes:
    print('Pedro está na lista')
else:
    print('Pedro não está na lista')