def Kitchen():
    print("\nYou are in the kitchen. What do you do?")
    print("OPEN THE FRIDGE, OPEN A RANDOM DRAWER, or GO BACK")
    antwoord = input("> ").upper()
    if antwoord == "OPEN A RANDOM DRAWER":
        found = open_drawer()
        print("You opened the drawer and found:", found)
        inventory.append(found)
        Kitchen()
    elif antwoord == "OPEN THE FRIDGE":
        Fridge()
        Kitchen()
    elif antwoord == "GO BACK":
        Home()
    else:
        Kitchen()

def open_drawer():
    items = ["Plates", "Glasses", "Pans", "Cutlery", "Nothing", "Spoon of Destiny"]
    weights = [0.25, 0.25, 0.15, 0.15, 0.15, 0.05]
    return random.choices(items, weights=weights, k=1)[0]

def Fridge():
    food = ["Eggs", "Cheese", "Quark", "Rotten human remains"]
    choice = random.choice(food)
    print("\nYou open the fridge and find:", choice)
    if choice != "Rotten human remains":
        inventory.append(choice)