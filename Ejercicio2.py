
Historial = 0
CamarotesDisponibles = 120
CamarotesMax = 90

print("¡Bienvenido al sistema de gestión de camarotes del Crucero Atlántico!")

while True:
    print("\n --- MENÚ PRINCIPAL ---")
    print("1. Camarotes disponibles")
    print("2. Reservar camarote")
    print("3. Cancelar camarote")
    print("4. Historial de reservas")
    print("5. Salir")

    try:
        Opcion = int(input("Ingrese una opción: "))
    except ValueError:
        print("Error: La opción debe ser un número")
        continue

    match Opcion:

        case 1:
            print(f"Hay {CamarotesDisponibles} camarotes disponibles")

        case 2:
            while True:
                try:
                    Reservas = int(input("¿Cuántos camarotes desea reservar?: "))
                except ValueError:
                    print("¡Error! Ingrese solo números enteros positivos")
                else:
                    if CamarotesDisponibles > 0:
                        if Reservas > 0 and Reservas <= CamarotesDisponibles:
                            CamarotesDisponibles -= Reservas
                            Historial += Reservas
                            print("Reserva realizada con éxito")
                            break
                        else:
                            print("La cantidad debe ser mayor a 0 y no superar los camarotes disponibles")
                    else:
                        print("No hay camarotes disponibles")

        case 3:
            while True:
                try:
                    Liberar = int(input("¿Cuántos camarotes desea cancelar?: "))
                except ValueError:
                    print("Error, solo debe ingresar números enteros positivos")
                else:
                    if Liberar > 0 and Liberar <= CamarotesMax and Liberar <= Historial:
                        CamarotesDisponibles += Liberar
                        Historial -= Liberar
                        print("Cancelación realizada con éxito")
                        break
                    else:
                        print("La cantidad debe ser mayor a 0, no superar 90 y no superar las reservas existentes")

        case 4:
            print(f"Cantidad de reservas vigentes: {Historial}")

        case 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break

        case _:
            print("Opción incorrecta")
