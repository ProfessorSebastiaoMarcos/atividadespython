# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_e

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('CONTANDO VOGAIS')
print('='*50)

frase = str(input('Digite uma frase: ')).lower()

a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')

vogais = a + e + i + o + u

#Saída
print(f'A vogal "a" aparece {a} vezes')
print(f'A vogal "e" aparece {e} vezes')
print(f'A vogal "i" aparece {i} vezes')
print(f'A vogal "o" aparece {o} vezes')
print(f'A vogal "u" aparece {u} vezes')
print('-'*50)
print(f'Quantidade de vogais na frase: {vogais} vogais')