import csv


# =========================================================================
# FUNCIONES AUXILIAR: VALIDACION
# =========================================================================
def solicitar_entero_positivo(mensaje):
    """Solicita un número entero por consola, evitando campos vacíos y letras."""
    while True:
        try:
            valor_input = input(mensaje).strip()
            if not valor_input:  # Si le dan Enter sin escribir nada (campo vacío)
                print(f"\nError: El campo no puede estar vacío. Intente de nuevo.\n")
                continue
                
            valor = int(valor_input)
            if valor <= 0:
                print(f"\nError: El número debe ser mayor a 0. Intente de nuevo.\n")
                continue
                
            return valor  # Si pasó todos los filtros, devuelve el número válido
        except ValueError:
            print(f"\nError: Debe ingresar un número entero válido (sin letras ni espacios).\n")


def solicitar_texto_puro(mensaje):
    """Solicita una cadena de texto por consola, asegurando que no esté vacía y contenga solo letras y espacios."""
    while True:
        valor_input = input(mensaje).strip()
        
        if not valor_input:
            print("\nError: El campo no puede estar vacío. Intente de nuevo.")
            continue
            
        # Reemplazamos los espacios temporariamente para verificar si el resto son solo letras
        # Esto permite nombres compuestos como "Costa Rica" o "Cabo Verde"
        if not valor_input.replace(" ", "").isalpha():
            print("\nError: El nombre debe contener solo letras (sin números ni símbolos). Intente de nuevo.\n")
            continue
            
        return valor_input.title()  # pasamos la primer letra a mayus independiente a lo que se haya ingresado (ej: "argentina" -> "Argentina")




def cargar_csv(ruta):
    paises = []
    try:
        with open(ruta, encoding="utf-8-sig") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                # VALIDACIÓN: Si la fila viene vacía o le faltan columnas clave, la saltea
                if not fila or fila.get("nombre") is None or fila.get("poblacion") is None:
                    continue
                
                try:
                    paises.append({
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"].strip()),    # Si falla, va al except de abajo
                        "superficie": int(fila["superficie"].strip()),  # Si falla, va al except de abajo
                        "continente": fila["continente"].strip()
                    })
                except (ValueError, TypeError):
                    # Si una fila puntual tiene un dato roto, avisa pero no rompe todo el sistema
                    print(f"Advertencia: Se omitió un registro en el CSV por datos inválidos o vacíos.")
                    
    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
        
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

