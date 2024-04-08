"""Archivo editado"""
import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def main():
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    print("El área del círculo es:", area)

if __name__ == "__main__":
    main()
