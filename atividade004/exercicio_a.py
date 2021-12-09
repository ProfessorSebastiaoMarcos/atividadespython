import os
os.system('cls')

#Faça um programa que peça um número inteiro com validação para números decimais. 
#Depois verifique se esse número é par ou se ele é ímpar.

numero = int(input('Digite um número inteiro: '))

if (numero % 2 == 0):
    print(f'O número {numero} é par!')
else: 
    print(f'O número {numero} é ímpar')