def agregar_pais(paises):
    print("\n--- Agregar país ---\n")
    
    nombre = solicitar_texto_puro("Nombre del país: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    
    try:
        poblacion = solicitar_entero_positivo("Ingrese población: ")
        if poblacion <= 0:
            print("Error: la población debe ser un número positivo.")
            return
    except ValueError:
        print("Error: la población debe ser un número entero.")
        return
    
    try:
        superficie = solicitar_entero_positivo("Ingrese superficie (en km²): ")
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
    print("\n--- Actualizar país ---\n")
    
    nombre = solicitar_texto_puro("\nNombre del país a actualizar: ").strip()
    if nombre == "":
        print("\nError: el nombre no puede estar vacío.")
        return
    
    # Buscar el país en la lista
    pais_encontrado = None
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais_encontrado = pais
            break
    
    if pais_encontrado is None:
        print(f"\nNo se encontró ningún país con el nombre '{nombre}'.")
        return
    
    print(f"\nPaís encontrado: {pais_encontrado['nombre']} | Población: {pais_encontrado['poblacion']} | Superficie: {pais_encontrado['superficie']}")
    
    try:
        poblacion = solicitar_entero_positivo(f"\nIngrese la nueva población: ")
        if poblacion <= 0:
            print(f"\nError: la población debe ser un número positivo.")
            return
    except ValueError:
        print(f"\nError: la población debe ser un número entero.")
        return
    
    try:
        superficie = solicitar_entero_positivo(f"Ingrese la nueva superficie en km²: \n")
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


# =========================================================================
# FUNCIONES DESARROLLADAS POR MENDIZABALGONZA
# =========================================================================

def buscar_pais_por_nombre(paises):
    print("\n--- BUSCAR PAÍS ---")
    busqueda = input("\nIngrese el nombre (o parte del nombre) a buscar: ").strip().lower()
    
    encontrados = []
    for pais in paises:
        if busqueda in pais["nombre"].lower():
            encontrados.append(pais)
            
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} coincidencia(s):\n")
        for p in encontrados:
            print(f"- {p['nombre']} | Continente: {p['continente']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
    else:
        print("No se encontraron países que coincidan con la búsqueda.")

def filtrar_paises(paises):
    if not paises:
        print("⚠️ No hay datos cargados para filtrar.")
        return

    print("\n--- OPCIONES DE FILTRADO ---")
    print("1. Por Continente")
    print("2. Por Rango de Población")
    print("3. Por Rango de Superficie")
    opcion = input("Seleccione una opción de filtrado: ").strip()

    filtrados = []

    if opcion == "1":
        continente_buscar = input("Ingrese el continente a filtrar: ").strip().lower()
        filtrados = [p for p in paises if p["continente"].lower() == continente_buscar]
    elif opcion == "2":
        try:
            min_pob = int(input("Población MÍNIMA: "))
            max_pob = int(input("Población MÁXIMA: "))
            filtrados = [p for p in paises if min_pob <= p["poblacion"] <= max_pob]
        except ValueError:
            print("⚠️ Error: Ingrese números enteros válidos.")
            return
    elif opcion == "3":
        try:
            min_sup = int(input("Superficie MÍNIMA (km²): "))
            max_sup = int(input("Superficie MÁXIMA (km²): "))
            filtrados = [p for p in paises if min_sup <= p["superficie"] <= max_sup]
        except ValueError:
            print("⚠️ Error: Ingrese números enteros válidos.")
            return
    else:
        print("⚠️ Opción de filtrado inválida.")
        return

    if filtrados:
        print(f"\nSe encontraron {len(filtrados)} país(es):")
        for p in filtrados:
            print(f"- {p['nombre']} | {p['continente']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km²")
    else:
        print("❌ No se encontraron países con ese criterio.")

def ordenar_paises(paises):
    if not paises:
        print("⚠️ No hay datos cargados para ordenar.")
        return

    print("\n--- OPCIONES DE ORDENAMIENTO ---")
    print("1. Por Nombre")
    print("2. Por Población")
    print("3. Por Superficie")
    opcion_campo = input("Seleccione campo para ordenar: ").strip()

    
    if opcion_campo == "1":
        import locale
        locale.setlocale(locale.LC_ALL, '')
        clave_orden = lambda x: locale.strxfrm(x["nombre"].lower())
    elif opcion_campo == "2":
        clave_orden = lambda x: x["poblacion"]
    elif opcion_campo == "3":
        clave_orden = lambda x: x["superficie"]
    else:
        print("⚠️ Opción inválida.")
        return

    print("\n1. Ascendente (Menor a Mayor / A-Z)")
    print("2. Descendente (Mayor a Menor / Z-A)")
    opcion_sentido = input("Seleccione el sentido: ").strip()

    if opcion_sentido == "1":
        descendente = False
    elif opcion_sentido == "2":
        descendente = True
    else:
        print("⚠️ Opción inválida.")
        return

    lista_ordenada = sorted(paises, key=clave_orden, reverse=descendente)

    print("\n--- RESULTADO DEL ORDENAMIENTO ---")
    for p in lista_ordenada:
        print(f"- {p['nombre']} | Pob: {p['poblacion']} | Sup: {p['superficie']} km² | {p['continente']}")

def mostrar_estadisticas(paises):
    if not paises:
        print("⚠️ No hay datos cargados.")
        return
        
    print("\n" + "="*30)
    print("   ESTADÍSTICAS DEL DATASET")
    print("="*30)
    
    pais_mayor_pob = max(paises, key=lambda x: x["poblacion"])
    pais_menor_pob = min(paises, key=lambda x: x["poblacion"])
    
    print(f"📊 Mayor Población: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']} hab.)")
    print(f"📊 Menor Población: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']} hab.)")
    
    total_pob = sum(p["poblacion"] for p in paises)
    total_sup = sum(p["superficie"] for p in paises)
    cant = len(paises)
    
    print(f"📈 Promedio de Población: {total_pob / cant:,.2f} hab.")
    print(f"📈 Promedio de Superficie: {total_sup / cant:,.2f} km²")
    
    print("\n🗺️ Países por continente:")
    conteo = {}
    for p in paises:
        conteo[p["continente"]] = conteo.get(p["continente"], 0) + 1
    for cont, cant_p in conteo.items():
        print(f"   - {cont}: {cant_p}")
    print("="*30)


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
            buscar_pais_por_nombre(paises)
        elif opcion == "4":
            filtrar_paises(paises)
        elif opcion == "5":
            ordenar_paises(paises)
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Ingresá un número del 0 al 6.")


if __name__ == "__main__":
    main()