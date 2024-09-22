# Programa para una agencia de venta de paquetes turisticos, el que lo usa es el empleado de la agencia
# Matriz de paquetes hardcodeada
# [Destino, Dias, Aerolinea, Hotel, Precio, Disponibilidad]

import time

paquetes = [
    ["Barcelona", 6, "Iberia", "Hotel NH Barcelona", 1450, 12],
    ["Berlin", 6, "Lufthansa", "Berlin Plaza Hotel", 1500, 10],
    ["Berlin", 8, "Delta Airlines", "Berlin Central Hotel", 1600, 8],
    ["Ciudad de Mexico", 9, "Aeromexico", "Hotel CDMX", 1350, 4],
    ["Londres", 4, "British Airways", "The London Inn", 1500, 5],
    ["Londres", 5, "Aerolineas Argentinas", "The London Inn", 1550, 8],
    ["Londres", 5, "British Airways", "The London Inn", 1450, 2],
    ["Londres", 6, "Lufthansa", "The London Inn", 1600, 2],
    ["Madrid", 7, "Iberia", "Hotel Madrid Centro", 1550, 9],
    ["Madrid", 5, "Air Europa", "Hotel Madrid Centro", 1500, 3],
    ["Nueva Delhi", 8, "British Airways", "Delhi Palace Hotel", 2100, 10],
    ["Nueva York", 10, "Aerolineas Argentinas", "NYC Plaza", 1800, 8],
    ["Nueva York", 12, "Delta Airlines", "NYC Plaza", 1900, 12],
    ["Nueva York", 8, "Delta Airlines", "The Central Park North", 1600, 2],
    ["Rio de Janeiro", 7, "LATAM Airlines", "Hotel Atlantico Copacabana", 1050, 10],
    ["Rio de Janeiro", 5, "Aerolinas Argentinas", "Hotel Atlantico Copacabana", 900, 5],
    ["Rio de Janeiro", 10, "LATAM Airlines", "Hotel Atlantico Copacabana", 1250, 20],
    ["Seul", 5, "Delta Airlines", "Seoul Central Hotel", 1450, 15],
    ["Sidney", 8, "Delta Airlines", "Sydney Harbour Hotel", 2200, 4],
    ["Tokyo", 7, "Delta Airlines", "Tokyo Grand Hotel", 2000, 5],
    ["Paris", 7, "Air France", "Hotel Parisien", 1700, 8],
    ["Paris", 5, "Air France", "Hotel Parisien", 1400, 9]
]

# Lista de los nombres de los meses
nombres_meses = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]

