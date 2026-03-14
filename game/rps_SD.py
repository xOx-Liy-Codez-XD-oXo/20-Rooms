"""

Inputs:
    None

Outputs:
    True or False

"""


import random
from random import randint

choiceWords = ['rock', 'paper', 'scissors']
score = [0, 0]
win = ''


def getDarkMove():
    ran = randint(0, 2)
    print("It chose " + choiceWords[ran] + ".")
    return ran

def getUserMove():
    enter = input("Rock, paper, scissors...: ")
    invalid = True
    while invalid:
        if enter == 'R' or enter == 'r' or enter == 'Rock' or enter == 'rock':
            print("\n'SHOOT'")
            print("\nYou chose rock.")
            return 0
            invalid = False
        elif enter == 'P' or enter == 'p' or enter == 'Paper' or enter == 'paper':
            print("\n'SHOOT'")
            print("\nYou chose paper.")
            return 1
            invalid = False
        elif enter == 'S' or enter == 's' or enter == 'Scissors' or enter == 'scissors':
            print("\n'SHOOT'")
            print("\nYou chose scissors.")
            return 2
            invalid = False
        else:
            enter = input("'ROCK, PAPER, OR SCISSORS, ONLY.' [Try again:] ")


def roundWinner(userRound, darkRound):
    global score
    if (userRound == 1 and darkRound == 0) or (userRound == 2 and darkRound == 1) or (userRound == 0 and darkRound == 2):
        print("\n'YOU WON'")
        score[0] = score[0] + 1
    elif (userRound == 0 and darkRound == 1) or (userRound == 1 and darkRound == 2) or (userRound == 2 and darkRound == 0):
        print("\n'I WON'")
        score[1] = score[1] + 1
    elif userRound == darkRound:
        print("\n'TIED.'")

def matchWinner(userMatch, darkMatch):
    global win
    if userMatch > darkMatch:
        print("'LUCKY WINNER'\n")
        print("The shroud of darkness dissipates from the front of the room. The door is now visible. An item lies in front of it.\n")
        win = True
    elif userMatch < darkMatch:
        print("'LOSER'\n")
        print("You feel a chill run down your spine as one of the darkness' hands points behind you. You turn around to look...\n")
        win = False


def rps_SD():
    global win

    while score[0] < 1 and score[1] < 1:
        userMove = getUserMove()
        darkMove = getDarkMove()
        roundWinner(userMove, darkMove)
        print(f"\nYou - {score[0]}; It - {score[1]}\n")

    if score[0] == 1 or score[1] == 1:
        matchWinner(score[0], score[1])
        return win