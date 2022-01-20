import random

def nahodne_cislo():
      vybiram_cislo = True
      while vybiram_cislo:
            cislo = random.sample(range(10), k = 4)
            print(cislo)
            if cislo[0] != 0:
                  spravne_cislo = cislo
                  break
            else:
                  continue
      return spravne_cislo




print(nahodne_cislo())
# print("Welcome in our game Bulls and Cows!")
# oddelovac = "-" * 47
# print(oddelovac)
# print("""
# I've generated a random 4 digit number for you.
# Let's play a bulls and cows game.
# """
#       )
# print(oddelovac)
