import numpy as np

dias = 1
actividades = []

print("\n Hola, Bienvenido a tu tracker personalizado de tus habitos diarios. \n")

while True:
    print("="*100)
    print("MENÚ DE OPCIONES: \n1. Definir hábitos. \n2. Registrar nuevo día. \n3. Ver datos almacenados. \n4. Generar gráficos. \n5. Salir.")
    opciones = int(input("Ingrese la opción: "))
    print("="*100)

    while opciones < 1 or opciones > 5:
        print("\nSe ha presentado un error de digitación. MENÚ DE OPCIONES: \n1. Definir hábitos. \n2. Registrar nuevo día. \n3. Ver datos almacenados. \n4. Generar gráficos. \n5. Salir. ")
        opciones = int(input("Ingrese la opción: "))
        print("="*100)

    match opciones:
        case 1:
            n = int(input("¿Cuántos hábitos deseas realizar diariamente? (Máximo 10 hábitos): "))

            while n < 0 or n > 10:
                n = int(input("Error de digitación. ¿Cuántos hábitos deseas realizar diariamente?: "))

            contadores = np.zeros(n)            

            i = 1

            while i <= n:
                actividad = input(f"Ingrese el hábito número {i}: ")
                cent = input("Desea continuar? (y/n): ")

                while cent.lower() not in ('y', 'n'):
                    cent = input("Desea continuar? (y/n): ")

                if cent.lower() == "y":
                    actividades.append(actividad)
                else:
                    i -= 1
                i += 1
        case 2:
            print(f"\nBienvenido al día {dias}")
            print("A continuación aparecerá las actividades que ya ha realizado. Marque el número correspondiente si ha realizado esa actividad")
        case 3:
            print("Hola cara de bola")
        case 4:
            print("Hola")
        case 5:
            break