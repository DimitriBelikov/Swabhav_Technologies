from random import randint

def guess_game():
    mood = 'y'
    while(mood == 'y'):
        rand_number = randint(1,10)
        guess_limit, usr_guess = 3, False
        while(usr_guess == False and guess_limit>0):
            usr_numb = int(input('Please take a guess between 1 and 10 : '))
            if (usr_numb > rand_number):
                print('----->Guess Lower !!!')
            elif (usr_numb == rand_number):
                print('----->You guessed Right !!!')
                usr_guess = True
            else:
                print('----->Please Guess Higher!!!!')
            guess_limit -= 1
        if(guess_limit == 0 and usr_guess != True):
            print('----->Ohh!!! Looks llike You have exhausted your Guess Limit')
        mood = input('\nWanna Play Again(y/n) = ')

guess_game()
