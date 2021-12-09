# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_g

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('PROGRAMA QUE MOSTRA A MILHAR')
print('-'*50)

numero = int(input('Digite um número: '))

unidade = (numero // 1) % 10
dezena = (numero // 10) % 10
centena = (numero // 100) % 10
milhar = (numero // 1000) % 10

print(f'O número {numero} tem {unidade} unidade(s)')
print(f'O número {numero} tem {dezena} dezena(s)')
print(f'O número {numero} tem {centena} centena(s)')
print(f'O número {numero} tem {milhar} unidade(s) de milhar')

print('-'*50)