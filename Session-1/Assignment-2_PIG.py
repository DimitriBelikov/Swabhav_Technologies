from random import randint

def pig_game():
    total_score, turn_count = 0, 0
    while(total_score < 20):
        turn_count += 1
        print('\nTURN {}'.format(turn_count))
        dice_face, turn_total = 0, 0
        while(dice_face != 1):
            usr_ch = input('U wanna hold or roll (h/r): ')
            if usr_ch == 'r':
                dice_face = randint(1,6)
                print('Dice = ', dice_face)
                if dice_face == 1:
                    print('Turn over. No Score for Turn')
                    turn_total = 0
                else:
                    turn_total += dice_face

            else:
                print('Turn Total : ', turn_total)
                total_score += turn_total
                break

        print('Total Score : ', total_score)

    print('\n*** YAY!!! U finished the game in {} turns. ***'.format(turn_count))

pig_game()