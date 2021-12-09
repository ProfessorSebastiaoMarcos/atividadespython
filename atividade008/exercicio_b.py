
# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_b.py

# Crie uma lista com 5 números inteiros. 
# Depois imprima a soma desses valores.

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Somando números')
print('='*70)

listaInteiros = []
soma = 0

for c in range(0, 5):
    numero = int(input('Digite um número inteiro: '))
    listaInteiros.append(numero)
    soma += numero

#Saída
print('Numeros inteiros: ', end=' ')
for i, numero in enumerate(listaInteiros):
    print(f'{numero}', end=' ')
print()
print(f'A soma dos números é: {soma}')
print('-'*70)

print('Fim do Programa!')
print()


