import random


def guess(x):
    random_number = random.randint(1, x)
    user_guess = 0

    while  user_guess != random_number:
        user_guess = int(input(f'Guess a number between 1 and {x}: '))
        if user_guess < random_number:
            print('Sorry, guess again. Too low.')
        elif user_guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')

