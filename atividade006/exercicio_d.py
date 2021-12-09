# Curso Técnico de Informática
# Autor: Sebastião Marcos
# Data início: 10/11/2021
# Término: 16/11/2021
# Exercício_d

# Importando as bibliotecas
import os


# Limpando o terminal
os.system('cls')

# Título
print('-'*50)
print('CONVERSÕES EM FRASE')
print('-'*50)

frase = str(input('Entre com uma frase: '))

minusculo = frase.lower()
maiusculo = frase.upper()
quantCaractere = len(frase)
fraseQuebrada = frase.split()
quantidadeCacactereSegundaFrase = len(fraseQuebrada[1])


print(f'A frase em minúsculo: {minusculo}')
print(f'A frase em minúsculo: {maiusculo}')
print(f'A frase tem {quantCaractere} caracteres')
print(f'A segunda palavra é {fraseQuebrada} e ela tem {quantidadeCacactereSegundaFrase} caracteres')
print()
print('-'*50)