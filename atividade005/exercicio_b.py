# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 10/11/2021
# Exercício_a: Raíz quadrada

# Importando as bibliotecas
import os
import math


# Limpando o terminal
os.system('cls')

# Título
print('-' * 50)
print('CALCULANDO DIVISÃO COM ARREDONDAMENTO: FUNÇÃO')
print('=' * 50)

# Declaração
arredondarCima = 0
arredondarBaixo = 0

numerador = int(input('Entre com o 1º valor: '))
denominador = int(input('Entre com o 2º valor: '))
print('-' * 50)

# Condicional e Validação
if (numerador == 0):
    # Saída
    print(f'A divisão de {numerador} por {denominador} é: {numerador}')

elif (denominador == 0):
    # Saída
    print('-' * 50)
    print('Não existe divisão por 0!')

else:
    # Cálculo
    divisao = numerador / denominador

    # Condicional
    if (divisao % 2 == 0):
        print(f'A divisão de {numerador} por {denominador} é: {divisao}')
    else:
        # Cálculo
        arredondarCima = math.ceil(divisao)
        arredondarBaixo = math.floor(divisao)

        # Saída
        print('-' * 50)
        print(f'A divisão de {numerador} por {denominador}' +
              f' arredondado para cima é: {arredondarCima}')
        print(f'A divisão de {numerador} por {denominador}' +
              f' arredondado para baixo é: {arredondarBaixo}')
        print('-' * 50)
    
print('Fim do Programama!')
print('-' * 50)