import time
import random


def print_pause(introductory_message):
    print(introductory_message)
    time.sleep(3)


def intro(item, scary_object):
    print_pause("You find yourself standing in an open field, filled "
                "with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a " + scary_object + " is somewhere around "
                "here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very "
                "effective) dagger.\n")


def field(item, scary_object):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        response_1 = input("(Please enter 1 or 2.)\n")
        if response_1 == "1":
            house(item, scary_object)
            break
        elif response_1 == "2":
            cave(item, scary_object)
            break


def cave(item, scary_object):
    if "sword" in item:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nYou've been here before, and gotten all"
                    " the good stuff. It's just an empty cave"
                    " now.")
        print_pause("\nYou walk back to the field.\n")
    else:
        print_pause("\nYou peer cautiously into the cave.")
        print_pause("\nIt turns out to be only a very small cave.")
        print_pause("\nYour eye catches a glint of metal behind a "
                    "rock.")
        print_pause("\nYou have found the magical Sword of Ogoroth!")
        print_pause("\nYou discard your silly old dagger and take "
                    "the sword with you.")
        print_pause("\nYou walk back out to the field.\n")
        item.append("sword")
    field(item, scary_object)


def house(item, scary_object):
    print_pause("\nYou approach the door of the house.")
    print_pause("\nYou are about to knock when the door "
                "opens and out steps a " + scary_object + ".")
    print_pause("\nEep! This is the " + scary_object + "'s house!")
    print_pause("\nThe " + scary_object + " attacks you!\n")
    if "sword" not in item:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    while True:
        response_2 = input("Would you like to (1) fight or (2) "
                           "run away?")
        if response_2 == "1":
            if "sword" in item:
                print_pause("\nAs the " + scary_object + " moves to attack, "
                            "you unsheath your new sword.")
                print_pause("\nThe Sword of Ogoroth shines brightly in "
                            "your hand as you brace yourself for the "
                            "attack.")
                print_pause("\nBut the " + scary_object + " takes one look at "
                            "your shiny new toy and runs away!")
                print_pause("\nYou have rid the town of the " + scary_object +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou do your best...")
                print_pause("but your dagger is no"
                            "match for the " + scary_object + ".")
                print_pause("\nYou have been defeated!\n")
            game_replay()
            break
        if response_2 == "2":
            print_pause("\nYou run back into the field. "
                        "\nLuckily, you don't seem to have been "
                        "followed.\n")
            field(item, scary_object)
            break


def game_replay():
    replay = input("Would you like to play again? (y/n)").lower()
    if replay == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        start_game()
    elif replay == "n":
        print_pause("\n\n\nGame Over. Thanks for playing!\n\n\n")
    else:
        game_replay()


def start_game():
    item = []
    scary_object = random.choice(['Bull', 'Wolf', 'Dragon', 'villain',
                                  'Vampire', 'Bear', 'Beast'])
    intro(item, scary_object)
    field(item, scary_object)


start_game()
