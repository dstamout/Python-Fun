import random

namebank = ["Brian", "Stevo", "Wayne", "Katie", "Tegan", "Monte"]
board = ["_", "_", "_", "_", "_"]
randName = namebank[random.randint(0, len(namebank) - 1)]

print("Welcome to hangman! Guess by entering a letter, and try to guess the full word!")

while True:
    guess = input("Enter any letter (or -1 to quit): ")

    if guess in randName:
        index = 0
        for letter in randName:
            if letter == guess:
                board[index] = guess
                print(board)
            index += 1
            if ''.join(board) == randName:
                print("You win!!!")
                break
    elif int(guess) == -1:
        print("Bye bye!")
        break
    else:
        print("Incorrect, try again.")

exit()

'''Ideas:
Bank of guessed letters
Build a board
Add strikes
'''