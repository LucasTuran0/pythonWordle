import random

def readInput(guess):
    with open('C:\VSCode\CPSC 230\Wordle\words-1.txt', 'r') as f:
        text = f.read()
        words = text.split()
        if guess in words:
            return True

#asks the user for their first guess
def printInstructions():
    guess = input("Enter a five-letter word: ")
    return guess

#uses the random module to select a random word from the provided text file
def getRandomWord():
    with open('C:\VSCode\CPSC 230\Wordle\words-1.txt', 'r') as f:
        text = f.read()
        words = text.split()
        word = random.choice(words)
        #print('the answer is', word)
    return word

#checks to make sure that the guess of the user is in the provided text file
def readInput(guess):
    with open('C:\VSCode\CPSC 230\Wordle\words-1.txt', 'r') as f:
        text = f.read()
        words = text.split()
        if guess in words:
            return True
        else:
            print('word is not in the list of available words')
            return False

#lets the user know what letters are still available
alpha = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
def letters(guess, answer, alpha):
    for i in range(len(guess)):
        alpha.discard(guess[i])

    for i in range(len(answer)):
        alpha.add(answer[i])

    alphaList = list(alpha)
    alphaList.sort()
    return alphaList


#initializes the answer and first user guess
answer = getRandomWord()
guess = printInstructions()
while readInput(guess) == False:
    print('Please enter a 5 letter word')
    guess = printInstructions()



#initializes a variable for how many guesses the user has left
count = 5

#loops through and checks the user guesses
for i in range(5):  

    #breaks if user wins
    if guess == answer:
        break
    

    #checks if the characters in user guess in in the word and if they are in the right spot, in the word or not at all
    for char1, char2 in zip(guess, answer):
        if char1 in answer:
            if guess.index(char1) == answer.index(char1):
                print(char1, "is in the right spot")
            else:
                print(char1, "is in the word but in the wrong spot")
    
    for char in guess:
        if char not in answer:
            print(char, "is not in the answer")

    print('you have', count, 'guesses left')

    #tells the user the letters that havent been guessed
    alphaList = letters(guess, answer, alpha)
    print('the list of available letters is: ')
    print(alphaList)

    #asks the user for their next guess
    guess = printInstructions()
    while readInput(guess) == False:
        print('Please enter a 5 letter word')
        guess = printInstructions()
    count-=1


#returns the final results of the game
if guess == answer:
    print('Congrats! The answer was', answer)
else:
    print('You ran out of guesses, the answer was', answer)