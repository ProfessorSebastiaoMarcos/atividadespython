# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_h.py

# Faça um programa que leia um número indeterminado de notas 
# (pressione ‘s’ ou ‘0’ para sair).
# Após esta entrada de dados, faça o seguinte: 
# • Mostre a quantidade de notas que foram lidas.
# • Exiba todas as notas na ordem em que foram informadas.
# • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
# • Calcule e mostre a soma das notas.
# • Calcule e mostre a média das notas.

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Vogais na ordem inversa')
print('='*70)

# criando variáveis
notas = []
conta_notas = 0
soma = 0

# laço
while True:
    nota = float(input('Digite uma nota: '))
    notas.append(nota)

    sair = str(input('Deseja sair (s):'))

    if(sair in 'sS'):
        break

print('-'*70)
for i, nota in enumerate(notas):
    conta_notas += 1
    soma += nota
    print(nota, end=' ')
print()

print(f'Quantidade de notas: {conta_notas}')
print(f'Soma das notas: {soma}')

print('-'*70)
print('Fim do Programa!')
print()
