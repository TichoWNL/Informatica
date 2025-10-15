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