# Paquetes
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
    
def agregar_paquete(paquetes, destino, dias, transporte, hotel, precio):
    paquete = [destino, dias, transporte, hotel, precio]
    paquetes.append(paquete)

def mostrar_paquetes(disponibles):
    print("Paquetes disponiles:")
    for paquete in disponibles:
        print(f"Destino: {paquete[0]}, Días: {paquete[1]}, Aerolínea: {paquete[2]}, Hotel: {paquete[3]}, Precio: {paquete[4]}$")
    
#Programa Principal

print("--- Sistema de búsqueda y reserva de paquetes turísticos ---")

opcion = 0
while opcion != 5:
    print("\n1. Agregar paquete")
    print("2. Buscar paquete por destino") #Aca sino también puede ser un buscar y que te de opciones tipo destino, precio, dias
    print("3. Reservar paquete")
    print("4. Mostrar todos los paquetes disponibles")
    print("5. Salir")
        
    opcion = int(input("\nSeleccione una opción: "))
    print()
    
    if opcion == 1:
        destino = input("Ingrese el destino: ")
        dias = int(input("Ingrese la cantidad de días: "))
        transporte = input("Ingrese la aerolínea: ")
        hotel = input("Ingrese el nombre del hotel: ")
        precio = int(input("Ingrese el precio: "))
        agregar_paquete(paquetes, destino, dias, transporte, hotel, precio)
        print("Paquete agregado con éxito.")

    elif opcion == 2:
        print("Seleccione el criterio de búsqueda:")
        print("1. Por destino")
        print("2. Por días")
        print("3. Por precio")
        
        criterio_opcion = int(input("Ingrese el número de la opción: "))
        print()

        if criterio_opcion == 1:
            destino = input("Ingrese el destino que desea buscar: ")
            encontrados = [paquete for paquete in paquetes if paquete[0] == destino]
        
            if encontrados:
                mostrar_paquetes(encontrados)
            else:
                print("No se encontró ningún paquete con ese destino.")

        elif criterio_opcion == 2:
            dias = int(input("Ingrese la cantidad de días que desea buscar: "))
            encontrados = [paquete for paquete in paquetes if paquete[1] == dias]
        
            if encontrados:
               mostrar_paquetes(encontrados)
            else:
                print("No se encontró ningún paquete con esa cantidad de días.")

        elif criterio_opcion == 3:
            precio = int(input("Ingrese el precio máximo que desea buscar: "))
            encontrados = [paquete for paquete in paquetes if paquete[4] <= precio]
        
            if encontrados:
                mostrar_paquetes(encontrados)
            else:
                print("No se encontró ningún paquete dentro del rango de precio.")

        else:
            print("Opción no válida. Por favor, intente nuevamente.")
           
    elif opcion == 3:
        print("Paquete reservado")

    elif opcion == 4:
        mostrar_paquetes(paquetes)

    elif opcion == 5:
        print("Saliendo del sistema...")
        
    else:
        print("Opción no válida. Por favor, intente nuevamente.")