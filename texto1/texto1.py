def mostrar_menu():
    print("Escriba 1 para pasar a minúsculas,")
    print(">         2 para pasar a mayúsculas, ")
    print(">         3 para invertir mayúsculas y minúsculas ")
    print(">         4 para pasar a capitalización.")
    print(">         5 para pasar a titulación.")
    print(">         6 para reemplazar espacios por guiones bajos.")
    print(">         7 para salir.")

def main():
    texto = input("Ingrese la línea de texto:\n< ")

    while True:
        mostrar_menu()
        opcion = input("< ")

        if opcion == "1":
            texto = texto.lower()
            print("Resultado:", texto)
        elif opcion == "2":
            texto = texto.upper()
            print("Resultado:", texto)
        elif opcion == "3":
            texto = texto.swapcase()
            print("Resultado:", texto)
        elif opcion == "4":
            texto = texto.capitalize()
            print("Resultado:", texto)
        elif opcion == "5":
            texto = texto.title()
            print("Resultado:", texto)
        elif opcion == "6":
            texto = texto.replace(" ", "_")
            print("Resultado:", texto)
        elif opcion == "7":
            print("Gracias!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
