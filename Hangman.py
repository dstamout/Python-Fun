import random

namebank = ["Brian", "Stevo", "Wayne", "Katie", "Tegan", "Monte"]
board = ["_", "_", "_", "_", "_"]
guessbank = []
randName = namebank[random.randint(0, len(namebank) - 1)].lower()
win = False

print("Welcome to hangman! Guess by entering a letter, and try to guess the full word!")

print(randName)

while not win:
    guess = input("\nEnter any letter (or -1 to quit): ")

    try:
        if int(guess) == -1:
            print("\n\nBye bye!!")
            break
    except:
        guess = guess.lower()

    if guess in randName:
        index = 0
        for letter in randName:
            if letter.lower() == guess:
                board[index] = guess
                print(board)
            index += 1
            if ''.join(board) == randName:
                print("\n\nYou win!!!")
                win = True
                break
    else:
        print("\nIncorrect, try again.")
    
    if guess not in guessbank and not win:
        guessbank.append(guess)
        print("\nThis is what you have guessed so far: ")
        print(guessbank)

exit()

'''Ideas:
Build a board
Add strikes
'''