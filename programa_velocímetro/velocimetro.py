"""
Programa Velocímetro
Descrição: O problema é desenvolver um programa que pergunte a velocidade do carro do usuário. Caso ele ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Neste caso, exiba o valor da multa, cobrando R$ 5,00 por km acima de 80km/h
Autor: Pedro Brum
Data: 12/04/2024
Versão: 0.0.4
"""

# Alocação de memória

vel_car: int = 0

warning = 0

mul: int = 0

# Entrada de dados

vel_car = int(input("\nSeu carro está em qual velocidade? "))

# Processamento e saída de dados

if vel_car > 80:
    mul = vel_car * 5
    warning = print(f"\nVocê foi multado! Pague a multa em R${mul},00!")
else:
    warning = print("\nVocê está dentro do limite de velocidade!")