# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_a

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('PROGRAMA JUNTAR NOME')
print('-'*50)

nome = str(input('Qual o primeiro Nome: '))
segundoNome = str(input('Qual o segundo Nome: '))
sobrenome = str(input('Qual o Sobrenome: '))

nomeCompleto = nome + segundoNome + sobrenome

print(f'O nome completo é: {nomeCompleto}')
print('-'*50)