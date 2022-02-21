import random

user = str(input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: "))
computer = random.choice(['r', 'p', 's'])

if user == computer:
    print('it\'s a tie')
elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
    print('you won')
else:
    print('you lost')