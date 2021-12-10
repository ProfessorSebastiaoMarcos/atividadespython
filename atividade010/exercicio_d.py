#Curso Técnico de Informática
#Autor: Sebastião Marcos
#Data início: 01/11/2021
#Término: 01/11/2021
#Atividade010: exercício_d.py

import os
os.system('cls')

# Declarar meu dicionário
d_cores = {1: 'Azul', 2: 'Marrom', 3: 'Branca', 4: 'Amarelo', 5: 'Verde'}

print('-'*70)
# Varrendo o dicionário
for chave, valor in d_cores.items():
    print(f'{chave}: {valor}')
print('-'*70)