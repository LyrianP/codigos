from random import randint

opciones = ["Piedra", "Papel", "Tijeras"]

cpu = opciones[randint(0, 2)]
usuario = raw_input("Piedra, papel o tijeras?").capitalize()

if cpu == usuario:
    print "Empate"
elif cpu == "Papel" and usuario == "Piedra":
    print "Perdiste"
elif cpu == "Piedra" and usuario == "Tijeras":
    print "Perdiste"
elif cpu == "Tijeras" and usuario == "Papel":
    print "Perdiste"

elif cpu == "Piedra" and usuario == "Papel":
    print "Ganaste"
elif cpu == "Tijeras" and usuario == "Piedra":
    print "Ganaste"
elif cpu == "Papel" and usuario == "Tijeras":
    print "Ganaste"
