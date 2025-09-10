import random

def roll_dice(faces):
    return random.randint(1, faces)

faces = int(input("Enter the number of faces on the die: "))

while True:
    result = roll_dice(faces)
    print(result)
    if result == faces:
        break