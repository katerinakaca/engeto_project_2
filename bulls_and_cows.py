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
def kontrola_vstupu():
      vyber = True
      while vyber:
            list_cisel = []
            hadani = input("Enter a number: ")
            for n in hadani:
                  if not n.isnumeric():
                        print("Obsahuje špatné znaky.")
                  elif hadani.count(n) > 1:
                        print("Číslice se nesmí opakovat.")
                  else:
                        list_cisel.append(n)
            if list_cisel[0] == "0" or len(list_cisel) != 4:
                  print("Číslo nesmí začínat 0 a číslo musí být 4místné.")
                  continue
            else:
                  vyber = False
      return list_cisel






print(kontrola_vstupu())