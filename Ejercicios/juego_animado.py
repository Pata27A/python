import random

def juego_adivina_numero():
    numero_secreto = random.randint(1, 50)
    intentos = 0
    intentos_maximos = 10
    
    print("¡Bienvenido al juego de adivinanza!")
    print(f"Debes adivinar un número entre 1 y 50. Tienes {intentos_maximos} intentos.")
    
    while intentos < intentos_maximos:
        try:
            numero_usuario = int(input("Ingresa tu número: "))
            intentos += 1
            
            if numero_usuario < 1 or numero_usuario > 50:
                print("Por favor, ingresa un número dentro del rango de 1 a 50.")
                continue
            
            if numero_usuario < numero_secreto:
                print("El número secreto es mayor.")
            elif numero_usuario > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")
    else:
        print(f"Lo siento, has alcanzado el máximo de {intentos_maximos} intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    juego_adivina_numero()
