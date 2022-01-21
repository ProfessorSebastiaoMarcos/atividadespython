# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 00-02-2022
# Término: 00-02-2022
#Atividade011: exercício_g.py

'''
Crie um programa que peça ao usuário 2 números maiores que 0 e 
menores que 11. Depois mostre um menu com as seguintes operações:

1. Soma
2. Subtração 
3. Produto
4. Divisão
4. Divisão inteira
6. Resto da divisão

O usuário deverá escolher um numero maior igual a 1 e menor igual a 6. 
Em seguida você criará funções que retornem os resultados das operações, 
imprimindo seus resultados.

'''

import os

os.system('cls')


def calculos(numero_1, numero_2, escolha):
    if escolha == 1:
        soma = numero_1 + numero_2
        return '+', soma

    elif escolha == 2:
        subtracao = numero_1 - numero_2
        return '-', subtracao

    elif escolha == 3:
        produto = numero_1 * numero_2
        return '×', produto

    elif escolha == 4:
        if numero_2 == 0:
            return '÷', 'Impossível dividir por zero!'
        else:
            divisao = numero_1 / numero_2
            return '÷', divisao

    elif escolha == 5:
        if numero_2 == 0:
            return '//', 'Impossível dividir por zero!'
        else:
            divisao_inteira = numero_1 // numero_2
            return '//', divisao_inteira

    elif escolha == 6:
        if numero_2 == 0:
            return '%', 'Impossível dividir por zero!'
        else:
            resto_divisao = numero_1 % numero_2
            return '%', resto_divisao

while True:

    print('''
        1. Soma
        2. Subtração 
        3. Produto
        4. Divisão
        5. Divisão inteira
        6. Resto da divisão
        7. Sair
    ''')

    try:        
        escolha = int(input('Escolha uma operação (1-7): '))

        if escolha == 7:
            break

        else:
            
            numero_1 = float(input('Entre com o 1º número: '))
            numero_2 = float(input('Entre com o 2º número: '))
            
            operdador, resultado = calculos(numero_1, numero_2, escolha)

            print('-'*70)
            print(f'O Resultado de' +
                f' {numero_1} {operdador} {numero_2} é igual a: {resultado}')
            print('-'*70)
            print()

    except (ValueError, TypeError):
        print('Valor inválido!')
