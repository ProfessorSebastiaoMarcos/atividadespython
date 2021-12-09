'''
Faça um programa que peça para o usuário a distância de uma 
viagem de Juiz de Fora a São Paulo. Calcule o preço da passagem 
sabendo que a empresa de ônibus cobra R$0,70 por km, em viagens de até 200Km. 
Acima dessa distância às viagens passam a custar R$0,40.

'''

import os
os.system('cls')

print('-'*50)
print('PROGRAMA PARA CALCULAR PASSAGEM')
print('='*50)
print()

#Entrada de dados
km = float(input('informe a distância em Km: '))

#Cálculos e condicionais
preco1 = km * .70
preco2 = km * .40

if (km > 0 and km <= 200):
    print(f'Sua passagem vair custar R${preco1:.2f}')
elif (km > 200):
    print(f'Sua passagem vai custar R${preco2:.2f}')
else:
    print('Km inválido!')

print()
print('-'*50)