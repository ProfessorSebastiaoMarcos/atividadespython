# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
# Atividade011: exercício_b.py - Cadastro de alunos

import os

# limpando o terminal
os.system('cls')


def cadastrar():
    alunos = {}
    lista = []
    for c in range(2):
        alunos['nome'] = str(input('Nome do aluno: '))
        alunos['matricula'] = str(input('Matrícula do aluno: '))
        alunos['nascimento'] = str(input('Data de nascimento do aluno: '))

        lista.append(alunos.copy())

    os.system('cls')
    print('-'*70)
    print('Alunos Cadastrados')
    print('='*70)

    for aluno in lista:  # para cada elemento na minha lista
        for chave, valor in aluno.items():  # para cada chave e valor do aluno
            print(f'{chave} : {valor}', end=' ' + '\n')
        print('-'*80)


print('-'*70)
print('Cadastro de Alunos')
print('='*70)
cadastrar()
