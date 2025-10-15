import random

inventory = []
basement_unlocked = False

def Home():
    print("\nYou are home. Where do you want to go?")
    print("GO UPSTAIRS, WALK TO KITCHEN, ENTER LIVING ROOM, GO TO BATHROOM, or TRY BASEMENT")
    antwoord = input("> ").upper()
    if antwoord == "GO UPSTAIRS":
        Upstairs()
    elif antwoord == "WALK TO KITCHEN":
        Kitchen()
    elif antwoord == "ENTER LIVING ROOM":
        LivingRoom()
    elif antwoord == "GO TO BATHROOM":
        Bathroom()
    elif antwoord == "TRY BASEMENT":
        Basement()
    else:
        print("I don't understand...")
        Home()

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

def Upstairs():
    print("\nYou are upstairs. Options:")
    print("GO TO ROOM, GO TO ATTIC, or GO BACK")
    antwoord = input("> ").upper()
    if antwoord == "GO TO ROOM":
        Room()
    elif antwoord == "GO TO ATTIC":
        Attic()
    elif antwoord == "GO BACK":
        Home()
    else:
        Upstairs()

def Room():
    print("\nYou are in your room. Options:")
    print("START GAMING, LIE IN BED, or GO BACK")
    antwoord = input("> ").upper()
    if antwoord == "START GAMING":
        Gaming()
    elif antwoord == "LIE IN BED":
        print("You lie in bed... Goodnight.")
        quit()
    elif antwoord == "GO BACK":
        Upstairs()
    else:
        Room()

def Gaming():
    print("\nPC Booted. Options: HEARTS OF IRON IV, GEOMETRY DASH, or EXIT PC")
    antwoord = input("> ").upper()
    if antwoord == "HEARTS OF IRON IV":
        HOI4()
    elif antwoord == "GEOMETRY DASH":
        GD()
    elif antwoord == "EXIT PC":
        print("You shut down your PC.")
        Room()
    else:
        Gaming()

def HOI4():
    print("\nChoose a country: GERMANY, ITALY, SWEDEN, or GO BACK")
    land = input("> ").upper()
    if land in ["GERMANY", "ITALY", "SWEDEN"]:
        print(f"You are playing as {land}. Go FASCIST or MONARCHIST?")
        ideologie = input("> ").upper()
        if ideologie in ["FASCIST", "MONARCHIST"]:
            print(f"You turned {land} into a {ideologie} power. The campaign ends, you quit the game.")
            Room()
        else:
            HOI4()
    elif land == "GO BACK":
        Gaming()
    else:
        HOI4()

def GD():
    print("\nLevels: GRIND BLOODBATH, REPLAY ULTRA VIOLENCE, or GO BACK")
    level = input("> ").upper()
    if level == "GRIND BLOODBATH":
        print("\n3 hours have passed... Would you like to GO TO BED or GO DOWNSTAIRS?")
        keuze = input("> ").upper()
        if keuze == "GO TO BED":
            print("You collapse in bed. Goodnight.")
            quit()
        elif keuze == "GO DOWNSTAIRS":
            Home()
    elif level == "REPLAY ULTRA VIOLENCE":
        print("You replayed Ultra Violence. Satisfied, you stop playing.")
        Room()
    elif level == "GO BACK":
        Gaming()
    else:
        GD()

def Attic():
    global basement_unlocked
    print("\nYou climb into the attic. It's dark and eerie.")
    print("You see an old CHEST or you can GO BACK.")
    antwoord = input("> ").upper()
    if antwoord == "CHEST":
        print("\nInside the chest you find... a rusty KEY!")
        inventory.append("Rusty Key")
        basement_unlocked = True
        print("You hurry back downstairs, clutching the key tightly.")
        Home()
    elif antwoord == "GO BACK":
        Upstairs()
    else:
        Attic()

def LivingRoom():
    print("\nYou are in the living room. You see a TV and a bookshelf.")
    print("WATCH TV, CHECK BOOKS, or GO BACK")
    antwoord = input("> ").upper()
    if antwoord == "WATCH TV":
        print("You watch TV for a while. A strange static appears, whispering your name...")
        LivingRoom()
    elif antwoord == "CHECK BOOKS":
        print("Among dusty books, you find a note: 'Don’t trust the doll.'")
        inventory.append("Strange Note")
        LivingRoom()
    elif antwoord == "GO BACK":
        Home()
    else:
        LivingRoom()

def Bathroom():
    print("\nYou are in the bathroom. Options: LOOK IN MIRROR, OPEN CABINET, GO BACK")
    antwoord = input("> ").upper()
    if antwoord == "LOOK IN MIRROR":
        print("Your reflection smiles back... but you are not smiling.")
        Bathroom()
    elif antwoord == "OPEN CABINET":
        print("You find some medicine and add it to your inventory.")
        inventory.append("Medicine")
        Bathroom()
    elif antwoord == "GO BACK":
        Home()
    else:
        Bathroom()

def Basement():
    global basement_unlocked
    if not basement_unlocked:
        print("\nThe basement door is locked. You need a key.")
        Home()
    else:
        print("\nYou unlock the basement with the rusty key...")
        print("Inside, it’s pitch black. You hear footsteps behind you.")
        print("GAME OVER – The shadows claimed you.")
        quit()

# Start the game
Home()
