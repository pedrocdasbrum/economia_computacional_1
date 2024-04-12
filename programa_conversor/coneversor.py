"""
Programa Conversor
Descrição: O problema é desenvolver um programa que leia um valor em metros e o converta para milímetros
Autor: Pedro Brum
Data: 12/04/2024
Versão: 0.0.4
"""

# Alocação de memória

value: int = 0

mil = 0

# Entrada de dados

value = int(input("\nInsira um valor em metro: "))

# Processamento de dados

mil = value * 1000

# Saída de dados

print(f"\nEste metro em milímetros é: {mil}mm")