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
