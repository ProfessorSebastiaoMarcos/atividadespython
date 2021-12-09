#Curso Técnico de Informática
#Autor: Sebastião Marcos
#Data início: 08/12/2021
#Término: 08/12/2021
#Atividade 010: exercicio_a.py

import os


os.system('cls')

# declarar minha variável
nomes = {'nome': 'John', 'idade': 40, 'peso': 80, 'altura': 1.70}

print('-'*60)
print('Nome \tIdade \tPeso \tAltura')
print('='*60)

# Varrer o Dicionário
for valor in nomes.values():
    print(f'{valor}', end='\t')
print()
print('-'*60)