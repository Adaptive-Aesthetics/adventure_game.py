import time


print("You find yourself standing in an open field, filled with grass and yellow wild flowers.")
time.sleep(2)
print("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village. ")
time.sleep(2)
print("Infront of you is a house")
time.sleep(2)
print("To the right of you is a dark and spooky cave")
time.sleep(2)
print("In your hand you hold your trusty and rusty (but ineffective) dagger.")


print("Enter 1 to knock on the door of the house.")
print("Enter 2 to peer into the cave.") 
print("What would you like to do?") 
print("Please enter 1 or 2")

choice = input ()

if choice == '1' :
    print("You step forward and knock on the door of the house.")
    print("An evil fairie with stringy white hair and a goti appears.")
    print("Yikes this is the wicked fairy's house")
    print("The wicked fairy attacks you.")
    print("You feel that the odds are definitely against you especially with this small dagger.")
    print("What would you like to do? (1) fight or (2) Run Away")

    choice = input()

    if "1" in choice :
        print("(1) fight")
        print("You do your best...")
        print("but your dagger is no match for the fairie.")
        print("You have been defeated!")
        print("Would you like to play again? (y/n)")
    else:
        print("(2) Run Away")
        print("You retreat back into the field. Luckily, you don't seem to have been followed.")

        if "y" in choice :
            print("Excellent! Restarting the game")
        else:
            print("Thanks for playing! See you next time")
                 