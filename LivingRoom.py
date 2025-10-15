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

