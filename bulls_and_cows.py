import random

# print("Welcome in our game Bulls and Cows!")
# oddelovac = "-" * 47
# print(oddelovac)
# print("""
# I've generated a random 4 digit number for you.
# Let's play a bulls and cows game.
# """
#       )
# print(oddelovac)

#vygenerovat náhodné číslo
def nahodne_cislo():
      vybiram_cislo = True
      while vybiram_cislo:
            random.seed(1)
            cislo = random.sample(range(10), k = 4)
            if cislo[0] != 0:
                  spravne_cislo = cislo
                  break
            else:
                  continue
      return spravne_cislo

#kontrola vstupu uživatele
def kontrola_vstupu(hadani):
      vyber = True
      while vyber:
            list_cisel = []
            for n in hadani:
                  if not n.isnumeric():
                        print("Obsahuje špatné znaky.")
                        break
                  elif hadani.count(n) > 1:
                        print("Číslice se nesmí opakovat.")
                        break
                  else:
                        list_cisel.append(n)
            if list_cisel[0] == "0" or len(list_cisel) != 4:
                  print("Číslo nesmí začínat 0 a číslo musí být 4místné.")
                  break
            else:
                  vyber = False
      return list_cisel

#hra samotná
def hra():
      hra_bezi = True
      while hra_bezi == True:
            cislo = nahodne_cislo()
            hadani = input("Zadej 4místné číslo: ")
            spravne_hadani = kontrola_vstupu(hadani)
            break
      return spravne_hadani

def porovnani_vstupu(cislo, spravne_hadani):
      indexace_cisla = list(enumerate(cislo))
      for i, cislice in enumerate(spravne_hadani):
            dvojice = tuple([i, cislice])
            print(dvojice)














print(porovnani_vstupu(["1", "2", "3", "4"], ["1", "2", "3", "4"]))

