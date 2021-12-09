'''
Faça um programa que calcule a equação do 2º grau da seguinte 
expressão matemática x² - 6x + 5. As raízes são {5, 1}. 
Esse cálculo deverá ser feito sem ajuda de funções ou métodos. 
Somente utilizando o que foi aprendido até o momento.

'''

import os
os.system('cls')

print('-'*50)
print('PROGRAMA PARA CALCULAR A EQUAÇÃO x² - 6x + 5  ')
print('='*50)
print()

#Entrada de dados
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "a": '))
c = int(input('Informe o valor de "c": '))

#Calculando o Delta
delta = (b ** 2) - (4 * a * c)

#Calculando as Raízes
x1 = ((-b) + (delta ** (1/2))) / 2*a
x2 = ((-b) - (delta ** (1/2))) / 2*a

#Saída
print(f'As raízes da equação são ({x1}, {x2}) ')
print('='*50)
print()
