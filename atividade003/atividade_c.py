#Curso Técnico de Informática
#Autor: Sebastião Marcos
#Data início: 01/11/2021
#Término: 01/11/2021
#Atividade 003 - Exercício c

#Entrada de dados
nota1 = float(input('Entre com a 1ª nota: '))
nota2 = float(input('Entre com a 2ª nota: '))
nota3 = float(input('Entre com a 3ª nota: '))
nota4 = float(input('Entra com a 4ª nota: '))

#Cálculo
somaNotas = nota1 + nota2 + nota3 + nota4
media =  somaNotas / 4

#Saída
print('-'*40)
print('CÁLCULO DA MÉDIA')
print('='*40)
print(f'A soma das notas das notas é: {somaNotas}')
print(f'A média é: {media}')
print('-'*40)

