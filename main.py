numero = int(input("Cual es el numero "))

billetesdequinientos = int(numero / 500)

numero = numero - (500 * billetesdequinientos)

billetesdedoscientos = int(numero / 200)

numero = numero - (200 * billetesdedoscientos)

billetesdecien = int(numero / 100)

numero = numero - (100 * billetesdecien)

billetesdecincuenta = int(numero / 50)

numero = numero - (50 * billetesdecincuenta)

billetesdeveinte = int(numero / 20)

numero = numero - (20 * billetesdeveinte)

monedasdediez = int(numero / 10)

numero = numero - (10 * monedasdediez)

monedasdecinco = int(numero / 5)

numero = numero - (5 * monedasdecinco)

monedasdedos = int(numero / 2)

numero = numero - (2 * monedasdedos)

monedadeuno = numero

print(f"{billetesdequinientos} billetes de 500")

print(f"{billetesdedoscientos} billetes de 200")

print(f"{billetesdecien} billetes de 100")

print(f"{billetesdecincuenta} billetes de 50")

print(f"{billetesdeveinte} billetes de 20")

print(f"{monedasdediez} billetes de 10")

print(f"{monedasdecinco} billetes de 5")

print(f"{monedasdedos} billetes de 2")

print(f"{monedadeuno} billetes de 1")
