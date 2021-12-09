'''
Faça um programa que peça ao usuário um ano aleatório. 
Depois, mostre na tela se o ano é bissexto. 
Faça a validação de entrada de dados para valores menores ou iguais a 0.

Para ser bissexto, o ano deve ser:

Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.

'''

import os
os.system('cls')

print('-'*50)
print('PROGRAMA PARA CALCULAR ANO BISSEXTO')
print('='*50)
print()

#Entrada de dados
ano = int(input('Infor uma ano qualquer: '))

#Cálculos e condicionais
if (ano <= 0):
    print('ano inválido!')
elif (ano % 4 == 0 and ano % 100 != 0 ) or (ano % 400 == 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')

print()
print('-'*50)