def validUserPass(accountType, username, password):
    #checks if username and password match
    return True

def addUser(accountType, firstName, lastName, username, password):
    #add to txt file a line in the format "accountType firstName lastName username password" and a new line.
    #new fields will probably be added to this such as account balance, classes payed for, etc.
    #don't bother checking if user already exists in system, we can add that later if we have time.
    
    pass
def existingUser(accountType,username):
    #loop through the list of currently created user accounts to verify they already have an account
    #Return false if there is not a matching account, otherwise true.
    return True
    #adds user to the database
    pass

def existingUser(accountType,username):
    #returns true if user exists in database, otherwise false
    return True

def displayClasses():
    #should display a formatted list of classes labelled by their ID with some associated info for each one
    pass

def getID(username):
    #finds the user with username matching the username parameter. returns their ID number
    pass

def attendClass(userID, classID, payed):
    #do all associated database actions required to have a member attend a class including money stuff. 
    # payed is a boolean value  (true = member payed when they attended, false = member skipped payment when they attended)
    pass

def validClassID(classID):
    #checks database to see if there exists a class with a matching ID
    pass

def displayClassesWithinNextMonth():
    #in a formatted list print all classes within the next month based on the current date. should be labelled by their ID.
    pass

def payForClass(userID, classID):
    #do all money related database tasks for payment of a class. 
    pass

def displayInbox(userID):
    #prints all messages in the inbox table for this userID in a formatted list
    pass
