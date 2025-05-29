from datetime import datetime, timedelta

def mostrar_menu():
    print("La fecha actual es:", datetime.now())
    print("Escriba 1 para ingresar segundos,")
    print(">         2 para ingresar días,")
    print(">         3 para salir.")

def main():
    while True:
        mostrar_menu()
        opcion = input("< ")

        if opcion == "1":
            try:
                segundos = int(input("Escriba la cantidad de segundos\n< "))
                nueva_fecha = datetime.now() + timedelta(seconds=segundos)
                print("La nueva fecha es:", nueva_fecha)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == "2":
            try:
                dias = int(input("Escriba la cantidad de días\n< "))
                nueva_fecha = datetime.now() + timedelta(days=dias)
                print("La nueva fecha es:", nueva_fecha)
            except ValueError:
                print("Por favor ingrese un número válido.")
        elif opcion == "3":
            print("Gracias!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
