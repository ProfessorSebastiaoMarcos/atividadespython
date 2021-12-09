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
print('CALCULANDO SENO/COSSENO/TANGENTE COM FUNÇÃO')
print('=' * 50)

#Entrada de dados
angulo = int(input('Informe o angulo: '))

#Cálculo
seno = math.sin(math.radians(angulo))
cosseso = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

#Saída
print('-' * 50)
print(f'O seno de {angulo}º é: {seno:.2f}')
print(f'O cosseno de {angulo}º é: {cosseso:.2f}')
print(f'O seno de {angulo}º é: {tangente:.2f}')
print('-' * 50)
print()