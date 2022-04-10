#this file will only have functions which directly relate to the UI and display text.
#all functions that just perform an action will go in helpers.py fghnjm

import os
import helpers
#from helpers import User

def entryMenu():
    os.system('cls')
    print("Recreation Club Membership System")
    print("-------------------------------------------------------")
    print("Main Menu")
    print("-------------------------------------------------------")
    print("Register (1) | Login (2) | Exit (0)")
    selection = input("Selection: ")
    if selection == '1':
        register()
    elif selection == '2':
        login()
    elif selection == '0':
        end()
    else:
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        entryMenu()

def register():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Register")
    print("-------------------------------------------------------")
    print("Member (1) | Coach (2) | Treasurer (3) | Go Back (4)")
    accountType = input("Select account type: ")
    if int(accountType) not in range(1,5):
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        register()
    elif int(accountType) in range(1,4):
        firstName = input("First name: ")
        lastName = input("Last name: ")
        username = input("Username: ")
        password = input("Password: ")
        if not helpers.existingUser(accountType, username):
            helpers.addUser(accountType, firstName, lastName, username, password)
            print("Success: Account created")
            input("Press any key and enter to continue to the login screen: ")
            login()
        else:
            print("An account of that type already exists for that username")
            input("Press any key and enter to go back to the home screen: ")
            entryMenu()
    else:
        entryMenu()

def login():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Login")
    print("-------------------------------------------------------")
    print("Member (1) | Coach (2) | Treasurer (3) | Go Back (4)")
    accountType = input("Select account type: ")
    if int(accountType) not in range(1,5):
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        login()
    elif int(accountType) in range(1,4):
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
    else:
        entryMenu()

def memberMainPage():
    #options for user to choose from:
    #-attend class
    #   -show the schedule of classes
    #   -ask what class they would like to attend (by class number)
    #   -add this members username to the list of members who attended this class in classes.txt
    #   -ask the user if they would like to pay for the class.
    #       1. if yes:
    #           -add this members username to the list of members who payed for this class in classes.txt
    #           -remove $10 from the balance of this user in users.txt
    #       2. if no:
    #           -add this members username to the list of members who attended but did not pay for this class in classes.txt

    
    #-pay for classes in advance
    #   -can only pay for a month in advance, we will simulate this by allowing them to pay for classes up to
    #     a month after their last attended class.
    #   -check through all the classes in classes.txt to see which is the last one where they appear in the attended list for.
    #   -show the user a list of classes which happen within the next month of their last attended class.
    #       -do this by checking that either (monthOfClass == monthOfLastAttendedClass AND dayOfClass > dayOfLastAttendedClass) OR (monthOfClass == monthOfLastAttendedClass + 1 AND dayOfClass <= dayOfLastAttendedClass)
    #   -once user has selected which class numbers they want to pay for:
    #       1.deduct $10 per selected class from their balance in users.txt
    #       2.add their username to the list of expectedAttendees for each of the classes they just payed for.

    #-open messageBoard

    #-open private messages/notifications
    #   -print all of the messages in the notifications section of their line in users.txt

    #-logout
    #   -go back to entry menu

    pass

def coachMainPage():
    #options for user to choose from:
    #-send group mail to members 
    #   -this adds a line to messageBoard.txt, then when users open the message board, we just print the whole text file for them

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

    #-logout
    #   -go back to entry menu

    pass

def treasurerMainPage():
    #options for user:
    #-view income statement (generate this based on current state)
    #-view unpaid debt
    #-add/remove coaches
    #-view/edit schedule
    #-pay rent
    #-pay coaches
    pass

def end():
    #Simple exit screen
    os.system('cls')
    print("-------------------------------------------------------")
    print("Thank you for using the Membership System")
    print("-------------------------------------------------------")
    os._exit(0)

if __name__ == "__main__":
    entryMenu()
