'''Faça um programa que peça a velocidade de um carro. 
Se o carro ultrapassar o limite de 60Km por hora, mostre na 
tela a mensagem: ‘Limite de velocidade acima do permitido’. 
Se a velocidade estiver a abaixo dos 60Km, mostrar a 
frase: ‘Velocidade normal! A velocidade não pode ser negativa.'''

import os
os.system('cls')

print('-'*50)
print('PROGRAMA QUE VERIFICA VELOCIDADE MÁXIMA')
print('='*50)
print()

#Entrada de dados
velocidade = int(input('Digite a velocidade do veículo: '))

#Cálculos e condicionais
if (velocidade < 0):
    print('• Vecolidade não pode ser negativa!')
elif (velocidade > 60):
    print('• Limite de velocidade acima do permitido!')
else:
    print('• Velocidade normal!')
print()
print('-'*50)