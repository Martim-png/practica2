
CantidadChefs = 0

while CantidadChefs <= 0:
    try:
        CantidadChefs = int(input("¿Cuántos chefs desea registrar?: "))
    except ValueError:
        print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")
    else:
        if CantidadChefs <= 0:
            print("¡Ingrediente inválido! Ingresa un entero positivo para continuar el registro.")

ChefsMaestro = 0
ChefsAprendiz = 0

for Chef in range(1, CantidadChefs + 1):
    print(f"--- Chef N°{Chef} ---")

    CodigoCulinario = input("Ingrese el código culinario: ")

    while len(CodigoCulinario) < 8 or " " in CodigoCulinario:
        print("Código inválido. Debe tener al menos 8 caracteres y no contener espacios.")
        CodigoCulinario = input("Ingrese el código culinario: ")

    Experiencia = 0

    while Experiencia <= 0:
        try:
            Experiencia = int(input("Ingrese años de experiencia culinaria: "))
        except ValueError:
            print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")
        else:
            if Experiencia <= 0:
                print("¡Error gastronómico! Ingresa un número entero positivo para la experiencia culinaria.")

    if Experiencia > 5:
        ChefsMaestro += 1
    else:
        ChefsAprendiz += 1

print(f"¡La escuela cuenta con {ChefsMaestro} Chefs Maestros y {ChefsAprendiz} Chefs Aprendices! ¡A cocinar!")
