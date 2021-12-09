# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 22/11/2021
# Término: 22/11/2021
# Exercício_g

'''
Faça um programa para somar os números primos em um intervalo pré-determinado pelo usuário.

'''

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*70)
print('For Range, número primo')
print('='*70)

# Declaração
#limite = 100

#Entrada de dados
inicio = int(input('Digite o inicio do intervalo: '))
fim = int(input('Digite o inicio do intervalo: '))
quantidadePrimos = 0
somaPrimos = 0
print('-'*70)

# Validação
if (inicio < 0 or fim < 0):
    print('-'*70)
    print('Entrada inválida')
else:

    # Estrutura de repetição
    for c in range(inicio, fim + 1):
        divisores = 0

        for j in range(1, c+1):

            if(c % j == 0):
                divisores = divisores + 1
                
        if (divisores == 2):
            
            # Soma quantidade de números primos
            quantidadePrimos += 1

            # Soma os números primos
            somaPrimos += c            
            print(c, end=' ')
    print()
    print('-'*70)
    print(f'Quantidade de números primos: {quantidadePrimos}')
    print(f'Soma de números primos: {somaPrimos}')
    print('='*70)
print('='*70)
print('Fim do programa!')