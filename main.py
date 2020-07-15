import os
import functions
import time
from Classes import *





if __name__ == "__main__":
    print("""
**************************************************
Welcome to the opening of Brawlers Stars packages"
|                |      |      |                 |
|                 |     |     |                  |
|                  |    |    |                   |
|                   | | | | |                    |
**************************************************
""")


    # First Ensures if there is any player
    #todo only a function to check if exists player change all loging
    if functions.check_exists_players():
        while(True):
            print("Please Choose a name form the list.\nOr create a new new game writing a different name.\nIf ypu want to exit write end or exit.")
            print(functions.show_players())
            name = input("\n>>> ").lower() # all names will be saves on minuscule

            if name == "exit" or name == "end":
                print("Goodbye person I do not know I hope you execute me soon")
                exit()

            # If player input exists continue with this name
            elif functions.check_only_one_player_exists(name):
                print("Welcome to your game "+ name.capitalize())
                break

            else:
                if functions.not_number(name):
                    functions.create_new_user("players/"+name)
                    print("Welcome to your new game "+ name.capitalize())
                    break
                else:
                    print("Sorry you must write a no fake game ma friend")
                # but if this name not exists check if its a name an create new game


    # If there isnt any player
    else:
        while(True):
            print("There are no saved games. Please enter a name for your game. Your characters will be saved when you write end")
            name = input("\n>>> ").lower()

            if name == "fin" or name == "end":
                print("Goodbye person I do not know I hope you execute me soon")
                exit()
            elif functions.not_number(name):
                if len(name.split()) == 1:
                    print("Welcome to your new game " + name.capitalize())
                    break
                else:
                    print("Sorry this app doesn't support compound names")
                    continue
            else:
                print("Sorry your name cannot be a number")
                continue



    # after login
    comands = """
    **************************************************
    > end =             exit and save
    > exit =            exit and save
    > commands =        Show commands
    > delete game =     delete the game of the current 
                        player
    > show brawlers =   shows the brawlers letters
    > simulate "days" = begin simulate of the game The 
                        simulation of the game begins 
                        according to the days 
                        entered
    **************************************************
        """
    brawlers_cards = functions.load_dic_from_file("brawlers")
    cards_player = functions.load_dic_from_file("players/" + name)
    brawlers = RandomCards(brawlers_cards)

    print("Enter a command from the list:\n"+comands)
    while(True):
        elec = input(">>> ").lower()
        if elec== "exit" or elec == "end":
            print("Good bye "+ name.capitalize() +" See you latter")
        elif elec == "commands" or elec == "command":
            print(comands)

        elif elec.split()[0] == "delete" and elec.split()[1] == "game":
            print("Your Game was deleted\nBye " + name.capitalize())
            #todo delete file of current player
            exit()

        elif elec == "comands" or elec == "comand":
            print(comands)

        elif elec.split()[0] == "show" and elec.split()[1] == "brawlers":
            print(brawlers)

        elif len(elec.split()) == 2 and elec.split()[0] == "simulate" and not functions.not_number(elec.split()[1]):
            days = int(elec.split()[1])
            if days > 0 and days <= 10:
                print("working in yout simulate simulate...\nYour cards are")
                time.sleep(3)
                for i in range(days):
                    # todo write it on the loop Player class and after that check for type or win RandomCards Class
                    print(brawlers.random_card())
            else:
                print("the days must be a number between 1 and 10")

        else:
            print("Sorry the command is invalid")
