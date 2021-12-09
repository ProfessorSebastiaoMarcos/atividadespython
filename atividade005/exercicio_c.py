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
print('CALCULANDO POTÊNCIA COM FUNÇÃO')
print('=' * 50)

# Declarações
resposta = ''
potencia = 0

# Entrada de Dados
base = int(input('Informe o valor da base: '))
expoente = int(input('Informe o expoente: '))

# Validação
if (base == 1):
    resposta = 'Base igual a 1, resultado é igual a base!'

elif (expoente == 0):
    resposta = 'Expoente igual a 0, resultado é igual a 1!'

elif (base == 0):
    resposta = 'Base igual a 0, resultado é igual a 0!'

else:
    # Cálculo
    potencia = math.pow(base, expoente)

    # Saída
    print('-' * 50)
    print(f'O número {base} elevado a {expoente} é igual a: {potencia}')

# Saída
print('-' * 50)
print(resposta)
print('Fim do Programa!')
print('-' * 50)
