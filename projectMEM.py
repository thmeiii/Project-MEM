import os

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
        addUser(accountType, firstName, lastName, username, password)

def login():
    os.system('cls')
    print("-------------------------------------------------------")
    print("Register")
    print("-------------------------------------------------------")
    print("Member (1) | Coach (2) | Treasurer (3)")
    print("Member (1) | Coach (2) | Treasurer (3)")
    accountType = input("Select account type: ")
    if accountType != '1' and accountType != '2' and accountType != '3':
        print("Error: Invalid input")
        input("Press any key and enter to continue: ")
        login()
    else:
        username = input("Username: ")
        password = input("Password: ")
        if validUserPass(username, password):
            mainPage(accountType)
        else:
            print("Error: Incorrect credentials")
            input("Press any key and enter to continue: ")
            login()

    
