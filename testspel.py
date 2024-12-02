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
        if input("ÄR DU REDO?\n[1] Spela!\n[2] Avbryt\n> ") == "1":
            difficulty = input("Vilken svårighetsgrad vill du spela på? \n[1] Lätt  100hp\n[2] Medel 75hp\n[3] Svårt 50hp\n> ")
            self.player = Player(difficulty)
            if not self.player.HP:
                print("Ogiltigt val! Spelet avslutas.")
                return
            self.main_menu()
        else:
            print("Spelet avslutas. Hej då!")
    
    def main_menu(self):
        while self.player.HP > 0:
            choice = input("Vad vill du göra? \n[1] Inventory\n[2] Dörrar\n[3] Se dina egenskaper\n> ")
            if choice == "1":
                print(f"Ditt inventory: {self.player.inventory}")
            elif choice == "2":
                self.enter_doors()
            elif choice == "3": 
                print(f"{self.player.HP}")
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
        print(f"Det är ett monster! Styrka: {random.randint(1, 100)}")
    
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

# # ---------------------------------------------------

# class Item:
#     item_types = [("Sköld", 15), ("Hälsodryck", 10), ("Svärd", 20)] # "Glass" skulle kunna ge HP

#     def __init__(self, name = "", strength = 0):
#         self.name = name 
#         self.strength = strength
        
#     def randomize(self):        
#         random_item = random.choice(self.item_types)
#         self.name = random_item[0]
#         self.strength = random_item[1]
#         return self

#     def to_str(self):
#         return f"{self.name}\t{self.strength}"
    
# class Inventory: 
#     inventory = []
    
#     def add_item(self, item): 
#         if len(self.inventory) < 5: 
#             self.inventory.append(item)
#         else: 
#             if (isinstance(item, Item)):
#                 print(f"Du hittade {item.name} men din ryggsäck är full!")
#                 self.show()
#                 svar = int(input("Ange siffra för att ersätta eller 0 för att skippa: "))
#                 if svar < 6 and svar > 0: 
#                     self.replace_item(svar - 1, item)
                 
#     def replace_item(self, item_index, item):
#         if item_index >= len(self.inventory): 
#             print("Den platsen finns inte!")
#         else:
#             self.inventory[item_index] = item

#     def show(self): 
#         index = 1
#         for item in self.inventory:
#             if isinstance(item, Item):
#                 print(f"{index}. {item.to_str()}") 
#                 index += 1

# class Chest: 
#     def __init__(self): 
#         self.item = Item().randomize
#         if (isinstance(self.item, Item)):
#             print(self.item.to_str())
    
# item = Item().randomize()
# print(f"Pryl = {item.name}, styrka = {item.strength}")

# inventory = Inventory()
# inventory.add_item(Item().randomize())
# inventory.add_item(Item().randomize())
# inventory.add_item(Item().randomize())
# inventory.add_item(Item().randomize())
# inventory.add_item(Item().randomize())
# inventory.add_item(Item().randomize())
# inventory.show()

# chest = Chest()
# if (isinstance(chest.item, Item)):
#     print(chest.item.to_str())

#-----------------------------------------------------------------------------------


# Game().start()

class Item:
    item_types = [("Sköld", 15), ("Hälsodryck", 10), ("Svärd", 20)] # "Glass" skulle kunna ge HP

    def __init__(self):
        random_item = random.choice(self.item_types)
        self.name = random_item[0]
        self.strength = random_item[1]

    def show(self):
        print(f"{self.name}\t{self.strength}")
    
class Inventory: 
    inventory = []
    
    def add_item(self, item): 
        if len(self.inventory) < 5: 
            # ryggsäck inte full, lägg till pryl
            self.inventory.append(item)
        else: 
            # ryggsäck full, ersätta pryl?
            if (isinstance(item, Item)):
                print(f"Du hittade {item.name} men din ryggsäck är full!")
                self.show()
                svar = int(input("\nErsätt pryl i ryggsäck genom att ange position eller 0 för att skippa: "))
                if svar < 6 and svar > 0: 
                    self.replace_item(svar - 1, item)
                    self.show()
                else: 
                    print("Inget ersatt i ryggsäcken!")
                 
    def replace_item(self, item_index, item):
        if item_index >= len(self.inventory): 
            print("Den platsen finns inte!")
        else:
            self.inventory[item_index] = item

    def show(self): 
        index = 0
        print("\nRYGGSÄCK:")
        print("---------")
        for item in self.inventory:
            if isinstance(item, Item):
                print(f"{index + 1}. {item.name}\t{item.strength}") 
                index += 1

class Chest: 
    def __init__(self): 
        self.item = Item()
    
print("Test av slumpad pryl (ITEM)")
print("---------------------------")
item = Item()
print(f"Pryl = {item.name}, styrka = {item.strength}")

print("\nTest av ryggsäck (INVENTORY) med fler än 5 slumpade prylar (ITEMs)")
print("------------------------------------------------------------------")
inventory = Inventory()
inventory.add_item(Item())
inventory.add_item(Item())
inventory.add_item(Item())
inventory.add_item(Item())
inventory.add_item(Item())
inventory.add_item(Item())

print("\nTest av kista (CHEST) med slumpad pryl (ITEM)")
print("---------------------------------------------")
chest = Chest()
if (isinstance(chest.item, Item)):
    chest.item.show()

#-----------------------------------------------------------------------------------
