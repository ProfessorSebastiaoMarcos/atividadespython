# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_f.py

# Faça um programa que leia 5 nomes, 
# depois imprima estes nomes com seus respectivos índices.

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Nome com Índices')
print('='*70)

# Declarando variáveis
nomes = []

# criando um laço para pegar os nomes
for c in range(0, 4+1):
    nomes.append(str(input(f'Digite o {c+1}º nome: ')))


print('-'*60)
# Laço para imprimir o índice e o nome
for indice, nome in enumerate(nomes):
    print(f'Índice: {indice} :: {indice + 1}º Nome: {nome}')
print('-'*60)




