"""
Programa Soma
Descrição: Este programa lê dois números inteiros digitados pelo usuário e põe na tela a soma deles
Autor: Pedro Brum
Data: 12/04/2024
Versão: 0.0.2
"""

# Alocação de memória

i: int = 0

numero: int = 0

soma: int = 0

# Entrada de dados e processamento de dados

while i < 2:
    numero = int(input(f"\nDigite a parcela {i + 1}: "))
    soma = soma + numero
    i += 1

# Saída de dados

print(f"\nA soma dos números digitados é igual a {soma}")