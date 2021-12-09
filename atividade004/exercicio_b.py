#Faça um programa que peça ao usuário 3 números. 
#Depois, mostre na tela qual é o maior e o menor número.

import os
os.system('cls')

a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

print()
if( a > b and a > c):
    print(f'O número {a} é o maior')
elif( b > c and b > a):
    print(f'O número {b} é o maior')
else:
    print(f'O número {c} é o maior')

print()
if (a < b and a < c):
    print(f'O número {a} é o menor')
elif (b < c and b < a):
    print(f'O número {b} é o menor')
else:
    print(f'O número {c} é o menor')

print()