# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_f

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('PROGRAMA PARA SEPARAR NOME')
print('-'*50)

nome = str(input('Digite o nome da pessoa: '))

nomeSeparado = nome.split()
posicaoNomeSeparado = nomeSeparado[0]

print(f'Nome completo: {nome}')
print(f'Nome separado: {nomeSeparado}')
print(f'O primeiro nome é: {posicaoNomeSeparado}')
print('-'*50)