# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
#Atividade011: exercício_a.py

import os

# limpando o terminal
os.system('cls')


def lista_numeros(lista):
    # criando listas pares e ímpares
    pares = []
    impares = []
    quantidade_pares = 0
    quantidade_impares = 0

    # imprimindo a lista
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
            quantidade_pares += 1
        else:
            impares.append(numero)
            quantidade_impares += 1
    return pares, impares, quantidade_pares, quantidade_impares


# Criando uma lista de números
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# passando a lista de números para a função
# e desempacotando os valores
num_pares, num_impares, quant_pares, quant_impares = lista_numeros(lista)

# Saída

print('-'*70)
print('Lista completa: ', end=' ')
for numero in lista:
    print(numero, end=' ')    
print()
print('='*70)

print(f'Lista de pares: ', end='')
for numero in num_pares:
    print(numero, end=' ')

print()

print(f'Lista de ímpares: ', end=' ')
for numero in num_impares:
    print(numero, end=' ')

print()

print(f'Quantidade de números pares: {quant_pares}')
print(f'Quantidade de números ímpares: {quant_impares}')
print('-'*70)
