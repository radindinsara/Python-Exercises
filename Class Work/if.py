while True:

    type = input("What is you type(Elves,Ghost,Wizard): ").lower()
    if type == "Elves" or type == "Ghost" or type == "Wizard":
        print("Invalid Type.")
        exit()

    age = int(input("What is you age: "))

    if type == "Elves" and age > 100:
        print("You can buy Leaf Drinks and sparking water")
    elif type == "Elves" and age < 100:
        print("You can buy sparking water")
    elif type == "Ghost":
        print("You can buy Leaf Drinks and dust cookies")
    elif type == "Wizard" and age > 21:
        print("You can buy sparking water and wine")
    else:
        print("You can buy sparking water.")

