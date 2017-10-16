import random

coinUser, coinBot = 10, 10
roundOfGames = 0


def bet(dice, userin):
    if dice > 7:
        if userin == 's':
            print('the dice is: ' + str(dice), ', you lost!')
            return -1
        else:
            print('the dice is: ' + str(dice), ', you win!')
            return 1
    elif dice == 7:
        print('the dice is: ' + str(dice), ', draw!')
        return 0
    elif dice < 7:
        if userin == 's':
            print('the dice is: ' + str(dice), ', you win!')
            return 1
        else:
            print('the dice is: ' + str(dice), ', you lost!')
            return -1


while True:
    print('your coin: ' + str(coinUser), "'bot's coin: " + str(coinBot))
    dice = random.randrange(2, 13)
    userin = input("what's your bet?")
    if coinUser == 0:
        print("woops, you've lost all, game over!")
        break
    elif coinBot == 0:
        print("woops, bot's lost all, game over!")
        break
    elif userin == 'q':
        print("you quit the game!")
        break
    elif userin in 'bs':
        result = bet(dice, userin)
        coinUser += result
        coinBot -= result
        roundOfGames += 1
    else:
        print('you must input the right things!')

print("you've played " + str(roundOfGames), ' rounds\n',
      "you have " + str(coinUser) + ' coins now. bye!')
