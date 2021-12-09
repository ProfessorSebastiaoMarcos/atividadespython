
# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_d.py

# Faça um programa que preencha uma lista com as notas de 4 alunos, 
# depois imprima a média.


# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Média de Notas')
print('='*70)

# Declarando variáveis
notas = []
soma = 0
media = 0

# Primeiro pego as notas e crio uma lista
for c in range(0, 4):
    nota = float(input(f'Digite a {c+1}ª nota: '))
    notas.append(nota) # grava as 4 notas na lista

    # somando as notas
    soma += nota

# Cálculo da Média
media = soma /4

#Saída
print('-'*70)
print('Notas: ', end=' ')
for i, nota in enumerate(notas):
    print(nota, end=' ')

print() 
print(f'Soma das notas: {soma}') 
print(f'Média de notas é: {media}')
print('-'*70)




