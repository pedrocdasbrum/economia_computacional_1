"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados
Autor: Pedro Brum
Versão: 0.0.3
Correções realizadas: 
- Informação mais intuitiva ao usuário da posição em que seu cpf foi encontrado
- Informação mais precisa de que o valor procurado é um cpf
Data: 19/04/2024
"""

# Alocação de memória

lista = []

achou = False

posicao = 0

# Leitura da base de dados de cpf

base = [1, 5, 2, 87, 31]

lista = base

# Leitura de dados

cpf = int(input("\nDigite o CPF a procurar: "))

# Processamento de dados

while posicao < len(lista):
    if lista[posicao] == cpf:
        achou = True
        break
    posicao += 1 # é a mesma coisa que posicao + 1

# Saída de dados

if achou:
    print(f"\nO CPF {cpf} foi encontrado na posição {posicao + 1}")
else:
    print(f"\nO CPF {cpf} não foi encontrado!")