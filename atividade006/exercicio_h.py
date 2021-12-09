# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_h

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('Programa que calcula a quantidade de "o" e posição na String')
print('-'*70)

nome = str(input('Entre com o nome do aluno: ')).lower()

QuantidadeO = nome.count('o')
primeiroO = nome.find('o')
ultimoO = nome.rfind('o') #rfind() e lfind()  direita e esquerda

print(f'O caracter "o" aparece {QuantidadeO} vezes')
print(f'O caracter "o" aparece a primeira vez na posição {primeiroO + 1}')
print(f'O caracter "o" aparece a pela última vez na posição {ultimoO + 1}')
print('-'*70)