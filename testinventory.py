inventory = []


    elif slumptal == 2:
        print("Tressure!")
        print(tressure)
    if tressure <= 15:
        inventory.append("sheild")
        print("Sheild!")
                
    elif 15 < tressure <= 30:
        inventory.append("healthpotion")
        print("Healthpotion!")
                
    elif tressure > 30: 
        inventory.append("glass")
        print("glass!")

if "sheild" in inventory:
    print("Vill du använda din sheild")

    #test för inventory funktioner