# Funcion de convertir numeros a palabras
def numero_a_palabras(numero):
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["","ciento", "docientos", "trecientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    especiales = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
    
    if 0 <= numero < 10:
        return unidades[numero]
    elif 10 <= numero < 20:
        return especiales[numero - 10]
    elif 20 <= numero < 100:
        if numero % 10 == 0:
            return decenas[numero // 10]
        else:
            return decenas[numero // 10] + " y " + unidades[numero % 10]
    else:
        return str(numero)

# Funcion de convertir fecha a palabras
def print_fechas(viaje_anio, viaje_mes, viaje_dia, anio_actual, mes_actual, dia_actual):
    # compara fechas y error si son fechas anteriores
    if (viaje_anio < anio_actual) or (viaje_anio == anio_actual and viaje_mes < mes_actual) or (viaje_anio == anio_actual and viaje_mes == mes_actual and viaje_dia < dia_actual):
        print("Fecha no valida")
        bandera = True
        return bandera
    else:
        # Print fechas en palabras
        dia_viaje_palabras = numero_a_palabras(viaje_dia)
        print(f"Fecha del viaje: {dia_viaje_palabras} de {nombres_meses[viaje_mes - 1]} de {viaje_anio}")
        bandera = False
        return bandera

#Funcion para agregar paquetes a la matriz
def agregar_paquete(paquetes, destino, dias, transporte, hotel, precio, disponibilidad):
    paquete = [destino, dias, transporte, hotel, precio, disponibilidad]
    paquetes.append(paquete)

#Funcion para mostrar los paquetes (pueden ser todos o algunos dependiendo la busqueda)
def mostrar_paquetes(disponibles):
    if disponibles:
        print("")
        print("Paquetes disponibles: ")
        print("")
        print(f"{'Destino':^18} | {'Dias':^5} | {'Aerolinea':^25} | {'Hotel':^28} | {'Precio':^8} | {'Disponibilidad':^16}") 
        print("-" * 115)
        for paquete in disponibles:
            print(f"{paquete[0]:18} {paquete[1]:^10} {paquete[2]:27} {paquete[3]:30} {paquete[4]:>5}$ {paquete[5]:^12}")
    else:
        print("No se encontraron paquetes disponibles.")

#Diccionario de funciones de busqueda
criterios_busqueda = {
    "1": lambda paquetes, destino: [paquete for paquete in paquetes if paquete[0] == destino],
    "2": lambda paquetes, dias: [paquete for paquete in paquetes if paquete[1] == int(dias)],
    "3": lambda paquetes, precio: [paquete for paquete in paquetes if paquete[4] <= int(precio)],
    "4": lambda paquetes, hotel: [paquete for paquete in paquetes if paquete[3] == hotel],
    "5": lambda paquetes, aerolinea: [paquete for paquete in paquetes if paquete[2] == aerolinea]
}

# Programa Principal

# Obtener fecha actual
fecha_actual = time.localtime()
anio_actual, mes_actual, dia_actual = fecha_actual.tm_year, fecha_actual.tm_mon, fecha_actual.tm_mday

print("--- Sistema de busqueda y reserva de paquetes turisticos ---")

opcion = 0
while opcion != 4:
    print("\n1. Agregar paquete")
    print("2. Busqueda y reserva de paquete") 
    print("3. Mostrar todos los paquetes disponibles")
    print("4. Salir")
        
    opcion = int(input("\nSeleccione una opcion: "))
    print("")
    
    if opcion == 1:
        destino = input("Ingrese el destino: ")
        dias = int(input("Ingrese la cantidad de dias: "))
        transporte = input("Ingrese la aerolinea: ")
        hotel = input("Ingrese el nombre del hotel: ")
        precio = int(input("Ingrese el precio: "))
        disponibilidad = int(input("Ingrese cuanta disponibilidad hay para el paquete: "))
        agregar_paquete(paquetes, destino, dias, transporte, hotel, precio, disponibilidad)
        print("Paquete agregado con exito.")

    elif opcion == 2:
        
        cantidad_personas = int(input("¿Cuantas personas van a viajar?: "))
        
        #Validamos el numero de personas
        while not (0 < cantidad_personas <= 30):
                print("Numero de personas no válido, ingrese de nuevo.")
                cantidad_personas = int(input("¿Cuantas personas van a viajar?: "))
        
        #Empezamos con la busqueda
        print("Seleccione el criterio de busqueda: ")
        print("1. Por destino")
        print("2. Por dias")
        print("3. Por precio")
        print("4. Por hotel")
        print("5. Por aerolinea")

        mensajes_busqueda = {
            "1": "Ingrese el destino que desea buscar: ",
            "2": "Ingrese la cantidad de dias que desea buscar: ",
            "3": "Ingrese el precio maximo que desea buscar: ",
            "4": "Ingrese el hotel que desea buscar: ",
            "5": "Ingrese la areolinea que desa buscar: "
        }
        
        while True:
            criterio_opcion = input("Ingrese el numero de criterio de busqueda: ")
            
            if criterio_opcion in criterios_busqueda:
                valor = input(mensajes_busqueda[criterio_opcion])
                #Busqueda de paquetes con diccionario de funciones
                paquetes_buscados = criterios_busqueda[criterio_opcion](paquetes, valor)
                mostrar_paquetes(paquetes_buscados)
                break
            
            else:
                print("Opcion no valida. Intente de nuevo.")
        
        while len(paquetes_buscados) > 1:
            print("\nAun hay varios paquetes disponibles. Refine su busqueda")
            print("1. Por destino")
            print("2. Por dias")
            print("3. Por precio")
            print("4. Por hotel")
            print("5. Por aerolinea")
            
            while True:
                criterio_opcion = input("Ingrese el numero de criterio de busqueda: ")
                
                if criterio_opcion in criterios_busqueda:
                    valor = input(mensajes_busqueda[criterio_opcion])
                    #Busqueda de paquetes con diccionario de funciones
                    paquetes_buscados = criterios_busqueda[criterio_opcion](paquetes_buscados, valor)
                    mostrar_paquetes(paquetes_buscados)
                    break
                else:
                    print("Opcion no valida. Intente de nuevo.")
        
        #Sistema de reserva
        if len(paquetes_buscados) == 1:
            print("\n--- Reserva de Paquete ---")
            reservar = input("¿Desea reservar este paquete? (si/no): ")
            if reservar == "si":
                bandera = True
                while bandera == True:
                    fecha_viaje = input("Ingrese la fecha del viaje (yyyy-mm-dd): ")
                    # Splitear la fecha para convertir a enteros
                    viaje_anio, viaje_mes, viaje_dia = map(int, fecha_viaje.split('-'))
                    bandera = print_fechas(viaje_anio,viaje_mes,viaje_dia, anio_actual, mes_actual, dia_actual)
                clientes = set()  # conjunto para almacenar los clientes sin duplicados
                for i in range(cantidad_personas):
                    print(f"Cliente {i+1}:")
                    nombre = input("Ingrese el nombre del cliente: ")
                    dni = int(input("Ingrese el DNI del cliente: "))
                    edad = int(input("Ingrese la edad del cliente: "))
                print("Paquete reservado con exito.") 
            else:
                print("No se realizo la reserva.")
            
    elif opcion == 3:
        mostrar_paquetes(paquetes)

    elif opcion == 4:
        print("Saliendo del sistema...")
        
    else:
        print("Opcion no valida. Por favor, intente nuevamente.")
