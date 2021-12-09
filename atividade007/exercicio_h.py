# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_h

'''
Faça um programa que imprima os valores no intervalo definido pelo usuário. 
O usuário poderá definir 3 números que deverão ser ignorados, ou seja, 
que não serão impressos na tela.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('For Range, ignorar numeros em um intervalo')
print('='*70)

# Declaração
#limite = 100

#Entrada de dados
inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o inicio do intervalo: '))
print('-'*70)
ignorar1 = int(input('ignorar 1º número: '))
ignorar2 = int(input('ignorar 2º número: '))
ignorar3 = int(input('Dignorar 3ª número '))
print('-'*70)

for c in range(inicio, fim):
    if (c == ignorar1 or c == ignorar2 or c == ignorar3):
        continue
    else:
        
        print(f'{c}', end=' ')

print('\n' + '='*70) # /n para saltar linha
print(f' Os número {ignorar1}, {ignorar2} e {ignorar3} foram ignorados!')
print('Fim do programa!')
print('-'*70)