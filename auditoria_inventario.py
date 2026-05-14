# --- PASO 1: LA MATRIZ DE DATOS ---
# Formato: [Código, Nombre del Producto, Stock Actual, Stock Mínimo]
inventario_tecnologia = [
    [501, "Mouse Inalámbrico", 12, 15],
    [502, "Teclado Mecánico", 20, 10],
    [503, "Monitor Gamer", 4, 8],
    [504, "Disco Duro SSD", 30, 20],
    [505, "Memoria RAM 8GB", 5, 12],
    [506, "Cable HDMI 2m", 50, 30],
    [507, "Cámara Web HD", 2, 6]
]

# --- PASO 2: LA FUNCIÓN (LÓGICA DEL NEGOCIO) ---
def procesar_auditoria(matriz_productos):
    print("============================================")
    print("   INFORME DE AUDITORÍA - TIENDA TECH")
    print("============================================")
    # Encabezados con formato para que se vea ordenado
    print(f"{'CÓDIGO':<10} {'PRODUCTO':<20} {'ESTADO'}")
    print("-" * 45)

    for fila in matriz_productos:
        codigo = fila[0]
        nombre = fila[1]
        actual = fila[2]
        minimo = fila[3]

        # Lógica: Si lo que hay es menos que el mínimo, hay que pedir
        if actual < minimo:
            unidades_a_pedir = minimo - actual
            mensaje = f"SOLICITAR: {unidades_a_pedir} unidades"
        else:
            mensaje = "Stock Suficiente"

        # Imprimir la fila con los resultados
        print(f"{codigo:<10} {nombre:<20} {mensaje}")

    print("-" * 45)
    print("Fin del reporte.")

# --- PASO 3: EJECUCIÓN ---
# Llamamos a la función pasándole nuestra matriz
procesar_auditoria(inventario_tecnologia)