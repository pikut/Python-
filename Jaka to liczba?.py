#Jaka to liczba?

import random

guess = int(input("Jaka to liczba?"))

number = random.randint(1,10)
tries = 5

while tries:
  tries -= 1
  
  if guess > number:
    print("Za duża")
    print("Pozostało Ci", tries,"prób")
  
  elif guess < number:
    print("Za mała")
    print("Pozostało Ci", tries,"prób")
    
  elif guess == number:
    print("Zgadłes! Ta liczba to", guess,"Zostały Ci", tries,"prób")
    break
  
  if not tries:
    print("KONIEC")
    break
  
  guess = int(input("\nJaka to liczba?"))


  
