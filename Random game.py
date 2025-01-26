import random
turno = random.randint(0,1)
def jugar_juego():
    global turno
    numero_inicial = random.randint(50, 150) 
    print(f"Número inicial: {numero_inicial}")

    while numero_inicial > 0:
        if turno == 0:
            print("Turno del jugador2")
            while True:
                try:
                    usuario_input = int(input("Introduce un número del 1 al 9: "))
                    if 1 <= usuario_input <= 9:
                        break
                    else:
                        print("Por favor, introduce un número válido entre 1 y 9.")
                except ValueError:
                    print("Entrada no válida. Por favor, introduce un número.")

            numero_inicial -= usuario_input
            print(f"Número restante: {numero_inicial}")

            if numero_inicial == 0:
                print("¡Has ganado!")
                break
            if numero_inicial < 0:
                print("¡Has perdido!")
                break
            if numero_inicial < 10:
                numero_ia = numero_inicial  
            else:
                numero_ia = random.randint(1, 9)
            turno = 1

        if turno == 1:
            print("Turno de la IA")
            numero_inicial -= numero_ia
            print(f"La IA resta: {numero_ia}")
            print(f"Número restante: {numero_inicial}")

            if numero_inicial == 0:
                print("La IA ha ganado.")
            turno = 0


jugar_juego()
