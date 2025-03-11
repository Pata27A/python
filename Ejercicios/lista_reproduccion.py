def administrar_lista_canciones():
    # Solicitar la cantidad de canciones a agregar con validación
    while True:
        try:
            cantidad = int(input("¿Cuántas canciones desea agregar? "))
            if cantidad > 0:
                break
            else:
                print("El número de canciones debe ser mayor que cero.")
        except ValueError:
            print("Valor incorrecto. Por favor, ingrese un número válido.")

    # Solicitar los nombres de las canciones
    canciones = []
    for i in range(cantidad):
        while True:
            cancion = input(f"Ingrese el nombre de la canción {i + 1}: ").strip()
            if cancion:
                canciones.append(cancion)
                break
            else:
                print("El nombre de la canción no puede estar vacío. Inténtelo de nuevo.")

    # Ordenar la lista alfabéticamente
    canciones.sort()

    # Imprimir la lista ordenada
    print("\nLista de canciones en orden alfabético:")
    for cancion in canciones:
        print(cancion)

# Ejecutar la función solo si se ejecuta desde consola
if __name__ == "__main__":
    administrar_lista_canciones()
