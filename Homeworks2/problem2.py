import random
num = random.randint(1, 100)
while True:


    print('Guess a number between 1 and 100 and if you Want to exit type 999 ')



    guess = input()
    i = int(guess)
    if i == num:
        print('You won!!!')
        break 
    elif i == 999:
               break
    elif i < num:
               print('Try Higher')
    elif i > num:
               print('Try Lower')
    
    
               
                  
    
               
    		


print('if you gussed less than 5  times you won')








