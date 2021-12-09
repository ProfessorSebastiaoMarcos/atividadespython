
# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_e.py

# Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Vogais na ordem inversa')
print('='*70)

# Declarando variáveis
vogais = []

for c in range(0, 5):

    # Também podemos inserir dados dessa forma
    vogais.append(str(input('Digite uma vogal: ')))

# Imprimir ordem normal
print('-'*70)
print('Vogais: ', end=' ')
for i, vogal in enumerate(vogais):
    print(f'{vogal}', end=' ')

# Inverter vogais
print()
vogais.reverse()
vogaisInversa = vogais

# Saída em ordem inversa
print(f'Ordem inversa: ', end=' ')
for i, vogal in enumerate(vogaisInversa):
    print(f'{vogal}', end=' ')
print()
print('-'*70)




