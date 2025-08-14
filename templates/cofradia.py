def Funciones(Opciones):
    match Opciones:
        case 1:
            print("registrar juego nuevo ")
        case 2:
            print("eliminar un juego")
        case 3:
            print("Lista de juegos")
        case 4:
            print("Prestamo de juegos ")
        case 5:
            print("Registro de prestamos")
        case 6:
            print("Buscar juego")
        case _:
            print("Opcion no valida")
print("Bienvenido a la Cofradia de los Jugadores")
while True:
    print("Menu de opciones")
    print("1. Registrar juego nuevo")
    print("2. Eliminar un juego")
    print("3. Lista de juegos")
    print("4. Prestamo de juegos")
    print("5. Registro de prestamos")
    print("6. Buscar juego")
    print("7. Salir")
    try:
        opciones = int(input("Seleccione una opcion: "))
        if opciones == 7:
            break
        Funciones(opciones)
    except ValueError:
        print("Por favor, ingrese un numero valido.")