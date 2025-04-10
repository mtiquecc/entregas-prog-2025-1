#!/usr/bin/env python3

"""
Título de práctica: Calculadora en Python

Descripción extendida del programa: Esta calculadora permite realizar operaciones matemáticas básicas y avanzadas, incluyendo suma, resta, multiplicación, división, potenciación, división entera y módulo.

Autor: ElAutor <el@correo>
Fecha: 2025-02-01
"""

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potenciacion(a, b):
    return a ** b

def division_entera(a, b):
    if b != 0:
        return a // b
    else:
        return "Error: División por cero"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: División por cero"

def obtener_numero(mensaje):
    valor = input(mensaje)
    if valor == "":
        print("> Operación cancelada")
        return None
    if valor.replace('.', '', 1).replace('-', '', 1).isdigit():
        return float(valor)
    else:
        print("> Dato inválido, solo se permiten números.")
        return None

def run():
    """script entrypoint"""
    print("Hola mundo!")

    while True:
        print("> Escriba 1 para suma, \n>         2 para resta, \n>         3 para multiplicación \n>         4 para división.\n>         5 para potenciación.\n>         6 para división entera.\n>         7 para módulo.\n>         8 para salir.")
        opcion = input("< ")

        if opcion == '8':
            print("> Gracias!")
            break

        if opcion in ('1', '2', '3', '4', '5', '6', '7'):
            num1 = obtener_numero("> Ingrese el operando A (vacío para cancelar):\n< ")
            if num1 is None:
                continue

            num2 = obtener_numero("> Ingrese el operando B (vacío para cancelar):\n< ")
            if num2 is None:
                continue

            if opcion == '1':
                print(f"> El resultado de la suma es: {suma(num1, num2)}")
            elif opcion == '2':
                print(f"> El resultado de la resta es: {resta(num1, num2)}")
            elif opcion == '3':
                print(f"> El resultado de la multiplicación es: {multiplicacion(num1, num2)}")
            elif opcion == '4':
                print(f"> El resultado de la división es: {division(num1, num2)}")
            elif opcion == '5':
                print(f"> El resultado de la potenciación es: {potenciacion(num1, num2)}")
            elif opcion == '6':
                print(f"> El resultado de la división entera es: {division_entera(num1, num2)}")
            elif opcion == '7':
                print(f"> El resultado del módulo es: {modulo(num1, num2)}")
        else:
            print("> Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    run()
