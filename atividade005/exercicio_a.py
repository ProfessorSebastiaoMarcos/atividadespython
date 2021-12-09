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
print('CALCULANDO A RAIZ QUADRADA COM FUNÇÃO')
print('=' * 50)

# Declaração
resposta = 0

# Entrada de dados
print()
numero = int(input('Entre com um número: '))

# Validando a entrada
if (numero == 0):
    print('-' * 50)
    print('Não pode encontrar raiz de 0!')
elif (numero < 0):
    print('-' * 50)
    print('O resultado será um número complexo!')
else:

    #Cálculo da raiz quadrada
    raizQuadrada = math.sqrt(numero)

    # Calculando a Raiz Quadrada
    if (raizQuadrada % 2 != 0):
        math.ceil(raizQuadrada)
        resposta = raizQuadrada
    else:
        resposta = raizQuadrada

    # Saída
    print('-' * 50)
    print(f'A raiz quadrada de {numero} é: {resposta:.2f}')

# Saída
print('Fim do programa!')
print('-' * 50)
print()