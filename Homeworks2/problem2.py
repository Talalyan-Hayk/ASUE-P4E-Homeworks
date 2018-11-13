import random

num = random.randint(1,100)
num_of_guesses = 0 
while True:
    print('Guess a number between 1 and 100 and if you Want to exit type 999 ')
    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break
        num_of_guesses += 1 
    elif i == 999:
               break
    elif i < num:
               print('Try Higher')
               num_of_guesses += 1 
    elif i > num:
               print('Try Lower')
               num_of_guesses += 1 
print('if you gussed less than 5  times you won')
print('number of guesses = ' + str(num_of_guesses)) 









