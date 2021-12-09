# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_a

'''
Evolua o programa no qual imprimimos os números no 
intervalo entre 1 - 100 utilizando a pergunta para usuário: 
Qual o valor do intervalo?

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('Imprimir os números de 0 a 100')
print('='*70)

inicio = int(input('Início do intervalo: '))
fim = int(input('Fim do intervalo: '))

if (inicio < 0 or fim < 0):
    print('Entrada inválida!')
else:
    for c in range(inicio, fim + 1):
        print(c, end=' ')

print()    
print('-'*70)
print('Fim do programa')
print('-'*70)