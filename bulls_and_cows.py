import random

print("Welcome in our game Bulls and Cows!")
oddelovac = "-" * 47
print(oddelovac)
print("""
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
"""
      )
print(oddelovac)

#vygenerovat náhodné číslo
def nahodne_cislo():
      vybiram_cislo = True
      while vybiram_cislo:
            random.seed(1)
            cislo = random.sample(range(10), k = 4)
            print(cislo)
            if cislo[0] != 0:
                  spravne_cislo = cislo
                  break
            else:
                  continue
      return spravne_cislo

#kontrola vstupu uživatele
def kontrola_vstupu():

      while True:
            list_cisel = []
            hadani = input("Enter a number: ")
            for n in hadani:
                  if not n.isnumeric():
                        print("Obsahuje špatné znaky.")
                        continue
                  elif hadani.count(n) > 1:
                        print("Číslice se nesmí opakovat.")
                        continue
                  else:
                        list_cisel.append(int(n))
            if list_cisel[0] == "0" or len(list_cisel) != 4:
                  print("Číslo nesmí začínat 0 a číslo musí být 4místné.")
                  continue
            else:
                  break
      return list_cisel

#hra samotná
def hra():
      pokusy = 0
      oddelovac = "-" * 47
      while True:
            cislo = nahodne_cislo()
            spravne_hadani = kontrola_vstupu()
            pocet = pocet_bulls_and_cows(cislo, spravne_hadani)
            pocet_byku = pocet[0]
            pocet_krav = pocet[1]
            tisk_poctu_bulls_and_cows(pocet_byku, pocet_krav)
            print(oddelovac)
            pokusy += 1
            if pocet_byku == 4:
                  break
      vysledek = []
      for c in cislo:
            vysledek.append(str(c))

      return print(f"Číslo je {''.join(vysledek)}.\n Pro uhodnutí správného výsledku jsi potřeboval {pokusy} pokusů. ")



def pocet_bulls_and_cows(cislo, spravne_hadani):
      indexace_cisla = list(enumerate(cislo))
      pocet_byku = 0
      pocet_krav = 0
      for i, cislice in enumerate(spravne_hadani):
            dvojice = tuple([i, cislice])
            if dvojice in indexace_cisla:
                  pocet_byku +=1
            elif cislice in cislo and cislo[i] != cislice:
                  pocet_krav += 1
      return [pocet_byku, pocet_krav]

def tisk_poctu_bulls_and_cows(pocet_byku, pocet_krav):
      if pocet_byku == 1 and pocet_krav == 1:
            return print(f"{pocet_byku} bull,{pocet_krav} cow")
      elif pocet_byku == 1 and pocet_krav != 1:
            return print(f"{pocet_byku} bull,{pocet_krav} cows")
      elif pocet_byku != 1 and pocet_krav == 1:
            return print(f"{pocet_byku} bulls,{pocet_krav} cow")
      elif pocet_byku == 4:
            return print("ANO, uhodls!")
      else:
            return print(f"{pocet_byku} bulls,{pocet_krav} cows")



hra()

