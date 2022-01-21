# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
# Atividade011: exercício_c.py - Cadastro de alunos

import os

# limpando o terminal
os.system('cls')


def titulo():
    print('-'*70)
    print('aluno(a)\t\tMatrícula\tNascimento')
    print('='*70)


def busca_aluno(cadastro_alunos):
    aluno = str(input('Entre com o nome do aluno: '))

    # Usando um laço
    # para encontrar o valor no cadastro_alunos
    for item in cadastro_alunos:
        if item['nome'] == aluno:
            print('Encontrado!')
            return item
        else:
            break


# Initialize list
cadastro_alunos = [
    {'nome': 'Diana Prince', 'matricula': '123456789', 'nascimento': 1960},
    {'nome': 'Carol Danvers', 'matricula': '987654321', 'nascimento': 1970},
    {'nome': 'Natalia Alianovna', 'matricula': '951753258', 'nascimento': 1980},
]

# Imprimindo a cadastro_alunos original
titulo()
for item in cadastro_alunos:
    for c, v in item.items():
        print(f'{v}', end='    \t')
    print()
print('-'*70)
print()

# invocando a função
resultado = busca_aluno(cadastro_alunos)

# Se a busca for verdadeira
if resultado:
    titulo()
    for chave, valor in resultado.items():
        print(f'{valor}', end='    \t')
    print()
    print('-'*70)

else:
    print('Aluno não encontrado!')
    print('-'*70)
    print()

