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

#Entrada de dados e declarações
numero = int(input('Digite um número entre 1 e 20: '))
npc = randint(1, 3) #npc: non-player character

#Validação
if(numero < 0 or numero > 3):
    print('Número inválido!')
else:
    print(f'Sua escolha: {numero}')
    print(f'NPC: {npc}')
    print('-'*50)
    if (numero == npc):
        print('- Você ganhou!!!')
    else:
        print('- Você perdeu!')

#Saída
print('-' * 50)
print(f'Fim do programa!')
print('-' * 50)
print()