


def convertir(valor, escala):

    if escala.upper() == "C":
        return (valor * 9 / 5) + 32 # Celsius a Fahrenheit
    elif escala.upper() == "c":
        return (valor -32) * 5 / 9 # Fahrenheit a Celsius
    else: 
        return None #escala invalida
    

try: 
    valor = float(input('Ingrese la temperatura a convertir: '))
    escala = input('Ingrese la escala de convercion C o F')

    resultado = convertir(valor, escala)
    if resultado is not None:
        print(f"La temperatura convertida es: {resultado:.2f}°{'F' if escala == 'C' else 'C'}")
    else:
        print("Escala no válida. Usa 'C' o 'F'.")
except ValueError:
    print("Error: Ingrese un número válido para la temperatura.")