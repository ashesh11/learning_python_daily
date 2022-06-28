import random

human = input("Enter 'r' for rock or 's' for scissors or 'p' for paper: ")
computer = random.choice(['r', 'p', 's'])
print(computer)

def play():
    if human == computer:
        return "Its a tie!!"

    if is_win(human, computer):
        return 'You win!!'
    
    return 'You lost!!'
    

def is_win(player, computer):
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') \
         or (player == 'p' and computer == 'r'):
         return True

print(play())
