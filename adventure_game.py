import time
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def restart_choice():
    print_pause("Would you like to play again?")
    restart_choice = input ("Would you like to play again (y/n)\n")
    if restart_choice == "y":
        play_game()

def play_game():
    items = []
    intro()
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input ("Please enter 1 or 2 \n")

    if choice == '1':
        knock_on_door(items)
    elif choice == '2':
        peer_into_cave(items)
        

def intro():
    print_pause("You find yourself standing in an open field, " 
                "filled with grass and yellow wild flowers. "
                "Rumor has it that a wicked fairie is somewhere around here, "
                "and has been terrifying the nearby village.")    
    print_pause("In front of you is a house "
                "To the right of you is a dark and spooky cave ")
    print_pause("In your hand you hold your trusty and rusty (but ineffective) dagger.")


   

def knock_on_door(items):
    print_pause("You step forward and knock on the door of the house... "
                "An evil fairy with stringy white hair and a goti appears.")
    print_pause("Yikes this is the Wicked Fairy's House! "
                "The wicked fairy attacks you. "
                "You feel that the odds are definitely against you" 
                "especially with this small dagger.")
    choice = input ("What would you like to do? (1) Fight or (2) Run Away")
    if "(1) Fight" in choice:
        print_pause("(1) Fight")
        print_pause("You do your best... "
                    "but your dagger is no match for the fairy. "
                    "You have been defeated!")
        if restart_choice == "y":
            print_pause("Excellent! Restarting the Game")
            play_game()
        else:
            print_pause("Thank's for playing! See you next time.")
        if "(1) Fight" in choice and "sword" in items:
            print_pause("You step forward and knock on the door. "
                        "An evil fairy with stringy white hair " 
                        "and a goti appears."
                        "The wicked fairy attacks you! "
                        "But he is no match for 'the sword of thorvath'")
            print_pause("You defeat the fairy! You win!")
            print_pause("Would you like to play again? (y/n)")
            items.append('sword')
            if restart_choice == "y":
                print_pause("Excellent! Restarting the Game")
                play_game()
        else:
            print_pause("Thank's for playing! See you next time.")            
    if "(2) Run Away" in choice:
        print_pause("(2) Run Away")
        print_pause("You retreat back into the field. Luckily, you dont seem to have been followed")
        play_game()

def peer_into_cave(items):
    print_pause("You step back and see a dark, damp cave off to this distance.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back to the field.")
        play_game()
    else:    
        print_pause("You peer cautiously into the cave and " 
                    "you see embedded into a diamond encrusted stone...")
        print_pause("The magical sword of Thorvath!")
        print_pause("Throwing aside your useless old dagger, "
                    "you run to the back of the cave to retrieve the sword")        
        print_pause("You take the sword and run out of the cave into the field.")
        print_pause("You feel INVINCIBLE!")
        items.append("sword")
        play_game()


play_game()        
   


                   
                 


