# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
#Atividade011: exercício_g.py

'''
Uma Academia deseja fazer um senso entre seus clientes para 
descobrir a média de altura  e peso de seus clientes. 
Faça um programa que pergunte a cada um dos clientes da academia 
seu código, nome, altura e peso. Informe ao usuário se ele deseja 
continuar, após a sequência de entrada. Se a resposta for negativa,
o programa deverá listar os dados dos clientes e a média. 

'''

import os

os.system('cls')

dicionario = {}
lista = []

while True:

    dicionario['codigo'] = str(input('Entre com o código: '))
    dicionario['nome'] = str(input('Entre com o nome: '))
    dicionario['altura'] = float(input('Entre com a altura: '))
    dicionario['peso'] = float(input('Entre com o peso: '))

    lista.append(dicionario.copy())

    continuar = str(input('Deseja continuar (s/n)? ')).lower()
    if continuar == 's':
        continue
    else:
        
        print('Programa finalizado!')
        print('Código\tNome\tAltura\tPeso')
        for nome in lista:            
            for chave, valor in nome.items():
                print(f'{valor}', end='\t')
            print()
    break

