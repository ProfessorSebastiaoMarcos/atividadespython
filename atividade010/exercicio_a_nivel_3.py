#Curso Técnico de Informática
#Autor: Sebastião Marcos
#Data início: 08/12/2021
#Término: 08/12/2021
#Atividade 010: exercicio_a.py

import os


os.system('cls')

# Declarar as variáveis
dicionario = {}
lista = []

# Criando o dicionário e iterando com o for
for c in range(0, 2):
    dicionario['nome'] = str(input('Digite um nome: '))
    dicionario['idade'] = int(input('Digite sua idade: '))
    dicionario['peso'] = float(input('Informe o seu peso: '))
    dicionario['altura'] = float(input('Informe a altura: '))

    # Armazenar na minha lista lista
    lista.append(dicionario.copy())

# Limpar a tela
os.system('cls')

# Saída de Dados
print('-'*35)
print('Nome \tIdade \tPeso \tAltura')
print('='*35)

# varrer a lista para pegar a quantidade de elementos
for pessoa in lista:
    # varrendo o dicionário
    for valor in pessoa.values():
        print(f'{valor}', end='\t')
    print() # Pular de linha para outro registro
print('-'*35)
print('-'*35)