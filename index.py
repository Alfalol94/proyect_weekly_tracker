dias = 1

print("\n Hola, Bienvenido a tu tracker personalizado de tus habitos diarios. \n")

while True:
    print("="*100)
    print("MENÚ DE OPCIONES: \n1. Registrar nuevo día. \n2. Ver datos almacenados. \n3. Generar gráficos. \n4. Salir.")
    opciones = int(input("Ingrese la opción: "))
    print("="*100)

    while opciones < 1 or opciones > 4:
        print("\nSe ha presentado un error de digitación. \nMENÚ DE OPCIONES: \n1. Registrar nuevo día. \n2. Ver datos almacenados. \n3. Generar gráficos. \n4. Salir. ")
        opciones = int(input("Ingrese la opción: "))
        print("="*100)

    match opciones:
        case 1:
            print("Hola mundo")
        case 2:
            print("Despues haré esto")
        case 3:
            print("Hola cara de bola")
        case 4:
            break
    
    
    
    
