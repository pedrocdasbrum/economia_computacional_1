"""
Programa Temperatura
Descrição: O problema é desenvolver um programa que pergunte a temperatura do ambiente. Se ela for menor ou igual a 18 graus Celsius, imprimir uma mensagem de que está frio. Se ela estiver de 18 a 28 graus Celsius, imprimir que está agradável. Se estiver mais do que 28 graus Celsius, imprimir que está quente
Autor: Pedro Brum
Data: 12/04/2024
Versão: 0.0.1
"""

# Alocação de memória

temp: int = 0

# Entrada de dados

temp = int(input("\nQual a temperatura do seu ambiente? "))

# Processamento e saída de dados

if temp <= 18:
    print("\nEntão a temperatura está fria!")
elif 18 <= temp <= 28:
    print("\nEntão a temperatura está agradável!")
else:
    print("\nEntão a temperatura está quente!")