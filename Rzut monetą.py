import random

moneta = random.randint (1, 2)
reszka = 0
orzeł = 0
rzut = 0

while True:
  rzut += 1
  
  if moneta == 1:
    orzeł += 1
    moneta = random.randint (1, 2)
  elif moneta == 2:
    reszka += 1
    moneta = random.randint (1, 2)
  if rzut == 100:
    print("Rzuciłes", orzeł,"orłów oraz", reszka,"reszek")
    break
