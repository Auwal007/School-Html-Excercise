number = range(0 , 5).random
guess = input('Im thinking of a number between zero to five, can you guess it: ')
while True:
    if number == guess:
        break
    else:
        input('Try again: ')
print('u guessed it')