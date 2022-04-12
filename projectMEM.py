#this file will only have functions which directly relate to the UI and display text.
#all functions that just perform an action will go in helpers.py

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
        return
    elif selection == '2':
        login()
    elif selection == '0':
        end()
        return
    elif selection == '0':
        end()
        return
    else:
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        entryMenu()
        return
def end():
    #Simple exit screen
    os.system('cls')
    print("-------------------------------------------------------")
    print("Thank you for using the Membership System")
    print("-------------------------------------------------------")
    os._exit(0)

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
        return
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
            return
        else:
            print("An account of that type already exists for that username")
            input("Press any key and enter to go back to the home screen: ")
            entryMenu()
            return
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
        return
    elif int(accountType) in range(1,4):
        username = input("Username: ")
        password = input("Password: ")
        if helpers.validUserPass(accountType, username, password):
            userID = helpers.getID(username)
            if accountType == '1':
                memberMainPage(userID)
                return
            elif accountType == '2':
                coachMainPage(userID)
                return
            else:
                treasurerMainPage(userID)
                return
        else:
            print("Error: Incorrect credentials")
            input("Press any key and enter to continue: ")
            login()
    else:
        entryMenu()
        return

def memberMainPage(userID):
    os.system('cls')
    print("-------------------------------------------------------")
    print("Member Main Page")
    print("-------------------------------------------------------")
    print("Attend a class (1) | Pay for future classes (2) | Open message inbox (3) | Log out (4)")
    selection = input("Selection: ")
    if selection == '1':
        memberAttend(userID)
        return
    elif selection == '2':
        memberPayForFutureClasses(userID)
        return
    elif selection == '3':
        messageInbox(userID)
        return
    elif selection == '4':
        entryMenu()
        return
    else:
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        memberMainPage(userID)
        return

def memberAttend(userID):
    os.system('cls')
    print("-------------------------------------------------------")
    print("Attend a class")
    print("-------------------------------------------------------")
    helpers.displayClasses() #should display a numbered list of classes with some associated info for each one
    classID = int(input("Enter class ID of class you want to select: "))
    payedString = input("Would you like to pay for the class when you attend?(y/n): ")
    if payedString == "y":
        payed = True
    elif payedString == "n":
        payed = False
    else:
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        memberAttend()
        return

    # if helpers.validClassID(classID):
    helpers.attendClass(userID, classID, payed)
    input("Success! Press any key to return to Member main page: ")
    memberMainPage(userID)
    return
    # else:
    #     print('Error: invalid class ID')
    #     input("Press any key and enter to continue: ")
    #     memberAttend(userID)
    #     return

def memberPayForFutureClasses(userID):
    os.system('cls')
    print("-------------------------------------------------------")
    print("Pay for future classes")
    print("-------------------------------------------------------")
    helpers.displayClassesWithinNextMonth()
    print("Type class ID numbers that you would like to pay for seperated by spaces.")
    classIDs = list(map(int, input("Selections: ").split())) #converts input to list of ints
    for ID in classIDs:
        if not helpers.validClassID(ID):
            print('Error: invalid class ID')
            input("Payment failed. Press any key and enter to continue: ")
            memberPayForFutureClasses(userID)
            return
    for ID in classIDs:
        helpers.payForClass(userID, ID)

    input("Success! Press any key to return to Member main page: ")
    memberMainPage(userID) 
    return  

def messageInbox(userID):
    os.system('cls')
    print("-------------------------------------------------------")
    print("Message Inbox")
    print("-------------------------------------------------------")
    helpers.displayInbox(userID)
    input("Press any key to go back: ")
    memberMainPage(userID)

def coachMainPage(userID):
    os.system('cls')
    print("-------------------------------------------------------")
    print("Coach Main Page")
    print("-------------------------------------------------------")
    print("Send Message (1) | View My Classes (2) | Log out (3)")
    selection = input("Selection: ")
    if selection == '1':
        coachSendMessage(userID)#-send group mail to members.
        return
    elif selection == '2':
        coachViewClasses(userID)#-Shows a list of all classes that coach is scheduled for. From there the coach can manipulate attendance records
        return
    elif selection == '3':
        entryMenu()
        return

def coachSendMessage(UserID):
    pass
def coachViewClasses(UserID):
    pass
def treasurerMainPage():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Treasuer Main Page")
    print("-------------------------------------------------------")
    print("View Finances (1) | Coach List (2) | View Schedule (3) | Member Log (4) | Log out (5)")
    selection = input("Selection: ")
    if selection == '1':
        treasurerFinances()#view income statement, view unpaid debt, pay rent, and pay coaches
        return
    elif selection == '2':
        treasurerCoachList()#add/remove coaches
        return
    elif selection == '3':
        treasurerSchedule()#view/edit schedule
        return
    elif selection == '4':
        treasurerMemberLog()#Create member log
        return
    elif selection == '5':
        entryMenu()
        return
    pass

def treasurerFinances():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Treasuer Main Page")
    print("-------------------------------------------------------")
    print("View Combined Report (1) | Coach List (2) | View Schedule (3) | Log out (4)")
    selection = input("Selection: ")
    #This screen will allow the treasurer to view outstanding balances, pay coaches/rent and generate financal reports
    pass

def treasurerCoachList():
    #In this section the treasurer will be able to see all coaches and edit the list as needed
    pass

def treasurerSchedule():
    #Will generate the monthly schedule and be able to assign coaches
    pass

def treasurerMemberLog():
    #Creates list of all members sorted on attendace for a given month
    pass

if __name__ == "__main__":
    entryMenu()
