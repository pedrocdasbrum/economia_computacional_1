"""
Programa Soma
Descrição: Este programa lê dois números inteiros digitados pelo usuário e põe na tela a soma deles
Autor: Pedro Brum
Data: 12/04/2024
Versão: 0.0.1
"""

# Alocação de memória

numero_1: int = 0

numero_2: int = 0

soma: int = 0

# Entrada de dados

numero_1 = int(input("\nQual é o primeiro número? "))

numero_2 = int(input("\nQual é o segundo número? "))

# Processamento de dados

soma = numero_1 + numero_2

# Saída de dados

print(soma)