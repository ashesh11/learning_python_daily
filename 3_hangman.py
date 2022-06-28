import random
from traceback import print_tb
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks', 'reeks']

word = random.choice(words)
filtered_word = list(dict.fromkeys(sorted(word)))

chance = len(word)

print("\nGame begins:")
print("You have ",chance,"chances to guess the following word.")

print()
guesses = ''
while chance>0:
    filtered_guesses = list(dict.fromkeys(sorted(guesses)))
    
    for char in word:            
        if char in guesses:
            print(char, end=" ")
        else:
            print('_', end=" ")

    if filtered_guesses == filtered_word:
        print("\n\t\tCongrats!! You win.")
        print("\t\tYou found the word", word,'.')
        break
    else:
        guess = input("\n\nPlease enter a guess letter: ")
        if guess in word:
            guesses += guess
            print("Correct Guess. Next guess please!!")
        else:
            chance -= 1
            if chance == 0:
                print("You have no chance left. You lost!!")
                break
            else:
                print("Incorrect Guess. You now have ",chance,"chance to guess the word.")
input("")