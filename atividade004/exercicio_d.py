'''Faça um programa que calcule um aumento salarial de um funcionário. 
Se o salário for maior que R$1500,00, efetuar um aumento de 5%; 
Se o salário for menor que R$1000,00, efetuar um aumento de 10%. 
O salário não pode ser 0 ou menor.
'''

import os
os.system('cls')

print('-'*50)
print('PROGRAMA PARA AUMENTO SALARIAL')
print('='*50)
print()

#Entrada de dados
salario = float(input('Informe o valor do salário R$'))

#Cálculos e condicionais
aumento1 = salario + (salario * .10)
aumento2 = salario + (salario * .05)

if (salario <= 0):
    print('• Salário inválido!')
elif (salario > 0 and salario <= 1000):
    print (f'• Salário atual R${salario}')
    print(f'• Salário com aumento de 10% R${aumento1}')
elif (salario > 1500):
    print (f'• Salário atual R${salario}')
    print(f'• Salário com aumento de 5% R${aumento2}')
else:
    ('• Salário Inválido!')
print()
print('-'*50)