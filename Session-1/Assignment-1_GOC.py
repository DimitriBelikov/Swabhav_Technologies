# Game of Chances
from random import randint
def roll_dice():
    dice1, dice2 = randint(1, 6), randint(1, 6)
    dice_total = dice1 + dice2
    return dice_total

def game_of_chances():
    game_end_status = False
    while(game_end_status == False):
        dice_total = roll_dice()
        print('--> You rolled a {}'.format(dice_total))

        if dice_total in [7, 11]:
            print('\n*** YAY!! U Win on the first roll ***')
            game_end_status = True
        
        elif dice_total in [2, 3, 12]:
            print('\n*** CRAPS !!! Sorry U lost the game ***')
        
        else:
            print('*** POINT!!... Roll untill u receive {} again. ***'.format(dice_total))
            dice_total1 = 0
            while(dice_total1 != dice_total):
                dice_total1 = roll_dice()
                print('--> You rolled a {}'.format(dice_total1))

                if dice_total1 == 7:
                    print('\n*** Shit! U rolled a 7 before making a Point. You Lose!! ***')
                    break
                elif dice_total == dice_total1:
                    print('\n*** Congrats!! You made the POINT. U win!! ***')
        game_end_status = True

game_of_chances()