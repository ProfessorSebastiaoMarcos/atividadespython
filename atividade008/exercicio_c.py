
# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_c.py

# Faça um programa que procure na lista 
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e 
# produza:
# • O intervalo de 1 até 9
# • O intervalo de 8 até 13
# • Os números pares
# • Os números ímpares
# • Os múltiplos de 2, 3 e 4
# • Lista reversa
# • O produto dos intervalos 5-6 por 11-12


# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Fatiamento e cálculos com listas')
print('='*70)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#Intervalo de 1 até 9
lista1 = numeros[0:9]
print(f'1ª Lista: {lista1}')

#Intervalo de 8 até 13
lista2 = numeros[7:13]
print(f'2ª Lista: {lista2}')

#Intervalo de números pares
lista3 = numeros[1:15:2]
print(f'3ª Lista: {lista3}')

#Intervalo de numeros ímpares
lista4 = numeros[0::2]
print(f'4ª Lista: {lista4}')

#Múltiplos de 2, 3 e 4
lista5a = numeros[1::2]
print(f'5ª Lista A:  Multiplos de 2: {lista5a}')
lista5b = numeros[2::3]
print(f'5ª Lista B:  Multiplos de 3: {lista5b}')
lista5c = numeros[3::4]
print(f'5ª Lista C:  Multiplos de 4: {lista5c}')

# Lista Reversa
numeros.reverse()
lista6 = numeros
print(f'6ª Lista Reversa: {lista6}')

# Lista Produto dos indices 5-6 por 11-12
lista7 = [numeros[5]*numeros[11], numeros[6]*numeros[12]]
print(f'7ª Lista: {lista7}')

