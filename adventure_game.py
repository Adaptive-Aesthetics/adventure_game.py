import time
import random


items = []
all_monsters = ['Fairy', 'Dragon', 'Ogre', 'Gorgon' ]

selected_monster = random.choice(list(all_monsters))

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wild flowers.  " 
                "Rumor has it that a wicked "+selected_monster+" is somewhere around here "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house "
                "To the right of you is a dark and spooky cave ")
    print_pause("In your hand is your trusty and rusty (but ineffective) dagger.")

def knock_on_door():
    if "sword" in items:
        print_pause("You step forward and knock on the door of the house "
                    "An evil "+selected_monster+" with stringy white hair and a goti appears "
                    "The wicked "+selected_monster+" ATTACKS YOU!")
        print_pause("But he is no match for 'The sword of Thorvath!'")
        print_pause("You DEFEAT the "+selected_monster+" ! YOU WIN!")
        restart_choice = input("Would you like to play again? (y/n)\n")
        if restart_choice == "y":
            print_pause("Excellent! Restarting the game.")
        elif restart_choice == "n":
            print_pause("Thanks for playing! See you next time.")
            
        else:
            print_pause("Sorry, try again!")    
    else:
        print_pause("You step forward and knock on the door of the house "
                    "An evil "+selected_monster+" with stringy hair and a goti appears.")
        print_pause("Yikes! This is the wicked "+selected_monster+"'s house")
        print_pause("The wicked "+selected_monster+" ATTACKS YOU!")
        print_pause("You feel that the odds are definitely against you, especially with this small dagger.")
        choice = input ("What would you like to do? (1) Fight (2) Run Away")
        if choice == '1':
            print_pause("(1) Fight")
            print_pause("You do your best... "
                        "but your dagger is no match for the "+selected_monster+".")
            print_pause("You have been DEFEATED!")
            restart_choice = input("Would you like to play again? (y/n)\n")
            if restart_choice == "y":
                print_pause("Excellent! Restarting the game.")
            elif restart_choice == "n":
                print_pause("Thanks for playing! See you next time.")
                exit
            else:
                print_pause("Sorry, try again!")
        elif choice == '2':
            print_pause("(2) Run Away")
            print_pause("You retreat back into the field. "
                        "Luckily you don't seem to have been followed")
        else:
            print_pause("Sorry, try again!")

def peer_into_cave():
    print_pause("You step back and see a dark, damp cave off into the distance")
    if "sword" in items:
        print_pause("You peer cautiously into the cave. You've been here before, and gotten all the good stuff. " 
                    "It's just an empty cave now. You walk back out to the field. ")
    else:
        print_pause("You peer cautiously into the cave and you see embedding into a diamond encrusted stone ")
        print_pause("The magical sword of Thorvath!")
        print_pause("Throwing aside your useless old dagger, "
                    "you run to the back of the cave to retrieve the sword ")
        print_pause("You take the sword and run out of the cave into the field.")
        print_pause("You feel INVINCIBLE!")
        items.append("sword")

intro()

while True:
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input ("Please enter 1 or 2 \n")
    if choice == '1':
        knock_on_door()
    elif choice == '2':
        peer_into_cave()
    else:
        print_pause("Sorry, try again!")        



                           




