# print("[1]Spela!")
# print("[2]Avbryt")
# start = int(input("Är du redo för att spela? "))

# import random

# slumptal = random.randint(1, 3)
# monster = random.randint(1, 100)
# tressure = random.randint(1, 100)

# def Troll():
#     print("Monster!")
#     print(monster)

#     if monster <= 10:
#         print()

# def kista():
#     print("Tressure!")
#     print(tressure)
#     if tressure <= 15:
#         inventory.append("sheild")
                
#     elif 15 < tressure <= 30:
#         inventory.append("healthpotion")
                
#     elif tressure > 30: 
#          inventory.append("glass")

# def fälla():
#     print("Trap!")
#     print(HP - 20)

# jHP = 40
# tHP = 30
# sHP = 15


# if start == 1:
#     print("Spelet startas!")
    
#     inventory = []

#     print("[1] Lätt")
#     print("[2] Medel")
#     print("[3] Svårt")
#     Svårhetsgrad = int(input("Välj din svårhetsgrad "))

#     if Svårhetsgrad == 1:
#         HP = 100
#         print("---Ditt HP---")
#         print(HP)
#         inventory.append("Svärd")
#     elif Svårhetsgrad == 2:
#         HP = 75
#         print("---Ditt HP---")
#         print(HP)
#         inventory.append("svärd")
#     elif Svårhetsgrad == 3:
#         HP = 50
#         print("---Ditt HP---")
#         print(HP)
#         inventory.append("svärd")
    
#     else:
#         print("Ogiltligt svar!")

#     while True:
#         print("---MENY---")
#         print("[1] Inventory")
#         print("[2] Gå till första dörrarna")
#         val = int(input("Vad vill du göra? "))

#         if val == 1:
            
#             print(F"""
#         Ditt inventory:
#         {inventory}
#             """)
#             #Om man väljer inventory, så ska man sedan kunna gå vidare till dörrarna
            

#         elif val == 2:
#             print("\nDu har kommit fram till dem första dörrarna!")
#             input("Vill du gå in i dörr 1, 2 eller 3?")
            

    
#             events = ["monster", "kista", "fälla"]
                
#             roomChoice = input("> ")
                
#             if(roomChoice in ["1", "2", "3"]):
#                 event = random.choice(events)

#                 if (event == "monster"):
#                     Troll()
#                 elif (event == "kista"):
#                     kista()
#                 elif (event == "fälla"):
#                     fälla()

    



# elif start == 2:
#     print("Du har valt att avbryta systemet")

# else:
#     print("ogiltligt svar")



import random

class Player:
    def __init__(self, difficulty):
        self.HP = {"1": 100, "2": 75, "3": 50}.get(difficulty, 0)
        self.inventory = ["Svärd"] if self.HP else []
    
    def add_item(self, item):
        self.inventory.append(item)
        print(f"Du hittade en {item}!")

    def take_damage(self, damage):
        self.HP -= damage
        print(f"Du tog {damage} skada! Nuvarande HP: {self.HP}")

class Game:
    def __init__(self):
        self.player = None

    def start(self):
        if input("[1] Spela!\n[2] Avbryt\n> ") == "1":
            difficulty = input("[1] Lätt\n[2] Medel\n[3] Svårt\n> ")
            self.player = Player(difficulty)
            if not self.player.HP:
                print("Ogiltigt val! Spelet avslutas.")
                return
            self.main_menu()
        else:
            print("Spelet avslutas. Hej då!")
    
    def main_menu(self):
        while self.player.HP > 0:
            choice = input("[1] Inventory\n[2] Dörrar\n> ")
            if choice == "1":
                print(f"Ditt inventory: {self.player.inventory}")
            elif choice == "2":
                self.enter_doors()
            else:
                print("Ogiltigt val!")
            
            if self.player.HP <= 0:
                break
            if input("Fortsätta spela? (ja/nej): ").lower() != "ja":
                break
        print("Spelet är över!" if self.player.HP <= 0 else "Tack för att du spelade!")
    
    def enter_doors(self):
        if input("Välj dörr [1, 2, 3]: ") in ["1", "2", "3"]:
            random.choice([self.monster_event, self.chest_event, self.trap_event])()
        else:
            print("Ogiltigt val!")
    
    def monster_event(self):
        print(f"Ett monster dyker upp! Styrka: {random.randint(1, 100)}")
    
    def chest_event(self):
        loot = random.randint(1, 100)
        if loot <= 15:
            self.player.add_item("Sköld")
        elif loot <= 30:
            self.player.add_item("Hälsodryck")
        else:
            self.player.add_item("Glass")
    
    def trap_event(self):
        self.player.take_damage(20)

# Starta spelet
Game().start()
