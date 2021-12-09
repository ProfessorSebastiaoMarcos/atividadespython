# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 23/11/2021
# Término: 29/11/2021
# Atividade008: exercicio_g.py

# Ler uma lista com 10 números, 
# depois apresente o maior e o menor número da lista


# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

print('-'*70)
print('Vogais na ordem inversa')
print('='*70)

# Declarando variáveis
lista = []
maior = 0
menor = 0

# criar um laço para pegar os numeros
for c in range(0, 3):
    numero = int(input(f'Digite {c+1}º número: '))
    lista.append(numero)

    if c == 0:
        maior = menor = lista[c] # 1º número digitado
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
        
#Saída        
print('-'*60)
print('Números: ', end='')
for i, numero in enumerate(lista):
    print(f'{numero}', end=' ')
    
print()
print(f'{maior} é o maior número!')
print(f'{menor} é o menor número!')
print('-'*60)




