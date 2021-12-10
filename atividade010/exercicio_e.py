#Curso Técnico de Informática
#Autor: Sebastião Marcos
#Data início: 01/11/2021
#Término: 01/11/2021
#Atividade010: exercício_e.py

import os
os.system('cls')

# Declarando o dicionário
d_ferramentas = {1: 'Chave inglesa', 2: 'enxada', 3: 'cavadeira', 4: 'espátula', 5: 'trena'}

# imprimindo chaves e valores
for chave, valor in d_ferramentas.items():
    print(f'{chave}: {valor}')

# Quantidade de itens
qtd_itens = len(d_ferramentas)
print('-'*60)
print(f'Quantidade de itens {qtd_itens}')
print('-'*60)