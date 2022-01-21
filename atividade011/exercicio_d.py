# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
# Atividade011: exercício_d.py - Conversão de Temperatura

import os

# limpando o terminal
os.system('cls')


def conversao(temperatura):
    conversao = ((temperatura - 32) * 5) / 9
    return conversao


print('-'*70)
print('Programa para converter temperatura')
print('Fahrenheit para Célsius')
print('='*70)

# Entrada
temperatura = float(input('Informe a temperatura em Fahrenheit: '))

# invocando a função e guardando eum uma variável
resultado = conversao(temperatura)

print('-'*70)
print(f'Temperatura em Fahrenheit: {temperatura}')
print(f'{temperatura} °F = {resultado:.1f} °C')
print('='*70)
print()
