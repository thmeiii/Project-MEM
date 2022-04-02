#this file will only have functions which directly relate to the UI and display text.
#all functions that just perform an action will go in helpers.py

import os
import helpers
from helpers import User

def entryMenu():
    os.system('cls')
    print("Recreation Club Membership System")
    print("-------------------------------------------------------")
    print("Main Menu")
    print("-------------------------------------------------------")
    print("Register (1) | Login (2)")
    selection = input("Selection: ")
    if selection == '1':
        register()
    elif selection == '2':
        login()
    else:
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        entryMenu()

def register():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Register")
    print("-------------------------------------------------------")
    print("Member (1) | Coach (2) | Treasurer (3)")
    accountType = input("Select account type: ")
    if accountType != '1' and accountType != '2' and accountType != '3':
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        register()
    else:
        firstName = input("First name: ")
        lastName = input("Last name: ")
        username = input("Username: ")
        password = input("Password: ")
        helpers.addUser(accountType, firstName, lastName, username, password)

def login():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Register")
    print("-------------------------------------------------------")
    print("Member (1) | Coach (2) | Treasurer (3)")
    accountType = input("Select account type: ")
    if accountType != '1' and accountType != '2' and accountType != '3':
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        login()
    else:
        username = input("Username: ")
        password = input("Password: ")
        if helpers.validUserPass(accountType, username, password):
            if accountType == '1':
                memberMainPage()
            elif accountType == '2':
                coachMainPage()
            else:
                treasurerMainPage()
        else:
            print("Error: Incorrect credentials")
            input("Press any key and enter to continue: ")
            login()

def memberMainPage():
    #
    pass

def coachMainPage():
    #options for user to choose from:
    #-send group mail to members 
    #   -this adds a line to messageBoard.txt, then when users open mail box, we just print the whole text file for them

    #-view members list (print all users with account type 1, and also the info required from the "keep a log of the members" requirement)
    #   -before displaying this list, ask how they should be sorted.
    #       1. by frequency of attendance
    #       2. by ratio of how many times they have payed and not payed

    #-add/remove members 
    #   -input username of member to remove, then remove the line from users.txt

    #-attend class
    #   -show list of all classes
    #   -ask user which class number they would like to attend 
    #   -add username to end of list of coaches who attended that class number in classes.txt

    pass

def treasurerMainPage():
    pass
    

if __name__ == "__main__":
    entryMenu()
