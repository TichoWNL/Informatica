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

