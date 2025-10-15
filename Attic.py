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