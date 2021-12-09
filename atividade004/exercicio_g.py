'''
Faça um programa que calcule a formação de um triângulo. 
Para isso, o programa deverá receber a medida de 3 segmentos e, 
em seguida, compará-los. A resposta dessa comparação deverá ser: 
‘Forma um triângulo’ e ‘não forma um triângulo’. 
Os valores não pode ser 0 ou menor.

| b - c | < a < b + c, seja a < b + c
| a - c | < b < a + c, ou seja b < a + c
| a - b | < c < a + b, ou seja c < a + b

'''

import os
os.system('cls')

print('-'*50)
print('PROGRAMA PARA CALCULAR EXISTÊNCIA DE UM TRIÂNGULO')
print('='*50)
print()

#Entrada de dados
a = int(input('informe o segmento "a":  '))
b = int(input('informe o segmento "b":  '))
c = int(input('informe o segmento "c":  '))

#Cálculos e condicionais
if (a <= 0 or b <= 0 or c <= 0):
    print('Valor de segmento inválido!')
elif ((a < (b + c)) and (b < (a + c)) and (c < (a + b))):
    print(f'{a} + {b} + {c}, formam um triângulo')
else: 
    print(f'{a} + {b} + {c}, não formam um triângulo')

print()
print('-'*50)