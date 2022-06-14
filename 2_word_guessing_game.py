import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'reeks']

word = random.choice(words)
print("Guess the characters!!")

guesses = ''

turns = len(word)

while turns>0:

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')

    guess = input("Guess a character: ")

    if guess not in guesses:
        guesses += guess

    elif guess in guesses:
        print("You have already used this character.")

    if guesses.split() == word:
        for char in word:
            print(char)
        print("You found the word: ", word)
        break

    if guess not in word:
        turns -= 1
        print("Wrong!!")
        print("You have", turns, "chances left")

if turns == 0:
    print("Sorry you lose!!")