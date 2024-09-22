# Programa para una agencia de venta de paquetes turisticos, el que lo usa es el empleado de la agencia

# Matriz de paquetes hardcodeada
# [Destino, Días, Aerolínea, Hotel, Precio]

paquetes = [
    ["Barcelona", 6, "Iberia", "Barcelona Beach Hotel", 1450],
    ["Berlin", 6, "Lufthansa", "Berlin Plaza Hotel", 1500],
    ["Berlin", 8, "Delta Airlines", "Berlin Central Hotel", 1600],
    ["Ciudad de México", 9, "Aeroméxico", "Hotel CDMX", 1350],
    ["Londres", 4, "British Airways", "The London Inn", 1500],
    ["Londres", 5, "Aerolineas Argentinas", "The London Inn", 1550],
    ["Londres", 5, "British Airways", "The London Inn", 1450],
    ["Londres", 6, "Lufthansa", "The London Inn", 1600],
    ["Madrid", 7, "Iberia", "Hotel Madrid Centro", 1550],
    ["Madrid", 5, "Air Europa", "Hotel Madrid Centro", 1500],
    ["Nueva Delhi", 8, "British Airways", "Delhi Palace Hotel", 2100],
    ["Nueva York", 10, "Aerolineas Argentinas", "NYC Plaza", 1800],
    ["Nueva York", 12, "Delta Airlines", "NYC Plaza", 1900],
    ["Nueva York", 8, "Delta Airlines", "The Central Park North", 1600],
    ["Rio de Janeiro", 7, "LATAM Airlines", "Hotel Atlantico Copacabana", 1250],
    ["Rio de Janeiro", 5, "Aerolinas Argentinas", "Hotel Atlantico Copacabana", 1150],
    ["Rio de Janeiro", 10, "LATAM Airlines", "Hotel Atlantico Copacabana", 1350],
    ["Seul", 5, "Delta Airlines", "Seoul Central Hotel", 1450],
    ["Sidney", 8, "Delta Airlines", "Sydney Harbour Hotel", 2200],
    ["Tokyo", 7, "Delta Airlines", "Tokyo Grand Hotel", 2000],
    ["Paris", 7, "Air France", "Hotel Parisien", 1700],
    ["Paris", 5, "Air France", "Hotel Parisien", 1400]
]

#Funcion para agregar paquetes a la matriz
def agregar_paquete(paquetes, destino, dias, transporte, hotel, precio):
    paquete = [destino, dias, transporte, hotel, precio]
    paquetes.append(paquete)

#Funcion para mostrar los paquetes (pueden ser todos o algunos dependiendo la busqueda)
def mostrar_paquetes(disponibles):
    if disponibles:
        print("Paquetes disponibles: ")
        print("")
        print(f"{'Destino':^18} | {'Dias':^5} | {'Aerolinea':^25} | {'Hotel':^30} | {'Precio':^8}")
        print("-" * 99)
        for paquete in disponibles:
            print(f"{paquete[0]:18} {paquete[1]:^8}   {paquete[2]:27} {paquete[3]:32} {paquete[4]:>5}$")
    else:
        print("No se encontraron paquetes disponibles")

#Funcion Lambda para descuento, se tendria que poner en la parte de la reserva
calcular_descuento = lambda precio, edad: precio * 0.95 if edad > 60 else precio

#Programa Principal

print("--- Sistema de busqueda y reserva de paquetes turísticos ---")

opcion = 0
while opcion != 5:
    print("\n1. Agregar paquete")
    print("2. Buscar paquete") 
    print("3. Reservar paquete")
    print("4. Mostrar todos los paquetes disponibles")
    print("5. Salir")
        
    opcion = int(input("\nSeleccione una opcion: "))
    print()
    
    if opcion == 1:
        destino = input("Ingrese el destino: ")
        dias = int(input("Ingrese la cantidad de dias: "))
        transporte = input("Ingrese la aerolinea: ")
        hotel = input("Ingrese el nombre del hotel: ")
        precio = int(input("Ingrese el precio: "))
        agregar_paquete(paquetes, destino, dias, transporte, hotel, precio)
        print("Paquete agregado con exito.")

    elif opcion == 2:
        print("Seleccione el criterio de busqueda:")
        print("1. Por destino")
        print("2. Por dias")
        print("3. Por precio")
        
        #Diccionario de funciones
        #Destino busqueda por destino
        #Clave 'Destino', valor la funcion
        
        criterio_opcion = int(input("Ingrese el número de la opcion: "))
        print()

        if criterio_opcion == 1:
            destino = input("Ingrese el destino que desea buscar: ")
            encontrados = [paquete for paquete in paquetes if paquete[0] == destino]
            mostrar_paquetes(encontrados)

        elif criterio_opcion == 2:
            dias = int(input("Ingrese la cantidad de dias que desea buscar: "))
            encontrados = [paquete for paquete in paquetes if paquete[1] == dias]
            mostrar_paquetes(encontrados)

        elif criterio_opcion == 3:
            precio = int(input("Ingrese el precio maximo que desea buscar: "))
            encontrados = [paquete for paquete in paquetes if paquete[4] <= precio]
            mostrar_paquetes(encontrados)

        else:
            print("Opcion no valida. Por favor, intente nuevamente")
        
        reservar = input("¿Desea reservar este paquete? (si/no): ")
        if reservar == "si":
            print("Paquete reservado con exito.") #ACA ES DONDE ENTRA LA PARTE DE RESERVA
        else:
            print("No se realizo la reserva.")
        
        #PARTE EN PROCESO
        print("\n--- Reserva de Paquete ---")
    
        fecha_viaje = input("Ingrese la fecha del viaje (dd/mm/yyyy): ")
        cantidad_personas = int(input("¿Cuántas personas van a viajar?: "))
    
        clientes = set()  # conjunto para almacenar los clientes sin duplicados
        for i in range(cantidad_personas):
            print(f"Cliente {i+1}:")
            nombre = input("Ingrese el nombre del cliente: ")
            dni = int(input("Ingrese el DNI del cliente: "))
            edad = int(input("Ingrese la edad del cliente: "))
        
        # Diccionario con lista adentro {ID: [nombre, dni, edad]}
        #Hasta aca ah
    
        print("¡Reserva realizada con exito!\n")
           
    elif opcion == 3:
        print("Funcion en proceso")

    elif opcion == 4:
        mostrar_paquetes(paquetes)

    elif opcion == 5:
        print("Saliendo del sistema...")
        
    else:
        print("Opcion no valida. Por favor, intente nuevamente")
