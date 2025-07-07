import random

print("Piedra, papel o tijeras, el juego")
jugador = input("Elige: piedra, papel o tijeras: ").lower()


while jugador != "piedra" and jugador != "papel" and jugador != "tijeras":
    print("Opción no válida.")
    jugador = input("Elige: piedra, papel o tijeras: ").lower()

#computadora elige 
numero_aleatorio = random.randint(1, 3)

if numero_aleatorio == 1:
    computadora = "piedra"
elif numero_aleatorio == 2:
    computadora = "papel"
elif numero_aleatorio == 3:
    computadora = "tijeras"

print("La computadora eligio:", computadora)

# Comparar jugadas
if jugador == computadora:
    print("Empate")
elif (jugador == "piedra" and computadora == "tijeras") or \
     (jugador == "papel" and computadora == "piedra") or \
     (jugador == "tijeras" and computadora == "papel"):
    print("Ganaste!")
else:
    print("Perdiste.")
