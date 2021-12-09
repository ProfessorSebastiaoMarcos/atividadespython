# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_i

'''
Faça um programa que imprima a frase "estou em looping" e, 
em seguida, solicite ao usuário uma letra. Caso a letra seja o 
“f" finalize a aplicação. Do contrário, imprima novamente a mesma 
frase até que o caractere “f" seja enviado.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('Estou em um looping...')
print('='*70)

while (True):
    
    entrada = input('Digite "f" para sair: ').lower()

    if (entrada != 'f'):
        print('Ainda estou em looping...')
    else:
        break


print('-'*70)
print('Fim do programa!')
print('-'*70)
