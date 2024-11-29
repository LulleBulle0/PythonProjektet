import ASCII_art as ascii

print(ascii.text("Through the trollgate"))


print("[1]Spela!")
print("[2]Avbryt")
start = int(input("Är du redo för att spela? "))

import random

slumptal = random.randint(1, 3)
monster = random.randint(1, 100)
tressure = random.randint(1, 100)

def Troll():
    print("Monster!")
    print(monster)

    if monster <= 10:
        print()

def kista():
    print("Tressure!")
    print(tressure)
    if tressure <= 15:
        inventory.append("sheild")
                
    elif 15 < tressure <= 30:
        inventory.append("healthpotion")
                
    elif tressure > 30: 
         inventory.append("glass")

def fälla():
    print("Trap!")
    print(HP - 20)

jHP = 40
tHP = 30
sHP = 15


if start == 1:
    print("Spelet startas!")
    
    inventory = []

    print("[1] Lätt")
    print("[2] Medel")
    print("[3] Svårt")
    Svårhetsgrad = int(input("Välj din svårhetsgrad "))

    if Svårhetsgrad == 1:
        HP = 100
        print("---Ditt HP---")
        print(HP)
        inventory.append("Svärd")
    elif Svårhetsgrad == 2:
        HP = 75
        print("---Ditt HP---")
        print(HP)
        inventory.append("svärd")
    elif Svårhetsgrad == 3:
        HP = 50
        print("---Ditt HP---")
        print(HP)
        inventory.append("svärd")
    
    else:
        print("Ogiltligt svar!")
    
    print("---MENY---")
    print("[1] Inventory")
    print("[2] Gå till första dörrarna")
    val = int(input("Vad vill du göra? "))

    if val == 1:
        print(inventory)
        #Om man väljer inventory, så ska man sedan kunna gå vidare till dörrarna
    elif val == 2:
        print("Du har kommit fram till dem första dörrarna!")
        print("Vll du gå in i dörr 1, 2 eller 3?")
    
events = ["monster", "kista", "fälla"]
    
roomChoice = input("> ")
    
if(roomChoice in ["1", "2", "3"]):
    event = random.choice(events)

    if (event == "monster"):
        Troll()
    elif (event == "kista"):
        kista()
    elif (event == "fälla"):
        fälla()

    



       

    




elif start == 2:
    print("Du har valt att avbryta systemet")

else:
    print("ogiltligt svar")



