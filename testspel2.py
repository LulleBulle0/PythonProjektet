#Installerar simple_Colors! -----------------------------
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import simple_colors
except ImportError:
    print("simple_colors inte installerat. Installerar nu...")
    install_package("simple_colors")

#--------------------------------------------------------

import simple_colors
import random
import ASCII_art as ascii
import os

os.system("cls")

print(simple_colors.green(ascii.text("Through the trollgate")))



class Game:
    def __init__(self):
        self.player = None
        self.difficulty = None

    def start(self):
        print(simple_colors.yellow("HEJ! VÄLKOMMEN TILL THROUGH THE TROLLGATE! "))
        name = input("VAD ÄR DITT NICKNAME? ")
        while True: 
            self.difficulty = input(f"Vilken svårighetsgrad vill du spela på? \n{simple_colors.green("[1] Lätt 10 hp")}\n{simple_colors.yellow("[2] Medel 8 hp")}\n{simple_colors.red("[3] Svårt 6 hp)")}\n>")
            if self.difficulty == "1":
                hp = 10
                break
            elif self.difficulty == "2":
                hp = 8
                break
            elif self.difficulty == "3": 
                hp = 6
                break
            else: 
                print(simple_colors.red("Ogiltigt svar!"))

        self.player = Player(name = name, hp = hp, strength = 30, level = 0, inventory = Inventory())

        self.main_menu()
           
    
    def main_menu(self):
        while self.player.hp > 0:
            print("\n----------------------")
            choice = input("Vad vill du göra? \n[1] Öppna en dörr\n[2] Titta i din ryggsäck\n[3] Se dina egenskaper\n[4] Avsluta\n> ")
            if choice == "1":
                self.enter_doors()
            elif choice == "2":
                self.player.inventory.show()
            elif choice == "3": 
                self.player.show()
            elif choice == "4": 
                break
            else:
                print("Ogiltigt val!")

            if self.player.level >= 10: 
                print(simple_colors.yellow("Grattis!!! Du klarade spelet!"))
                break
            if self.player.hp <= 0:
                break    
        print(simple_colors.yellow("Spelet är över!" if self.player.hp <= 0 else "Tack för att du spelade!"))
    
    def enter_doors(self):
        if input("Välj dörr [1] VÄNSTER, [2] MITTEN, [3] HÖGER: ") in ["1", "2", "3"]:
            random.choice([self.monster_event, self.chest_event, self.trap_event])()
        else:
            print("Ogiltigt val!")
    
    def monster_event(self):
        print(simple_colors.red("\nDet är ett monster!"))
        self.player.fight(monster = Monster())
    
    def chest_event(self):
        self.player.found_chest(chest = Chest())
        

    def trap_event(self):
        self.player.got_cought(trap = Trap())

ITEM_SWORD = ("Svärd", 20)
ITEM_HELTH_POTION = ("Hälsodryck", 10)
ITEM_SHIELD = ("Sköld", 15)

class Item:
    item_types = [ITEM_SHIELD, ITEM_HELTH_POTION, ITEM_SWORD] # "Glass" skulle kunna ge HP

    def __init__(self):
        random_item = random.choice(self.item_types)
        self.name = random_item[0]
        self.strength = random_item[1]

    def start_item(self, item):
        self.name = item[0]
        self.strength = item[1]
        return(self)

    def show(self):
        print(simple_colors.yellow(f"{self.name}\tSTYRKA: {self.strength}"))
    
class Inventory: 
    inventory = []

    def get_items(self): 
        return self.inventory
    
    def add_item(self, item): 
        if len(self.inventory) < 5: 
            # ryggsäck inte full, lägg till pryl
            self.inventory.append(item)
        else: 
            # ryggsäck full, ersätta pryl?
            if (isinstance(item, Item)):
                print(f"Din ryggsäck är full!")
                self.show()
                while True: 
                    try: 
                        svar = int(input("\nErsätt pryl i ryggsäck genom att ange position eller 0 för att skippa: "))
                        if 1 <= svar <= 5: 
                            break
                        elif svar == 0: 
                            print("\nInget ersattes, du lämnde kvar skattkistan i skogen! ")
                            return
                        else:
                            print(simple_colors.red("FEL: Du måste ange en position i ryggsäcken, ett tal mellan 1 och 5 eller 0 för att skippa! "))
                    except ValueError: 
                        print(simple_colors.red("FEL: Du måste ange ett heltal! Försök igen "))
            
                self.replace_item(svar - 1, item)
                self.show()
                             
    def replace_item(self, item_index, item):
        if item_index >= len(self.inventory): 
            print(simple_colors.red("Den platsen finns inte!"))
        else:
            self.inventory[item_index] = item

    def show(self): 
        index = 0
        print(simple_colors.yellow("\nRYGGSÄCK:"))
        print("---------")
        for item in self.inventory:
            if isinstance(item, Item):
                print(f"{index + 1}. {item.name}\t{item.strength}") 
                index += 1
        return ""
    
    def total_strength(self): 
        total_styrka = 0
        for item in self.inventory: 
            # if isinstance(item, Item):
            total_styrka += item.strength
        return total_styrka
    
