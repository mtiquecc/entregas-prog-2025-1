#!/usr/bin/env python3

"""
Título de práctica: Calculadora en Python

Descripción extendida del programa: Esta calculadora permite realizar operaciones básicas como suma, resta, multiplicación y división.

Autor: ElAutor <el@correo>
Fecha: 2025-02-01
"""

# **** En esta región puede importar los módulos necesarios para su programa
# **** O las definiciones de clases y/o funciones que requiera.

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

def run():
    """script entrypoint"""
    # **** Poner el código ejecutable de su ejercicio aquí
    
    # Saludo
    print("Hola mundo!")
    
    while True:
        print("\nCalculadora - Elige una opción:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = input("Introduce el número de la operación: ")
        
        if opcion == '5':
            print("Saliendo de la calculadora...")
            break
        
        if opcion in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                
                if opcion == '1':
                    print(f"Resultado: {suma(num1, num2)}")
                elif opcion == '2':
                    print(f"Resultado: {resta(num1, num2)}")
                elif opcion == '3':
                    print(f"Resultado: {multiplicacion(num1, num2)}")
                elif opcion == '4':
                    print(f"Resultado: {division(num1, num2)}")
            except ValueError:
                print("Error: Ingresa valores numéricos válidos.")
        else:
            print("Opción no válida, intenta de nuevo.")

# **** Conserve este condicional para ejecutar el programa directamente
if __name__ == "__main__":
    run()
    