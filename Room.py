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