class Chest: 
    def __init__(self): 
        self.item = Item()
  
class Player:
    def __init__(self, name, hp, strength, level, inventory):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.level = level
        self.inventory = inventory
    

    def fight_won(self, monster_name): 
        self.level += 1

        print(simple_colors.green(f"Du vann fighten mot {monster_name} och din nya level är {self.level}"))
        
    def fight_lost(self, monster_name): 
        self.hp -= 1
        print(simple_colors.yellow(f"Du förlorade fighten mot {monster_name} och din nya HP är: {self.hp}"))

    def fight(self, monster): 
        self.strength
        bonus_strength = 0
        if (isinstance(self.inventory, Inventory)):
            items_in_inventory = self.inventory.get_items()
            for item in items_in_inventory: 
                if (isinstance(item, Item)):
                    bonus_strength += item.strength

            total_strength = self.strength + bonus_strength

            if total_strength > monster.strength: 
                self.fight_won(monster.name)
            
            elif total_strength < monster.strength: 
                self.fight_lost(monster.name)

            else: 
                print(simple_colors.yellow("Fighten blev oavgjord, monstret försvann! "))

    def got_cought(self, trap): 
        if(isinstance(trap, Trap)): 
            self.hp -= trap.damage
            if trap.name == "Fallnät": 
                print(simple_colors.yellow(f"\nDu fick ett fallnät över dig, du förlorade {trap.damage} HP! "))

            elif trap.name == "Björnfälla": 
                print(simple_colors.yellow(f"\nDu snubblade in i en björnfälla, du förlorade {trap.damage} HP! "))

            else: 
                print(simple_colors.yellow(f"\nDu trillade ner i en varggrop, du förlorade {trap.damage} HP! "))

    def found_chest(self, chest): 
        if(isinstance(chest, Chest)): 
            print(simple_colors.yellow("\nDU HITTADE EN SKATTKISTA!"))
            print("DEN INNEHÖLL: ", end="")
            chest.item.show()
            self.inventory.add_item(chest.item)

    def show(self): 
        egen_styrka = self.strength
        inventory_styrka = self.inventory.total_strength()
        total_styrka = egen_styrka + inventory_styrka
        print(f"\nHEJ {self.name}!")
        print(simple_colors.yellow("\nDINA EGENSKAPER"))
        print("---------------")
        print(f"HP:\t{self.hp}")
        print(f"LEVEL:\t{self.level}")
        print(f"STYRKA:\t{egen_styrka} + {inventory_styrka} = {total_styrka}")
        # print(f"{inventory.show()}")

class Trap: 
    trap_types = [("Fallnät", 0.5), ("Björnfälla", 2), ("Varggrop", 1)]

    def __init__(self):
        random_trap = random.choice(self.trap_types)
        self.name = random_trap[0]
        self.damage = random_trap[1]
    
class Monster: 
    monster_types = [("Lilltrollet", 35), ("Jätten", 60 ), ("Dunderklumpen", 90)]

    def __init__(self):
        random_monster = random.choice(self.monster_types)
        self.name = random_monster[0]
        self.strength = random_monster[1]

Game().start()

# inventory = Inventory()
# item_sword = Item().start_item(ITEM_SWORD)
# item_helth_potion = Item().start_item(ITEM_HELTH_POTION)
# inventory.add_item(item_sword)
# inventory.add_item(item_helth_potion)


# player = Player(name = "Pontus", hp = 10, strength = 30, level = 0, inventory = inventory)
# player.show() 






# rownumber = 1

# while True: 
#     trap = Trap()
#     print(f"{rownumber} {trap.name}\t{trap.damage}")
#     rownumber = rownumber + 1 
#     if rownumber >= 10: 
#         break

# for i in range(1,11): 
#     monster = Monster()
#     print(f"{i} {monster.name}\t{monster.strength}")

    
# print("Test av slumpad pryl (ITEM)")
# print("---------------------------")
# item = Item()
# print(f"Pryl = {item.name}, styrka = {item.strength}")

# print("\nTest av ryggsäck (INVENTORY) med fler än 5 slumpade prylar (ITEMs)")
# print("------------------------------------------------------------------")
# inventory = Inventory()
# inventory.add_item(Item())
# inventory.add_item(Item())
# inventory.add_item(Item())
# inventory.add_item(Item())
# inventory.add_item(Item())
# inventory.add_item(Item())

# print("\nTest av kista (CHEST) med slumpad pryl (ITEM)")
# print("---------------------------------------------")
# chest = Chest()
# if (isinstance(chest.item, Item)):
#     chest.item.show()
