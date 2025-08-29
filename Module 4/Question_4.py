import random
number = random.randint(1,10)

while True:
    guess_num = int(input("Guess a number (1-10): "))
    if guess_num == number:
        print("Correct")
        break
    elif number < guess_num:
        print("Too high")
    else:
        print("Too low")
