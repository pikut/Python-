import random

liczba = int(input("Zgadnij o jakiej liczbie z przedziału od 1 do 10 myslę?"))
komputer = random.randint(1, 10)

while komputer != liczba:
  print("Czy mylisz o...", komputer)
  print("Niestety nie, spróbuj ponownie")
  komputer = random.randint(1, 10)
 
print("Czy mylisz o...", komputer) 
print("Zgadłes, myslę o liczbie", liczba)
