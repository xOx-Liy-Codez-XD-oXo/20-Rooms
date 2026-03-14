"""

Program Name:
    20 Rooms

Program Description:
    "Filler."

Author:
    L. A.

Code Update Date:
    03/13/26

"""


import random

from story.beginning import beginning

from game.rps import rps
from game.rps_SD import rps_SD

def main():

    beginning() # Introductory print text when you first start the program
    startGame = True # Begin the actual game

    while startGame: # Keep
        health = int(100)  # Start/restart user health
        inventory = ['', '', '']  # Start/restart user inventory
        room = int(1) # Start/restart room number to "Room 1"
        gameLoop = True # Activate regular loop of the game

        if play_again().called:
            print("\nYou wake up on the floor of one of the rooms, again. The shady forearms immediately immerge from the front of the room's darkness.\n")
            print("\"ANOTHER GO, HUH?\"\n")
            print("You get up, and walk over to it before posing your hands and arms for another match.")
            print("It follows suit.\n")
            print("\"LET'S SEE IF YOU CAN GET LUCKY ENOUGH, THIS TIME.\"\n")
            print("A bright-red '1' appears in your mind's eye, once more.\n")

        while gameLoop:
            match = ''

            if room >= 1 and room <= 20:
                if room == 10 or room == 20:
                    print("\n'SUDDEN DEATH'")
                    print("'1-OUT-OF-1 MATCH'\n")
                    print("'BE READY'\n")
                    rps_SD()

                    if rps_SD() == True:
                        match = 'won'

                    elif rps_SD() == False:
                        match = 'lost'

                else:
                    rps()

                    if rps() == True:
                        match = 'won'

                    elif rps() == False:
                        match = 'lost'

                if match == 'won':
                    if inventory[0] != '' and inventory[1] != '' and inventory[2] != '':
                        print("\nYour inventory is full, so the item disappears.")
                    item
                    room = room + int(1)

                elif match == 'lost':
                    entity

                    if health < int(1):
                        death_screen()
                        play_again()

                        if play_again() == True:
                            play_again().called = True
                            gameLoop = False

                        elif play_again() == False:
                            startGame = False

            else:
                gameLoop = False

        startGame = False


if __name__ == "__main__":
    main()