

import random

slumptal = random.randint(1, 3)
monster = random.randint(1, 100)
tressure = random.randint(1, 100)

def Troll():
    print("Monster!")
    print(monster)


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

print("[1]Spela!")
print("[2]Avbryt")
start = int(input("Är du redo för att spela? "))

name = input("Välj namn till din karaktär! ")

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
        if "rustning" in inventory:
            print("[1] Använd rustning")
            print("[2] Lämna i inventory")
            equip_rustning = int(input("Vill du använda din rustning?"))
            if equip_rustning == 1:
                inventory.pop("rustning")
                
        #Om man väljer inventory, så ska man sedan kunna gå vidare till dörrarna
    elif val == 2:
        print("Du har kommit fram till dörrarna!")
        dörr_nummer = int(input("välj mellan dörr nummer 1, 2 eller 3 "))
        if dörr_nummer == 1:
            print(slumptal)

            if slumptal == 1:
                print("Monster!")
                print(monster)

                if monster <= 10:
                    print()

            
            elif slumptal == 2:
                print("Tressure!")
                print(tressure)
                if tressure <= 15:
                    inventory.append("rustning")
                    print("rustning!")
                
                elif 15 < tressure <= 30:
                    inventory.append("healthpotion")
                    print("Healthpotion!")
                
                elif tressure > 30: 
                    inventory.append("glass")
                    print("glass!")

                    

            elif slumptal == 3:
                print("Trap!")
                print(HP - 20)
        
        if dörr_nummer == 2:
            print(slumptal)

            if slumptal == 1:
                print("Monster!")
                #Måste fixa så att monstren slumpas och de olika monstren gör olika mycket skada.
            
            elif slumptal == 2:
                print("Tressure!")
            
            elif slumptal == 3:
                print("Trap!")
                print(HP - 20)
                
        if dörr_nummer == 3:
            print(slumptal)

            if slumptal == 1:
                print("Monster!")
                #Måste fixa så att monstren slumpas och de olika monstren gör olika mycket skada.
            
            elif slumptal == 2:
                print("Tressure!")
            
            elif slumptal == 3:
                print("Trap!")
                print(HP - 20)
    

    



       

    




elif start == 2:
    print("Du har valt att avbryta systemet")

else:
    print("ogiltligt svar")





