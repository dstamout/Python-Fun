import random

# Board builder helper
def build(name):
    board = []
    for letter in name:
        if letter == " ":
            board.append(" ")
        else:
            board.append("_")
        
    return board

# Bank of words
namebank = ["Joseph", "Abu Abdo", "Wayne", "Dimitrios", "Tegan", "Gerasimos"]
guessbank = []
# Random name generator
randName = namebank[random.randint(0, len(namebank) - 1)].lower()
# Board build (call to helper)
board = build(randName)
win = False
strikes = 0
STRIKE_MAX = 5

print("Welcome to hangman! Guess by entering a letter, and try to guess the full word!")

# Game loop
while not win:
    guess = input("\nEnter any letter (or -1 to quit): ")

    # If -1 entered, quit. Else, continue
    try:
        if int(guess) == -1:
            print("\nBye bye!!")
            break
    except:
        guess = guess.lower()

    # If guess was a letter of word
    if guess in randName:
        index = 0
        # Loop through word, find letter and fill in board accordingly
        for letter in randName:
            if letter.lower() == guess:
                board[index] = guess
            index += 1
            # Win condition
            if ''.join(board) == randName:
                win = True
                break
        print("\n" + ' '.join(board))
    # Incorrect guess handle (increment strike)
    else:
        strikes += 1
        print("\nIncorrect, you have " + str(STRIKE_MAX - strikes) + " strikes left.")

    # Fill guessbank with unique guesses
    if guess not in guessbank and not win:
        guessbank.append(guess)
        print("\nThis is what you have guessed so far: ")
        print(guessbank)

    # Strike condition
    if strikes == STRIKE_MAX:
        print("\nYou ran out of strikes, you lose. Good game!")
        win = False
        break

# Win print
if win:
    print("\nYou win!!!")

exit()