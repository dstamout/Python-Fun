import random

print("Welcome to the guessing game!")

while True:
    inp = input("Please enter a number from 1-20 (or -1 to quit): ")

    rand = random.randint(1, 20)

    if int(inp) == rand:
        print("You win! Good job, I guess?")
    elif int(inp) == -1:
        print("Bye!")
        break
    else:
        print("Ehh, wrong. The correct number was " + str(rand))

exit()