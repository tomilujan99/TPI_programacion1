import csv

def cargar_csv(ruta):
    paises = []
    try:
        with open(ruta, encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                })
    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
    except ValueError:
        print("Error: hay datos con formato incorrecto en el CSV.")
    return paises

def guardar_csv(ruta, paises):
    with open(ruta, "w", encoding="utf-8-sig", newline="") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(paises)

def mostrar_menu():
    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1. Agregar país")
    print("2. Actualizar país")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("0. Salir")
    print("==============================")

def main():
    paises = cargar_csv("paises.csv")
    print(f"Se cargaron {len(paises)} países.")

    while True:
        mostrar_menu()
        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            print(">> Buscar país (próximamente)")
        elif opcion == "4":
            print(">> Filtrar países (próximamente)")
        elif opcion == "5":
            print(">> Ordenar países (próximamente)")
        elif opcion == "6":
            print(">> Estadísticas (próximamente)")
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingresá un número del 0 al 6.")

def agregar_pais(paises):
    print("\n--- Agregar país ---")
    
    nombre = input("Nombre del país: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    
    try:
        poblacion = int(input("Población: ").strip())
        if poblacion <= 0:
            print("Error: la población debe ser un número positivo.")
            return
    except ValueError:
        print("Error: la población debe ser un número entero.")
        return
    
    try:
        superficie = int(input("Superficie en km²: ").strip())
        if superficie <= 0:
            print("Error: la superficie debe ser un número positivo.")
            return
    except ValueError:
        print("Error: la superficie debe ser un número entero.")
        return
    
    continente = input("Continente: ").strip()
    if continente == "":
        print("Error: el continente no puede estar vacío.")
        return

    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(pais)
    guardar_csv("paises.csv", paises)
    print(f"País '{nombre}' agregado correctamente.")  

def actualizar_pais(paises):
    print("\n--- Actualizar país ---")
    
    nombre = input("Nombre del país a actualizar: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    
    # Buscar el país en la lista
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break
    
    if pais_encontrado is None:
        print(f"No se encontró ningún país con el nombre '{nombre}'.")
        return
    
    print(f"País encontrado: {pais_encontrado['nombre']} | Población: {pais_encontrado['poblacion']} | Superficie: {pais_encontrado['superficie']}")
    
    try:
        poblacion = int(input("Nueva población: ").strip())
        if poblacion <= 0:
            print("Error: la población debe ser un número positivo.")
            return
    except ValueError:
        print("Error: la población debe ser un número entero.")
        return
    
    try:
        superficie = int(input("Nueva superficie en km²: ").strip())
        if superficie <= 0:
            print("Error: la superficie debe ser un número positivo.")
            return
    except ValueError:
        print("Error: la superficie debe ser un número entero.")
        return
    
    pais_encontrado["poblacion"] = poblacion
    pais_encontrado["superficie"] = superficie
    guardar_csv("paises.csv", paises)
    print(f"País '{pais_encontrado['nombre']}' actualizado correctamente.")


main()