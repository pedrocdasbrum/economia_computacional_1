"""
Programa de Cálculo de Média
Autor: Pedro Brum
Descrição: calcular uma média em paradigma de programação estruturada
Data: 05/04/2024
Versão: 0.0.1
"""

# Alocação de memória

soma: float = 0

valor: float = 0

i: int = 0

num_val: int = 0

# Entrada e processamento de dados

num_val = int(input("\nQual o número de valores? "))

while i < num_val:
    valor = float(input("Insira um valor: "))
    soma = soma + valor
    i = i + 1
    media = soma / num_val

# Saída de dados

print(f"A média dos valores é: {media}")