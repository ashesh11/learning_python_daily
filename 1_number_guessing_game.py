from cmath import log
from itertools import count
import math
import random

#taking inputs (lower range and upper range)
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

x= random.randint(lower, upper)  #x is the number to be guessed

print("\n\tYou have only ", round(math.log(upper-lower+1,2)), " chances to guess the number\n")

count = 0 #Initializing the number of guesses

while count < round(math.log(upper-lower+1,2)):
    count += 1

    #taking guesses from user
    print("\n\tYou have ",round(math.log(upper-lower+1,2))-count," chance left\n")
    guess = int(input("Enter your guess: "))
    
    if guess == x:
        print("Congratulations your guess ", guess, " is correct. You did it on your try number ", count, ".")
        break #once guessed loop will break
    elif x>guess:
        print("Your guess is low.")
    elif x<guess:
        print("Your guess is high.")
    
if count>=math.log(upper-lower+1,2):
    print("The number is %d" %x)
    print("Better luck next time.")


