# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_e

'''
Faça um programa para somar a quantidade de números 
pares encontrados no intervalo entre 0 e 100.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Jeito EQUIVICADO
print('-'*70)
print('For Range, quantidade de pares')
print('='*70)

# Declarações
contador = 0
somaPares = 0
quatidadePares = 0

# Estrutura de Repetição
for c in range(0, 100, 2):
    print(f'{c}', end=' ')
    contador += 1

print()
print(f'Quantidade de pares: {contador} números')
print('\n'+'-'*70)

# Jeito CORRETO
print('For Range, soma de pares')
print('='*70)

for c in range(0, 100):
    if (c % 2 == 0):

        # Quantidade de pares
        quatidadePares += 1

        # Soma de pares
        somaPares += c
        print(c, end=' ')
print()
print(f'Soma dos números pares: {somaPares}')
print(f'Quantidade de números pares: {quatidadePares} números')
